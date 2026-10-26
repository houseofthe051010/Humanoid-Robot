const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { JSDOM, VirtualConsole } = require('jsdom');
const { compile, writeExport, ROOT } = require('./export.cjs');
const { createService } = require('./server.cjs');

const PNG = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aY9sAAAAASUVORK5CYII=';
const IMAGE = `data:image/png;base64,${PNG}`;
const tests = [];
const folder = fs.mkdtempSync(path.join(os.tmpdir(), 'humanoid-journal-test-'));
const archive = path.join(folder, 'docs', 'macondo-journal');
fs.mkdirSync(archive, { recursive: true });
const fixture = '<!doctype html><html><head></head><body><main><section class="hero"><div class="stats"><span class="stat">2h total</span><span class="stat">2h journals</span><span class="stat">0h Hackatime</span><span class="stat">1 entries</span></div></section><article class="entry" id="main-entry"><header><span>NEW</span><div><h2>Main entry</h2><p>Oct 25, 2026, 4:20 PM · 2h · Aditya</p></div></header><div class="content"><p>Original writing.</p></div></article></main><script src="../../.journal-state/client-config.js"></script></body></html>';
fs.writeFileSync(path.join(archive, 'journal.html'), fixture);
const state = {
  version: 8,
  savedAt: '2026-10-26T18:00:00.000Z',
  entries: [{ id: 'main-entry', title: 'Main entry', meta: 'Oct 25, 2026, 4:20 PM · 2h · Aditya', contentHtml: `<p>Before picture.</p><img src="${IMAGE}"><p>After picture.</p>` }],
  queue: [{ id: 'queue-entry', title: 'Private queued entry', meta: 'Oct 26, 2026, 4:20 PM · 8h · Aditya', contentHtml: '<p>Queued material.</p>' }],
  trash: [{ id: 'trash-entry', title: 'Private trashed entry', meta: 'Oct 26, 2026, 5:20 PM · 5h · Aditya', contentHtml: '<p>Trashed material.</p>' }],
};

// Reproduces the boundaries and time extraction in Forge's published SyncJournalJob.
function parseLikeForge(markdown) {
  const source = markdown.replace(/^---\s*\n[\s\S]*?\n---\s*\n/, '');
  const entries = [];
  let current;
  for (const line of source.split('\n')) {
    const match = line.match(/^(#+)\s+(.+)$/);
    if (match && match[1].length === 1) {
      current = { title: match[2].trim(), body: [] };
      entries.push(current);
    } else if (current) current.body.push(line);
  }
  return entries.filter((entry) => entry.title.length >= 3 && !/^(TOTAL|More|---)/i.test(entry.title)).map((entry) => {
    const body = entry.body.join('\n').trim();
    return { title: entry.title, body, time: body.match(/\*\*Total time spent:\s*(.+?)\*\*/i)?.[1] || null };
  });
}

async function until(condition) {
  for (let i = 0; i < 150; i++) {
    if (condition()) return;
    await new Promise((resolve) => setTimeout(resolve, 10));
  }
  throw new Error('Timed out waiting for editor/server save.');
}

(async () => {
  const result = compile(state);
  assert.equal(result.report.entries, 1);
  assert.ok(!result.markdown.includes('Private queued entry'));
  assert.ok(!result.markdown.includes('Private trashed entry'));
  assert.ok(result.markdown.indexOf('Before picture.') < result.markdown.indexOf('!['));
  assert.ok(result.markdown.indexOf('![') < result.markdown.indexOf('After picture.'));
  assert.ok(!result.markdown.includes('data:image'));
  assert.equal(result.assets.length, 1);
  assert.equal(result.assets[0].bytes.toString('base64'), PNG);
  assert.equal(parseLikeForge(result.markdown)[0].time, '2h');
  assert.throws(() => compile({ entries: [{ ...state.entries[0], contentHtml: '<img src="media/../../private.png">' }] }), /allowed folder/);
  tests.push('Main-only conversion preserves text/image order, dates, time and pasted image bytes; unsafe paths rejected.');

  const snapshot = JSON.parse(fs.readFileSync(path.join(ROOT, 'docs', 'macondo-journal', 'journal.json'), 'utf8'));
  const exported = compile(snapshot);
  const parsed = parseLikeForge(exported.markdown);
  assert.equal(parsed.length, snapshot.entries.length);
  assert.equal(parsed.length, 32);
  assert.ok(parsed.some((entry) => entry.title.endsWith(': More research')));
  assert.equal(parsed.filter((entry) => /^\d{4}-\d{2}-\d{2}: /.test(entry.title)).length, 32);
  assert.equal(parsed.filter((entry) => entry.time && entry.time !== 'not recorded').length, 31);
  const total = parsed.reduce((sum, entry) => sum + (entry.time === 'not recorded' ? 0 : Number.parseFloat(entry.time)), 0);
  assert.ok(Math.abs(total - 100.65) < 0.0001);
  assert.equal(exported.report.warnings.length, 3);
  tests.push('All 32 snapshot entries parse with Forge heading/time rules; 100.65 recorded hours retained, missing data flagged.');

  const service = createService({ root: folder, archive, port: 0 });
  const { apiBase, token } = await service.listen();
  let dom;
  try {
    const headers = { 'Content-Type': 'application/json', 'X-Journal-Token': token, Origin: 'null' };
    let response = await fetch(`${apiBase}/api/save`, { method: 'POST', headers, body: JSON.stringify(state) });
    assert.equal(response.status, 200);
    assert.equal((await response.json()).entries, 1);
    const generated = fs.readFileSync(path.join(folder, 'JOURNAL.md'), 'utf8');
    assert.equal(parseLikeForge(generated).length, 1);
    const persisted = JSON.parse(fs.readFileSync(path.join(folder, '.journal-state', 'journal.json'), 'utf8'));
    assert.equal(persisted.queue.length, 1);
    assert.equal(persisted.trash.length, 1);
    assert.equal(fs.readFileSync(path.join(folder, result.assets[0].destination)).toString('base64'), PNG);
    response = await fetch(`${apiBase}/api/save`, { method: 'POST', headers: { ...headers, Origin: 'https://unrelated.example' }, body: JSON.stringify(state) });
    assert.equal(response.status, 403);
    response = await fetch(`${apiBase}/api/save`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(state) });
    assert.equal(response.status, 401);
    response = await fetch(`${apiBase}/api/save`, { method: 'POST', headers, body: JSON.stringify({ ...state, savedAt: '2026-10-25T00:00:00.000Z' }) });
    assert.equal(response.status, 409);
    assert.equal((await fetch(`${apiBase}/.journal-state/journal.json`)).status, 404);
    const served = await (await fetch(`${apiBase}/`)).text();
    assert.ok(served.includes('/journal-config.js'));
    tests.push('Local-only authenticated save writes root files; Queue/Trash stay private; untrusted requests and stale saves rejected.');

    const errors = [];
    const virtualConsole = new VirtualConsole();
    virtualConsole.on('jsdomError', (error) => errors.push(error.message));
    dom = new JSDOM(fixture, { url: `${apiBase}/`, runScripts: 'outside-only', virtualConsole });
    const w = dom.window;
    w.HTMLElement.prototype.scrollIntoView = function () {};
    w.JOURNAL_REPO_CONFIG = { apiBase, token };
    w.JOURNAL_REPO_INITIAL_STATE = state;
    w.fetch = (url, options) => fetch(url, { ...options, headers: { ...options.headers, Origin: apiBase } });
    w.eval(fs.readFileSync(path.join(ROOT, 'docs', 'macondo-journal', 'journal-editor.js'), 'utf8'));
    assert.equal(w.document.querySelectorAll('#journal-queue-entries > .entry').length, 1);
    assert.equal(w.document.querySelectorAll('#journal-trash-entries > .entry').length, 1);
    w.document.querySelector('[data-action="edit"]').click();
    w.document.querySelector('#main-entry .content').innerHTML = `<p>Edited through the website.</p><img src="${IMAGE}"><p>Image follows the text.</p>`;
    w.document.querySelector('[data-action="save"]').click();
    await until(() => w.document.querySelector('[role="status"]').textContent.includes('Repository JOURNAL.md updated'));
    assert.ok(fs.readFileSync(path.join(folder, 'JOURNAL.md'), 'utf8').includes('Edited through the website.'));
    w.document.querySelector('#main-entry [data-entry-action="trash"]').click();
    await until(() => parseLikeForge(fs.readFileSync(path.join(folder, 'JOURNAL.md'), 'utf8')).length === 0);
    assert.equal(JSON.parse(fs.readFileSync(path.join(folder, '.journal-state', 'journal.json'), 'utf8')).trash.length, 2);
    w.document.querySelector('#main-entry [data-entry-action="restore-main"]').click();
    await until(() => parseLikeForge(fs.readFileSync(path.join(folder, 'JOURNAL.md'), 'utf8')).length === 1);
    assert.deepEqual(errors, []);
    tests.push('Actual editor Save -> localhost API -> JOURNAL.md verified in an isolated DOM; Trash removes and Restore re-adds the exported entry.');
  } finally {
    dom?.window.close();
    await new Promise((resolve) => service.server.close(resolve));
  }
  console.log(JSON.stringify({ passed: true, tests, limitation: 'No Forge account sync or live browser interaction was performed.' }, null, 2));
})().catch((error) => { console.error(error); process.exitCode = 1; }).finally(() => {
  const resolved = path.resolve(folder);
  if (resolved.startsWith(path.resolve(os.tmpdir()) + path.sep) && path.basename(resolved).startsWith('humanoid-journal-test-')) fs.rmSync(resolved, { recursive: true, force: true });
});
