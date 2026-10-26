# Forge journal export and local editor

The public journal is the repository-root `JOURNAL.md`. Its images and GIFs are in `journal-media/`. The original Macondo export and editing website stay locally in `docs/macondo-journal/`; `docs/` remains ignored. Browser drafts, Queue, Trash, access tokens, and local backups are kept in the ignored `.journal-state/` folder.

## Use the editor

From the repository root:

```bat
npm ci --prefix journal-tools
node journal-tools/server.cjs
```

Alternatively, open `journal-tools/start-journal.cmd` after dependencies are installed. Open <http://127.0.0.1:8876/> while the service is running. The service listens only on this computer.

The existing `docs/macondo-journal/journal.html` editor also loads the local service configuration. Reload that page and choose **Save changes** once to transfer its current browser edits to the repository. Adding entries or moving them between Main, Queue, and Trash saves automatically; after editing text or pictures, choose **Save changes**. Wait for **Repository JOURNAL.md updated** before committing.

If the browser prevents the file-based page from reaching the local service, use **Export backup** in that page, open the localhost editor above, and **Import backup** there. Browser storage belongs to an origin: a file page and localhost do not share it. The localhost editor restores the most recent state saved through this service.

Saving writes:

- `JOURNAL.md`: Main entries only, with original wording, dates, times and recorded durations.
- `journal-media/`: referenced media and extracted pasted pictures. Assets are kept when an entry is queued or trashed so it can be restored.
- `.journal-state/journal.json`: the complete editable Main/Queue/Trash state, excluded from Git.
- `.journal-state/export-report.json`: missing durations/images and export checks, excluded from Git.

No commit, push, or Forge account change is performed automatically.

## Publish to Forge

1. Save the editor and check `.journal-state/export-report.json`. Supply actual missing hours/images yourself; the exporter does not invent them.
2. Commit and push `JOURNAL.md`, `journal-media/`, the `firmware/` rename, and other intended changes. Do not add `.journal-state/` or `docs/`.
3. Attach this GitHub repository to the Forge project and select Git/JOURNAL.md journaling mode with branch `main`.
4. Use **Sync JOURNAL.md** on Forge. Merely attaching a repository is not the documented import action.

Forge matches existing devlogs by their complete heading/title. The first import can duplicate earlier Macondo/manual entries whose titles do not include the exported date prefix. Review that transition in Forge before syncing an already-populated project. Later exports retain stable dated headings. Moving an already-synced entry into Queue or Trash removes it from the next `JOURNAL.md`; Forge's normal sync does not delete previously imported devlogs automatically.

The local editor's uniform body font is preserved. `# YYYY-MM-DD: Title` headings exist only in the Markdown export because Forge needs them as entry boundaries. Each entry retains its original text/image sequence, tables, and animated GIFs. Dashboard HTML links point to the copied source on GitHub; they are not embedded interactive dashboards on Forge.

## Command-line export

```bat
node journal-tools/export.cjs
node journal-tools/export.cjs "C:\path\to\humanoid-journal-backup.json"
node journal-tools/export.cjs --check
npm test --prefix journal-tools
```

Without a filename, the exporter uses `.journal-state/journal.json` if it exists; otherwise it uses the original on-disk `docs/macondo-journal/journal.json` snapshot. Browser-only edits cannot be read by the command-line exporter until saved through the service or supplied as an exported backup.

## Format sources

Checked 2026-10-26 against Hack Club's published source at commit `539cb5988ff991bf091405612d95b55a0645a51e`:

- [Official JOURNAL.md format](https://github.com/hackclub/forge/blob/539cb5988ff991bf091405612d95b55a0645a51e/docs/design/journal-format.md): root filename, YAML frontmatter, dated entry headings, images and `**Total time spent: ...**`.
- [Actual sync/import parser](https://github.com/hackclub/forge/blob/539cb5988ff991bf091405612d95b55a0645a51e/app/jobs/sync_journal_job.rb): root path, heading boundaries, title matching, date extraction and relative image rewriting.
- [Time parser](https://github.com/hackclub/forge/blob/539cb5988ff991bf091405612d95b55a0645a51e/lib/time_spent_parser.rb): decimal hours and minute formats.

The initial on-disk snapshot has 32 entries and 100.65 recorded journal hours. “I have enough data, time to build the final design” has no recorded duration or image, and “Important note to reviewers” has no image. These are reported rather than filled in. The separate aggregate Hackatime value is not converted into a journal entry or added to entry durations.
