#!/usr/bin/env python3
"""Check workflow-card references without executing a workflow or calling an API.

Run from the repository root. Sparse checkouts are supported: tracked link targets
are checked against the Git tree as well as the working tree.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

ROOTS = {'en': 'docbits', 'de': 'deutsch', 'es': 'espanol', 'fr': 'french',
         'it': 'italian', 'nl': 'dutch', 'pl': 'polish', 'pt': 'portuguese', 'zh': 'chinese'}
NEW_GUIDES = ('logic-cards-guide.md', 'export-cards-guide.md',
              'po-comparison-versions-guide.md', 'quote-comparison-guide.md', 'card-versions-guide.md')
TAGS = ('hint', 'tabs', 'tab', 'code', 'stepper', 'step', 'columns', 'column')


def lexical(path: Path) -> str:
    import posixpath
    return posixpath.normpath(path.as_posix())


def front_matter(text: str) -> str | None:
    """Compare technical metadata by value, allowing GitBook YAML formatting."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return "UNCLOSED"
    block = text[4:end]
    try:
        import yaml
        data = yaml.safe_load(block) or {}
        if not isinstance(data, dict):
            return "INVALID"
    except ImportError:
        # The current card pages use flat boolean metadata. Full GitBook YAML
        # validation is also run with language_bridge.py before publication.
        data = {}
        for line in block.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*$", line)
            if not match:
                return "INVALID"
            key, value = match.groups()
            value = value.split(" #", 1)[0].strip()
            data[key] = {"true": True, "false": False}.get(value.lower(), value)
    except Exception:
        return "INVALID"
    technical = {key: value for key, value in data.items()
                 if key not in {"description", "title"}}
    return json.dumps(technical, sort_keys=True, ensure_ascii=False)


def technical_identifiers(text: str) -> Counter:
    """Escaped API card identifiers must also survive translation in prose."""
    values = re.findall(r"[\w]+(?:\\_[\w]+)+", text)
    return Counter(value for value in values
                   if value.replace("\\_", "_").isupper() or value == "tasks\\_create")


def navigated_card_path(folder: str, reference: str, navigation: set[str]) -> str | None:
    """Resolve both canonical and flat language-branch paths from SUMMARY."""
    workflow = 'administration-and-setup/workflow/'
    candidates = [workflow + 'cards-overview/' + reference]
    candidates.append(workflow + ('cards-overview.md' if reference == 'README.md' else reference))
    direct = next((folder + '/' + path for path in candidates if path in navigation), None)
    if direct is not None:
        return direct
    # Older language branches keep the cross-category guides in a related
    # category folder. Their SUMMARY nesting still gives them a cards URL.
    if '/' not in reference and reference.endswith('-guide.md'):
        matches = [path for path in navigation if path.startswith(workflow)
                   and path.endswith('/' + reference)]
        if len(matches) == 1:
            return folder + '/' + matches[0]
    return None


def check(repo: Path, locales: list[str]) -> list[str]:
    tracked = set(subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', 'HEAD'], cwd=repo, text=True).splitlines())
    present = {p.relative_to(repo).as_posix() for folder in ROOTS.values()
               for p in (repo / folder / 'administration-and-setup/workflow').rglob('*.md')}
    existing = tracked | present
    errors = []
    english = repo / 'docbits/administration-and-setup/workflow/cards-overview'
    expected = {p.relative_to(english).as_posix() for p in english.rglob('*.md')}
    for lang in locales:
        summary = (repo / ROOTS[lang] / 'SUMMARY.md').read_text()
        navigation = {unquote(p) for p in re.findall(r'\]\(([^)]+\.md)\)', summary)}
        resolved = {reference: navigated_card_path(ROOTS[lang], reference, navigation)
                    for reference in expected}
        actual = {reference: repo / path for reference, path in resolved.items()
                  if path is not None and (repo / path).is_file()}
        for missing in sorted(expected - actual.keys()):
            errors.append(f'{lang}: missing navigated card reference {missing}')
        for guide in NEW_GUIDES:
            if f'workflow/cards-overview/{guide})' not in summary:
                errors.append(f'{lang}: new guide is absent from SUMMARY: {guide}')
        pages = sorted(actual.values())
        sources = {page: english / reference for reference, page in actual.items()}
        for page in pages:
            rel = page.relative_to(repo).as_posix()
            text = page.read_text()
            source = sources[page]
            expected_metadata = front_matter(source.read_text()) if source.exists() else None
            required_ids = technical_identifiers(source.read_text()) if source.exists() else Counter()
            actual_ids = technical_identifiers(text)
            for identifier, count in (required_ids - actual_ids).items():
                errors.append(f'{rel}: technical identifier missing or translated: {identifier} ({count} occurrences)')

            actual_metadata = front_matter(text)
            if actual_metadata in {"UNCLOSED", "INVALID"}:
                errors.append(f'{rel}: invalid or unclosed frontmatter')
            elif expected_metadata is not None and actual_metadata != expected_metadata:
                errors.append(f'{rel}: technical frontmatter differs from the English source')
            if not re.search(r'^# .+', text, re.M):
                errors.append(f'{rel}: missing page title')
            if re.search(r'ZXQSEG\d+QXZ|⟦P\d+⟧', text):
                errors.append(f'{rel}: unresolved translation marker')
            # Ignore literal examples when checking GitBook block delimiters.
            prose = re.sub(r'(?ms)^\s*```.*?^\s*```[^\n]*', '', text)
            for tag in TAGS:
                opened = len(re.findall(r'\{%\s*' + tag + r'(?:\s|%)', prose))
                closed = len(re.findall(r'\{%\s*end' + tag + r'\s*%\}', prose))
                if opened != closed:
                    errors.append(f'{rel}: unbalanced {tag} block ({opened}/{closed})')
            for target in re.findall(r'\]\(([^)]+)\)', prose):
                target = unquote(target.split('#')[0])
                if not target or re.match(r'[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('<'):
                    continue
                dest = lexical(page.parent.relative_to(repo) / target)
                if dest not in existing and dest + '/README.md' not in existing and dest + '.md' not in existing:
                    errors.append(f'{rel}: missing link target {target}')
        print(f'{lang}: {len(pages)} card-reference pages; {len(expected - actual.keys())} missing')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--language', action='append', choices=ROOTS)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    errors = check(repo, args.language or list(ROOTS))
    for error in errors:
        print('ERROR:', error)
    print(f'Workflow-card reference check: {len(errors)} errors')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
