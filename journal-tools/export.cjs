const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const domino = require('@mixmark-io/domino');
const Turndown = require('turndown');
const gfm = require('turndown-plugin-gfm');

const ROOT = path.resolve(__dirname, '..');
const ARCHIVE = path.join(ROOT, 'docs', 'macondo-journal');
const STATE_DIR = path.join(ROOT, '.journal-state');
const REPOSITORY = 'https://github.com/houseofthe051010/Humanoid-Robot';
const RAW_BASE = 'https://raw.githubusercontent.com/houseofthe051010/Humanoid-Robot/main/';
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

function within(base, relative) {
  const result = path.resolve(base, relative);
  if (!result.startsWith(path.resolve(base) + path.sep)) throw new Error(`Path leaves its allowed folder: ${relative}`);
  return result;
}

function validateState(state) {
  if (!state || !Array.isArray(state.entries)) throw new Error('Expected a journal export with an entries array.');
  const ids = new Set();
  for (const section of ['entries', 'queue', 'trash']) {
    if (state[section] !== undefined && !Array.isArray(state[section])) throw new Error(`Invalid ${section} section.`);
    for (const entry of state[section] || []) {
      if (!entry || typeof entry.title !== 'string' || !entry.title.trim()) throw new Error('Each journal needs a title.');
      if (entry.id) {
        if (ids.has(entry.id)) throw new Error(`Duplicate entry ID: ${entry.id}`);
        ids.add(entry.id);
      }
    }
  }
}

function entryDate(entry) {
  const text = String(entry.dateTime || entry.meta || '');
  const iso = text.match(/\b(\d{4}-\d{2}-\d{2})\b/);
  if (iso) return iso[1];
  const match = text.match(/\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{1,2}),?\s+(\d{4})/i);
  if (!match) throw new Error(`Missing date for "${entry.title}". Set its date in the editor.`);
  return `${match[3]}-${String(MONTHS.findIndex((month) => month.toLowerCase() === match[1].toLowerCase()) + 1).padStart(2, '0')}-${match[2].padStart(2, '0')}`;
}

function duration(entry) {
  const source = entry.hours !== undefined ? String(entry.hours) : String(entry.meta || '').match(/·\s*([\d.]+\s*h(?:ours?)?)\s*·/i)?.[1] || '';
  if (!source.trim()) return null;
  if (!/^\d+(?:\.\d+)?\s*(?:h|hours?|m|minutes?)(?:\s+\d+(?:\.\d+)?\s*(?:m|minutes?))?$/i.test(source.trim())) throw new Error(`Unrecognized duration for "${entry.title}": ${source}`);
  return source.trim();
}

function compile(state) {
  validateState(state);
  const assets = new Map();
  const warnings = [];
  const headings = new Set();
  const metadata = [];
  const entries = state.entries.map((entry) => ({ entry, date: entryDate(entry) })).sort((a, b) => {
    const day = a.date.localeCompare(b.date);
    if (day) return day;
    const aTime = Date.parse(String(a.entry.dateTime || a.entry.meta || '').split('·')[0]);
    const bTime = Date.parse(String(b.entry.dateTime || b.entry.meta || '').split('·')[0]);
    return Number.isFinite(aTime) && Number.isFinite(bTime) ? aTime - bTime : 0;
  });

  function assetUrl(value, image) {
    const url = String(value || '').trim();
    if (!url) return '';
    if (/^https?:\/\//i.test(url) || (!image && /^(?:mailto:|#)/i.test(url))) return url;
    if (/^data:/i.test(url)) {
      const match = url.match(/^data:image\/(png|jpeg|gif|webp|avif|bmp|x-ms-bmp);base64,([a-z0-9+/=\s]+)$/i);
      if (!image || !match) throw new Error('Only embedded raster pictures can be exported.');
      const bytes = Buffer.from(match[2], 'base64');
      const ext = match[1].toLowerCase().replace('jpeg', 'jpg').replace('x-ms-bmp', 'bmp');
      const destination = `journal-media/pasted-${crypto.createHash('sha256').update(bytes).digest('hex')}.${ext}`;
      assets.set(destination, { destination, bytes });
      return destination;
    }
    if (/^(?:blob:|file:|javascript:)/i.test(url)) throw new Error('A picture has a temporary or machine-specific URL. Re-paste it and save before exporting.');
    const [rawPath] = url.split(/[?#]/, 1);
    const source = decodeURIComponent(rawPath).replace(/^\.\//, '').replace(/\\/g, '/');
    if (!/^(?:media|reviews)\//.test(source)) throw new Error(`Unsupported local journal resource: ${source}`);
    within(ARCHIVE, source);
    const destination = source.startsWith('media/') ? `journal-media/${source.slice(6)}` : `journal-media/${source}`;
    assets.set(destination, { destination, source });
    const suffix = url.slice(rawPath.length);
    const encoded = encodeURI(destination).replace(/\(/g, '%28').replace(/\)/g, '%29');
    return image ? encoded : `${REPOSITORY}/blob/main/${encoded}${suffix}`;
  }

  const blocks = entries.map(({ entry, date }) => {
    const title = entry.title.replace(/[\r\n]+/g, ' ').trim();
    const heading = `${date}: ${title}`;
    if (headings.has(heading)) throw new Error(`Duplicate date/title: ${heading}`);
    headings.add(heading);
    const time = duration(entry);
    const document = domino.createDocument(`<div id="entry">${entry.offlineContentHtml ?? entry.contentHtml ?? ''}</div>`);
    const body = document.getElementById('entry');
    const images = Array.from(body.querySelectorAll('img'));
    if (!time) warnings.push({ title, issue: 'missing_duration', message: 'No duration was recorded. Add the actual time in the editor.' });
    if (!images.length) warnings.push({ title, issue: 'missing_image', message: 'Forge expects a progress image for each entry.' });
    for (const headingNode of Array.from(body.querySelectorAll('h1,h2,h3,h4,h5,h6'))) {
      const paragraph = document.createElement('p');
      paragraph.innerHTML = headingNode.innerHTML;
      headingNode.parentNode.replaceChild(paragraph, headingNode);
    }
    for (const image of images) image.setAttribute('src', assetUrl(image.getAttribute('src'), true));
    for (const link of Array.from(body.querySelectorAll('a[href]'))) link.setAttribute('href', assetUrl(link.getAttribute('href'), false));
    for (const video of Array.from(body.querySelectorAll('video'))) {
      const source = video.getAttribute('src') || video.querySelector('source')?.getAttribute('src');
      if (source) video.setAttribute('data-forge-video', assetUrl(source, false).replace(`${REPOSITORY}/blob/main/`, RAW_BASE));
    }
    const converter = new Turndown({ headingStyle: 'atx', codeBlockStyle: 'fenced', bulletListMarker: '-' });
    converter.use(gfm.gfm);
    converter.addRule('journal-video', {
      filter: 'video',
      replacement: (_content, node) => `\n\n[Video](${node.getAttribute('data-forge-video') || ''})\n\n`,
    });
    let markdown = converter.turndown(body.innerHTML).trim();
    if (/^#{1,2}\s/m.test(markdown)) throw new Error(`Body contains a heading that Forge would mistake for a separate entry: ${title}`);
    if (/\*\*Total time spent:/i.test(markdown)) warnings.push({ title, issue: 'existing_time_footer', message: 'Check the existing time footer against the recorded duration.' });
    const timestamp = String(entry.dateTime || entry.meta || '').split('·')[0].trim();
    metadata.push({ title, forgeTitle: heading, date, timeSpent: time, images: images.length });
    return `# ${heading}\n\nDate: ${date}${timestamp ? ` (${timestamp})` : ''}\n\n${markdown}\n\n**Total time spent: ${time || 'not recorded'}**`;
  });
  const frontmatter = [
    '---',
    'title: "Humanoid Robot"',
    'author: "Aditya"',
    'description: "I am building a human-sized humanoid robot, including its mechanical design, motor control and simulation."',
    `created_at: "${entries[0]?.date || new Date().toISOString().slice(0, 10)}"`,
    '---',
  ].join('\n');
  return {
    markdown: `${frontmatter}\n\n${blocks.join('\n\n')}\n`,
    assets: Array.from(assets.values()),
    report: { entries: entries.length, excludedQueue: (state.queue || []).length, excludedTrash: (state.trash || []).length, warnings, metadata },
  };
}

function writeAtomic(filename, text) {
  fs.mkdirSync(path.dirname(filename), { recursive: true });
  const temporary = `${filename}.${process.pid}.tmp`;
  fs.writeFileSync(temporary, text);
  fs.renameSync(temporary, filename);
}

function writeExport(state, options = {}) {
  const root = options.root || ROOT;
  const archive = options.archive || ARCHIVE;
  const result = compile(state);
  const copied = new Set();
  function copyFile(source, destination) {
    const target = within(root, destination);
    const file = fs.statSync(source);
    if (!file.isFile() || file.size >= 100 * 1024 * 1024) throw new Error(`Resource is not a GitHub-compatible file: ${source}`);
    fs.mkdirSync(path.dirname(target), { recursive: true });
    if (!fs.existsSync(target) || fs.statSync(target).size !== file.size) fs.copyFileSync(source, target);
    copied.add(destination);
  }
  function copyReviewTree(relative) {
    const folder = path.posix.dirname(relative);
    function walk(directory) {
      for (const item of fs.readdirSync(within(archive, directory), { withFileTypes: true })) {
        const child = `${directory}/${item.name}`;
        if (item.isSymbolicLink()) throw new Error(`Review resource contains a symbolic link: ${child}`);
        if (item.isDirectory()) walk(child);
        else copyFile(within(archive, child), `journal-media/${child}`);
      }
    }
    walk(folder);
  }
  for (const asset of result.assets) {
    if (asset.bytes) writeAtomic(within(root, asset.destination), asset.bytes);
    else if (asset.source.startsWith('reviews/')) copyReviewTree(asset.source);
    else copyFile(within(archive, asset.source), asset.destination);
  }
  writeAtomic(path.join(root, 'JOURNAL.md'), result.markdown);
  const report = { ...result.report, copiedResourceFiles: copied.size, generatedAt: new Date().toISOString(), sourceSavedAt: state.savedAt || null };
  writeAtomic(path.join(root, '.journal-state', 'export-report.json'), JSON.stringify(report, null, 2) + '\n');
  return report;
}

function loadState(filename) {
  const saved = path.join(STATE_DIR, 'journal.json');
  const source = filename || (fs.existsSync(saved) ? saved : path.join(ARCHIVE, 'journal.json'));
  return JSON.parse(fs.readFileSync(source, 'utf8'));
}

if (require.main === module) {
  try {
    const filename = process.argv[2] && process.argv[2] !== '--check' ? path.resolve(process.argv[2]) : undefined;
    const state = loadState(filename);
    const result = process.argv.includes('--check') ? compile(state).report : writeExport(state);
    console.log(JSON.stringify(result, null, 2));
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}

module.exports = { ROOT, ARCHIVE, STATE_DIR, compile, writeExport, writeAtomic, loadState, validateState };
