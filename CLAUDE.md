<!-- gitbook-agent-instructions:start -->

## GitBook Documentation Editing

This repository contains documentation synced with GitBook via Git Sync.

Before editing GitBook-synced Markdown, YAML, or asset files, make sure the GitBook skill is available and up to date in your local agent environment. Prefer installing or updating it with:

```bash
npx skills add gitbookio/gitbook-skills
```

This command may add or update local agent skill files. Use them only as local agent instructions; do not commit those installed skill files or any tool-generated agent configuration unless the user explicitly asks for it.

If `npx` is unavailable, load the skill from:

https://gitbook.com/docs/skill.md

When making changes, preserve GitBook sync metadata such as frontmatter, `SUMMARY.md`, `gitbook-docs.yaml`, `.gitbook/`, and asset links unless the requested edit explicitly requires changing them.

<!-- gitbook-agent-instructions:end -->

## Languages and GitBook Git Sync

Since 2026-11-03 **every language space has its own Git Sync on its own branch**. The
English space syncs from `main`, folder `docbits/`. Do not move the language spaces back
to folders on `main`.

| Language | Branch (edit and merge here) | Content root |
|---|---|---|
| English | `main` | `docbits/` (images in `docbits/.gitbook/assets/`) |
| German, Spanish, French, Italian, Dutch, Polish, Portuguese, Chinese | `de`, `es`, `fr`, `it`, `nl`, `pl`, `pt`, `zh` | `readme/` (`.gitbook.yaml`: `root: ./readme/`) |

- A translation is published by merging its PR into the language branch. GitBook picks it
  up through that space's Git Sync. There is no bridge workflow any more.
- The folders `deutsch/`, `espanol/`, `french/`, `italian/`, `dutch/`, `polish/`,
  `portuguese/`, `chinese/` on `main` are **frozen and obsolete**. Never edit them and never
  read them as a source; use the language branch.
- `gitbook-docs.yaml` on `main` is written by GitBook (site structure). In it the language
  spaces have `directory: null`; do not edit it by hand.
- Docs changes to a page need the matching change on every language branch.
- The search index (Docs Search Sync) reads the language pages from the language branches
  (`readme/`) and English from `docbits/` on `main`.

## Video hosting

Publish video files to the DigitalOcean Spaces bucket `docbits-videos` in `fra1`.
Use absolute playback, caption and poster URLs under
`https://docbits-videos.fra1.cdn.digitaloceanspaces.com/`.
Keep video binaries out of Git and GitBook file uploads. Commit documentation links
only. Publish changed media under a new immutable version; never overwrite an
existing video object.
