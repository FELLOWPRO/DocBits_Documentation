# NOVA release availability correction

Reviewed on 16 October 2026. This evidence file is outside the published GitBook content roots.

## Confirmed schedule

- NOVA R1.1 is available in the sandbox from **16 October 2026**, confirmed by the user on that date.
- NOVA R1.1 production availability is planned for **4 November 2026**.
- The next VESTA hotfix remains planned for **11 November 2026**.

Jira's `Release No.` field (`customfield_10392`) was read on 16 October 2026:

- [CORE-2303](https://fellowpro.atlassian.net/browse/CORE-2303) and [CORE-6230](https://fellowpro.atlassian.net/browse/CORE-6230) both have `R1.1 (16-10-26/04-11-26)`.
- [CORE-6274](https://fellowpro.atlassian.net/browse/CORE-6274) has `R1.0.16 (04-11-26/11-11-26)`, consistent with the VESTA hotfix production date.
- The existing roadmap already lists the two R1.1 dates as sandbox and production respectively.

## Documentation scope

Update the release overview, NOVA release detail, VESTA hotfix preview, release navigation, and existing roadmap and release lifecycle pages. Include English (`readme/` and `docbits/`), German, Spanish, French, Italian, Dutch, Polish, Portuguese and Chinese. Keep the seven translation source branches in parity with the published language folders.

NOVA is explicitly available for sandbox testing, with production planned for 4 November. Former VESTA beta features are described in that availability context. The 16 service versions and individual deployment timestamps remain the 16 October sandbox snapshot; they do not establish the final production builds.

Keep all existing documentation and video URLs unchanged, including the existing dated NOVA path, so published links continue to work. Video language selection remains unchanged: German walkthroughs use German links without redundant English alternatives.

## Validation

- All 59 edited published pages passed the repository's GitBook tag and front matter validation.
- Link target lists and all service-version table rows are identical before and after the edit.
- The correct production date appears in the release overview, NOVA detail, VESTA preview and navigation in every existing release-note language.
- `git diff --check` passed.
