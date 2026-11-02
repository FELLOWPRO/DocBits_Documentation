"""Create an isolated country-video extension of the retained DocBits renderer."""
import json
from pathlib import Path

WORK = Path(__file__).resolve().parent
ROOT = WORK / 'pipeline/scripts/settings_assistant/explainer_videos'
LOCALES = ('en', 'de', 'es', 'fr', 'it', 'nl', 'pl', 'pt', 'zh')
catalog = json.loads((WORK / 'catalog.json').read_text())
translations = {lang: json.loads((WORK / f'translations/{lang}.json').read_text()) for lang in LOCALES}
pages = ['edocs_country_' + country['slug'].replace('-', '_') for country in catalog['countries']]

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

(ROOT / 'country_registry.py').write_text('"""Explicit allowlist for documentation-only country films."""\nCOUNTRY_PAGES = ' + repr(tuple(pages)) + '\nDOCS_LOCALES = ' + repr(LOCALES) + '\n')
for country, page in zip(catalog['countries'], pages):
    content = ROOT / 'content' / page
    write(content / 'script.yaml', {
        'page': page, 'segment_ids': ['formats', 'workflow', 'accept'],
        'scenes': ['formats', 'workflow', 'accept'],
        'must_coverage': {key: [key] for key in ('formats', 'workflow', 'accept')},
        'synthetic_only': True,
        'scope': 'Country-specific teaching diagrams; real settings screenshots are supplied separately.',
    })
    write(content / 'labels.yaml', {'labels': translations['en']['labels'], 'purpose': 'Teaching labels, not product controls.'})
    for lang, text in translations.items():
        c = text['countries'][country['slug']]
        narrations = [c['narration'], text['narration_unconfirmed'] if country['status']=='unconfirmed' else text['narration_workflow'], text['narration_accept']]
        write(content / f'locales/{lang}.json', {
            'locale': lang, 'title': c['name'] + ' — ' + text['labels']['formats'],
            'english_audio_badge': '', 'country': c['name'],
            'status': country['status'],
            'representative': country['representative'],
            'syntax': country['syntax'] if country['representative'] else text['labels']['unconfirmed'],
            'segments': [dict(id=key, scene_id=key, narration=narration, caption=narration) for key, narration in zip(('formats','workflow','accept'), narrations)],
            'labels': text['labels'], 'notes': {},
        })
    (ROOT / f'scenes/{page}.py').write_text('from country_scene import CountryScene\n\n\nclass ' + page.capitalize() + '(CountryScene):\n    page_key = ' + repr(page) + '\n')

for name in ('build.py', 'qa.py'):
    p = ROOT / name
    source = p.read_text()
    source = source.replace('ROOT = Path(__file__).resolve().parent', 'from country_registry import COUNTRY_PAGES, DOCS_LOCALES\n\nROOT = Path(__file__).resolve().parent')
    source = source.replace('\n\n\ndef prepare(', '\nPAGE_LOCALES.update({page: DOCS_LOCALES for page in COUNTRY_PAGES})\n\n\ndef prepare(') if name == 'build.py' else source.replace('\n\n\ndef check_all(', '\nPAGE_LOCALES.update({page: DOCS_LOCALES for page in COUNTRY_PAGES})\n\n\ndef check_all(')
    source = source.replace('choices=("layouts", "users", "sub_organizations", "edocs_credit_note"),', 'choices=("layouts", "users", "sub_organizations", "edocs_credit_note", *COUNTRY_PAGES),')
    if name == 'build.py':
        # Country jobs of one locale may render concurrently without sharing scratch files.
        source = source.replace('Path(out) / "work" / locale', 'Path(out) / "work" / page / locale')
    p.write_text(source)
p = ROOT / 'tts.py'
source = p.read_text().replace('ROOT = Path(__file__).resolve().parent', 'from country_registry import COUNTRY_PAGES\n\nROOT = Path(__file__).resolve().parent')
source = source.replace('"page": page,', '"page": "edocs_country" if page in COUNTRY_PAGES else page,')
source = source.replace('choices=("layouts", "users", "sub_organizations", "edocs_credit_note"),', 'choices=("layouts", "users", "sub_organizations", "edocs_credit_note", *COUNTRY_PAGES),')
p.write_text(source)
p = ROOT / 'manifest.py'
source = p.read_text().replace('ROOT = Path(__file__).resolve().parent', 'from country_registry import COUNTRY_PAGES\n\nROOT = Path(__file__).resolve().parent')
source = source.replace('\n\n\ndef source_inputs(', '\nROUTES.update({page: [r"^/settings/manage-xslt/INVOICE(?:/.*)?$"] for page in COUNTRY_PAGES})\n\n\ndef source_inputs(')
p.write_text(source)
p = ROOT / 'manifest.schema.json'
schema = json.loads(p.read_text())
schema['properties']['pages']['propertyNames']['enum'].extend(pages)
schema['properties']['pages']['maxProperties'] += len(pages)
pattern = schema['$defs']['asset']['properties']['key']['pattern']
schema['$defs']['asset']['properties']['key']['pattern'] = pattern.replace('(edocs_credit_note|', '(' + '|'.join(pages) + '|edocs_credit_note|')
write(p, schema)
print(f'Prepared {len(pages)} country films in {len(LOCALES)} locales')
