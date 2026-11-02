# English publication source: TDD evidence

The journeys were derived from the current publication audit; no external plan was used.

An English author must edit the directory the English GitBook space imports.
A reviewed legacy change must also reach its active counterpart, while newer
published sections remain intact. Translation changes use their existing paths.

## RED and GREEN

- RED checkpoint: e2738f5f0b955c9d6d51e30f80acb7586d4cd213.
  The focused runtime test executed and failed because the default root was
  readme while the active English space imported docbits.
- GREEN checkpoint: f45f77c6f111da4f3a0256d2553f9302c5c37895.
  All 24 focused tests passed after the root and publication check were added.
- Commands run with an isolated Python environment:
  - python -m pytest -q .github/scripts/test_english_source_contract.py
  - python -m coverage run --include="*/english_source_contract.py" -m pytest -q .github/scripts/test_english_source_contract.py
  - python -m coverage report --fail-under=80
- Result: 24 passed; the check has 91% statement coverage (87 statements, 8 missed).

Related regression: the focused tests plus the existing language-bridge suite passed
62 tests. Workflow YAML, main-branch scope, read-only permissions, hosted runner
and two-commit checkout were also checked locally.

## Guarantees

| Behavior | Evidence | Type |
| --- | --- | --- |
| Default root agrees with the active English space | Root regression test | Repository configuration |
| Legacy-only pages and binary assets return a failure | Temporary Git repositories | Integration |
| Active counterparts may preserve newer public sections | Counterpart preservation test | Integration |
| Already published identical content is accepted | Canonical catch-up test | Integration |
| New files, deletions, spaces and unsafe directories are handled | Focused boundary cases | Integration |
| English and translation changes continue through their active paths | Active-source and translation tests | Integration |
| Executable CLI reports the missing published path | Script entrypoint test | End to end |

## Scope and remaining work

The check reads Git objects and does not rewrite documentation or navigation.
It validates source selection, not factual content, image quality, navigation
completeness, or actual GitBook delivery. Branch protection determines whether
the CI result is mandatory.

Historical approved readme-only changes still need individual reconciliation
with their current public pages and ordinary public URL verification. This
change does not mark those tickets complete.
