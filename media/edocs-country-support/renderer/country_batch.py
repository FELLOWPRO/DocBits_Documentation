"""Resumable media build for exactly one documentation locale. No publication."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import fcntl
import json
from pathlib import Path

from country_registry import COUNTRY_PAGES, DOCS_LOCALES
from cache import canonical, digest, write_json
from tts import Provider, request_spec, synthesize
from build import ROOT, build, prepare
from manifest import source_inputs
from qa import audio_check, keyframes
from toolchain import install_fonts
import os


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--locale',required=True,choices=DOCS_LOCALES)
    parser.add_argument('--speech-only',action='store_true')
    parser.add_argument('--credential-file',default='/run/tts-credential')
    parser.add_argument('--workers',type=int,default=3)
    args=parser.parse_args()
    locale=args.locale
    lock=(ROOT/'country-media.lock').open('w')
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    if args.speech_only:
        from dotenv import dotenv_values
        provider=Provider(dotenv_values(args.credential_file)['TOUCHLESS_ADVISOR_API_KEY'])
        settings=json.loads((ROOT/'voice_settings.json').read_text())[locale]
        specs={}
        for page in COUNTRY_PAGES:
            content=json.loads((ROOT/f'content/{page}/locales/{locale}.json').read_text())
            for segment in content['segments']:
                spec=request_spec(page,segment['id'],segment['narration'],locale,settings)
                specs[digest(canonical(spec))]=spec
        def acquire(spec):
            key,meta=synthesize(spec,ROOT/'cache/tts',provider,offline=False)
            print(json.dumps({'stage':'speech','locale':locale,'key':key[:12],'samples':meta['samples']}),flush=True)
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for future in as_completed([pool.submit(acquire,spec) for spec in specs.values()]):
                future.result()
        for page in COUNTRY_PAGES:
            timing=prepare(locale,ROOT/'out',page)
            print(json.dumps({'page':page,'seconds':timing[-1]['end_ms']/1000}),flush=True)
        return
    os.environ['FONTCONFIG_FILE']=str(install_fonts())
    def render(page):
        directory=ROOT/'out'/page
        provenance=directory/f'{locale}.provenance.json'
        if not provenance.exists() or json.loads(provenance.read_text())['source_inputs']!=source_inputs(page):
            build(locale,ROOT/'out',page,poster_at=3.5)
        timing=json.loads((directory/f'{locale}.timing.json').read_text())
        audio=audio_check(ROOT/'out',locale,timing,page)
        write_json(directory/f'{locale}.audio.json',audio)
        destination=ROOT/'out'/'review'/locale/page
        destination.mkdir(parents=True,exist_ok=True)
        keyframes(ROOT/'out',destination,page,[locale])
        print(json.dumps({'stage':'review-ready','page':page,'locale':locale}),flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for future in as_completed([pool.submit(render,page) for page in COUNTRY_PAGES]):
            future.result()


if __name__=='__main__':
    main()
