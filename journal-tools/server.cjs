const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { ROOT, writeExport, writeAtomic, validateState } = require('./export.cjs');

function createService(options = {}) {
  const root = options.root || ROOT;
  const archive = options.archive || path.join(root, 'docs', 'macondo-journal');
  const privateFolder = path.join(root, '.journal-state');
  fs.mkdirSync(privateFolder, { recursive: true });
  const tokenFile = path.join(privateFolder, 'access-token');
  const token = fs.existsSync(tokenFile) ? fs.readFileSync(tokenFile, 'utf8').trim() : crypto.randomBytes(32).toString('hex');
  if (!fs.existsSync(tokenFile)) writeAtomic(tokenFile, token);
  const stateFile = path.join(privateFolder, 'journal.json');
  let savedState = fs.existsSync(stateFile) ? JSON.parse(fs.readFileSync(stateFile, 'utf8')) : null;
  let apiBase;
  let saveQueue = Promise.resolve();
  const mime = { '.html': 'text/html; charset=utf-8', '.js': 'application/javascript; charset=utf-8', '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.webp': 'image/webp', '.mp4': 'video/mp4', '.csv': 'text/csv; charset=utf-8' };

  const server = http.createServer(async (request, response) => {
    response.setHeader('Cache-Control', 'no-store');
    response.setHeader('X-Content-Type-Options', 'nosniff');
    response.setHeader('X-Frame-Options', 'DENY');
    const send = (status, value) => {
      response.writeHead(status, { 'Content-Type': 'application/json' });
      response.end(JSON.stringify(value));
    };
    try {
      const authority = new URL(apiBase).host;
      if (request.headers.host !== authority) return send(403, { error: 'Unexpected host.' });
      const origin = request.headers.origin;
      if (origin && origin !== 'null' && origin !== apiBase) return send(403, { error: 'Only the local journal editor can access this service.' });
      if (origin) {
        response.setHeader('Access-Control-Allow-Origin', origin);
        response.setHeader('Vary', 'Origin');
        response.setHeader('Access-Control-Allow-Private-Network', 'true');
      }
      if (request.method === 'OPTIONS') {
        response.writeHead(204, { 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type, X-Journal-Token' });
        return response.end();
      }
      const url = new URL(request.url, apiBase);
      if (url.pathname.startsWith('/api/')) {
        const supplied = String(request.headers['x-journal-token'] || '');
        if (supplied.length !== token.length || !crypto.timingSafeEqual(Buffer.from(supplied), Buffer.from(token))) return send(401, { error: 'Local journal access token is missing or invalid.' });
        if (url.pathname === '/api/status' && request.method === 'GET') return send(200, { service: 'humanoid-journal', entries: savedState?.entries.length ?? null });
        if (url.pathname !== '/api/save' || request.method !== 'POST') return send(404, { error: 'Unknown API route.' });
        if (!String(request.headers['content-type']).startsWith('application/json')) return send(415, { error: 'Expected JSON.' });
        const chunks = [];
        let size = 0;
        for await (const chunk of request) {
          size += chunk.length;
          if (size > 100 * 1024 * 1024) return send(413, { error: 'Journal exceeds the 100 MB save limit. Export a backup before reducing image sizes.' });
          chunks.push(chunk);
        }
        const state = JSON.parse(Buffer.concat(chunks).toString('utf8'));
        validateState(state);
        const operation = saveQueue.then(() => {
          if (savedState?.savedAt && state.savedAt && Date.parse(state.savedAt) < Date.parse(savedState.savedAt)) {
            const error = new Error('A newer journal was already saved by another tab. Reload or export a backup before merging edits.');
            error.status = 409;
            throw error;
          }
          const report = writeExport(state, { root, archive });
          const backup = path.join(privateFolder, 'backups', `${new Date().toISOString().slice(0, 10)}.json`);
          if (fs.existsSync(stateFile) && !fs.existsSync(backup)) {
            fs.mkdirSync(path.dirname(backup), { recursive: true });
            fs.copyFileSync(stateFile, backup);
          }
          writeAtomic(stateFile, JSON.stringify(state, null, 2) + '\n');
          savedState = state;
          return report;
        });
        saveQueue = operation.catch(() => {});
        const report = await operation;
        return send(200, { ok: true, entries: report.entries, warnings: report.warnings });
      }
      if (request.method !== 'GET' && request.method !== 'HEAD') return send(405, { error: 'Method not allowed.' });
      if (request.headers['sec-fetch-site'] === 'cross-site') return send(403, { error: 'Cross-site access is not allowed.' });
      if (url.pathname === '/journal-config.js') {
        const config = { apiBase, token };
        const script = `window.JOURNAL_REPO_CONFIG=${JSON.stringify(config)};window.JOURNAL_REPO_INITIAL_STATE=${JSON.stringify(savedState).replace(/</g, '\\u003c')};`;
        response.writeHead(200, { 'Content-Type': mime['.js'] });
        return response.end(script);
      }
      const relative = url.pathname === '/' ? 'journal.html' : decodeURIComponent(url.pathname.slice(1));
      const filename = path.resolve(archive, relative);
      if (!filename.startsWith(path.resolve(archive) + path.sep) || !mime[path.extname(filename).toLowerCase()]) return send(404, { error: 'Not found.' });
      if (!fs.existsSync(filename) || !fs.statSync(filename).isFile()) return send(404, { error: 'Not found.' });
      if (relative === 'journal.html') {
        const content = fs.readFileSync(filename, 'utf8').replace('../../.journal-state/client-config.js', '/journal-config.js');
        response.writeHead(200, { 'Content-Type': mime['.html'] });
        return response.end(request.method === 'HEAD' ? undefined : content);
      }
      response.writeHead(200, { 'Content-Type': mime[path.extname(filename).toLowerCase()] });
      if (request.method === 'HEAD') return response.end();
      fs.createReadStream(filename).pipe(response);
    } catch (error) { if (!response.headersSent) send(error.status || 400, { error: error.message }); }
  });

  return {
    server,
    listen: () => new Promise((resolve, reject) => {
      server.once('error', reject);
      server.listen(options.port ?? 8876, '127.0.0.1', () => {
        apiBase = `http://127.0.0.1:${server.address().port}`;
        writeAtomic(path.join(privateFolder, 'client-config.js'), `window.JOURNAL_REPO_CONFIG=${JSON.stringify({ apiBase, token })};\n`);
        writeAtomic(path.join(privateFolder, 'server.pid'), String(process.pid));
        resolve({ apiBase, token });
      });
    }),
  };
}

if (require.main === module) {
  const service = createService();
  service.listen().then(({ apiBase }) => console.log(`Journal editor: ${apiBase}\nSave changes updates ${path.join(ROOT, 'JOURNAL.md')}\nListening only on this computer. Press Ctrl+C to stop.`))
    .catch((error) => { console.error(error.message); process.exitCode = 1; });
}

module.exports = { createService };
