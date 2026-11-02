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

## Video hosting

Publish video files to the DigitalOcean Spaces bucket `docbits-videos` in `fra1`.
Use absolute playback, caption and poster URLs under
`https://docbits-videos.fra1.cdn.digitaloceanspaces.com/`.
Keep video binaries out of Git and GitBook file uploads. Commit documentation links
only. Publish changed media under a new immutable version; never overwrite an
existing video object.
