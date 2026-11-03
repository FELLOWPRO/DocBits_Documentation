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

The GitBook site uses **site-level Git Sync** on `main`: one repository, one branch,
one folder per language space (mapping in `gitbook-docs.yaml`). Do not switch the
spaces to one branch per language.

| Language | Source of truth (edit here) | Folder on `main` (published, bot-written) |
|---|---|---|
| English | `main`, folder `docbits/` | `docbits/` |
| de, es, fr, it, nl, pl, pt, zh | branch `de`, `es`, `fr`, `it`, `nl`, `pl`, `pt`, `zh`, under `readme/` | `deutsch/`, `espanol/`, `french/`, `italian/`, `dutch/`, `polish/`, `portuguese/`, `chinese/` |

- **Never edit** `deutsch/`, `espanol/`, `french/`, `italian/`, `dutch/`, `polish/`,
  `portuguese/` or `chinese/` on `main` by hand. The workflow **Sync Language Folders**
  (`.github/workflows/sync-language-folders.yml`, every 30 minutes) overwrites them
  from the language branches (`.github/scripts/language_bridge.py`).
- Translate on the language branch, merge there, then wait for the next sync run or start
  it manually (Actions > Sync Language Folders, optional `lang`).
- Docs changes to a page need the matching change on every language branch.
- Keep `language:` in `gitbook-docs.yaml` equal to the folder's language (English is `en`).
- If `main` later requires pull requests, the bot `github-actions[bot]` needs a bypass or a PAT.

## Video hosting

Publish video files to the DigitalOcean Spaces bucket `docbits-videos` in `fra1`.
Use absolute playback, caption and poster URLs under
`https://docbits-videos.fra1.cdn.digitaloceanspaces.com/`.
Keep video binaries out of Git and GitBook file uploads. Commit documentation links
only. Publish changed media under a new immutable version; never overwrite an
existing video object.
