# Contributing to DocBits documentation

## English publication

The public documentation lives in **public_docs/** on every branch: English on
**main**, each language on its own branch (`de`, `es`, `fr`, `it`, `nl`, `pl`,
`pt`, `zh`). GitBook reads the folder from the `root:` in **.gitbook.yaml**. Edit
pages and their images in **public_docs/** and **public_docs/.gitbook/assets/**.

The old **readme/** and **docbits/** folders on main are retired. The English
Publication Source check rejects any new or changed file under **readme/** on
main; make the change in **public_docs/** instead.

This check validates source selection. Before completing a documentation ticket,
open the ordinary public page, confirm the intended new text, and inspect the
actual delivered images, alternate text, captions, links, and relevant media.

## Other language spaces

Edit the page selected by **public_docs/SUMMARY.md** on its language branch:
**de**, **es**, **fr**, **it**, **nl**, **pl**, **pt**, or **zh**.
After review and merge, GitBook picks the change up directly: each language
space syncs from its own branch. Verify the new content on the ordinary public
URL before confirming publication in Jira.
