# Contributing to DocBits documentation

## English publication

The English GitBook space imports the **docbits/** directory on **main**.
The active mapping is in **gitbook-docs.yaml**; **.gitbook.yaml** must name the
same default root. Edit English pages and their images in **docbits/** and
**docbits/.gitbook/assets/**.

The legacy **readme/** copy has diverged from the published English source.
When reconciling an older approved change, review the current **docbits/** page
and preserve newer published sections. Apply the intended change to the active
page and its referenced assets. The English Publication Source check rejects a
main-branch change confined to **readme/** unless its exact content is already
present in the active destination. It also checks added, removed, and binary
files. Updating both copies does not require replacing the published page with
the legacy copy.

This check validates source selection. Before completing a documentation ticket,
open the ordinary public page, confirm the intended new text, and inspect the
actual delivered images, alternate text, captions, links, and relevant media.

## Other language spaces

Edit the page selected by **readme/SUMMARY.md** on its language branch:
**de**, **es**, **fr**, **it**, **nl**, **pl**, **pt**, or **zh**.
After review and merge, run **Sync Language Folders** with that language code.
The bridge copies the selected pages and assets into the corresponding
language directory on main. Verify the new content on the ordinary public URL
before confirming publication in Jira.
