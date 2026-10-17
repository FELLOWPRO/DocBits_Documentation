"""Assemble every real screenshot and every film's three scenes for inspection."""
import json
from pathlib import Path
import sys
from PIL import Image,ImageDraw

WORK=Path(__file__).resolve().parent
lang=sys.argv[1]
countries=json.loads((WORK/'catalog.json').read_text())['countries']
dest=WORK/'reviews'/lang
dest.mkdir(parents=True,exist_ok=True)
pipeline=WORK/'pipeline/scripts/settings_assistant/explainer_videos'
for offset in range(0,len(countries),8):
    sheet=Image.new('RGB',(1600,1360),'#eeeeee')
    draw=ImageDraw.Draw(sheet)
    for index,c in enumerate(countries[offset:offset+8]):
        file=WORK/f'screenshots/{lang}/edocs-support-{c["slug"]}-{lang}.png'
        im=Image.open(file).convert('RGB');im.thumbnail((790,300))
        if c['representative']:assert Image.open(file).height>300,file
        x=index%2*800;y=index//2*340;sheet.paste(im,(x,y));draw.text((x+8,y+306),c['slug'],fill='#111111')
    sheet.save(dest/f'screenshots-{offset//8}.jpg',quality=88)
    if not (pipeline/'out'/('edocs_country_'+countries[offset]['slug'].replace('-','_'))/f'{lang}.provenance.json').exists():continue
    sheet=Image.new('RGB',(1152,8*244),'#0a2531');draw=ImageDraw.Draw(sheet)
    for index,c in enumerate(countries[offset:offset+8]):
        page='edocs_country_'+c['slug'].replace('-','_')
        for column,segment in enumerate(('formats','workflow','accept')):
            im=Image.open(pipeline/f'out/review/{lang}/{page}/{lang}-{segment}-drawer.png').convert('RGB')
            sheet.paste(im,(column*384,index*244))
        draw.text((8,index*244+216),c['slug']+' / '+lang,fill='white')
    sheet.save(dest/f'films-{offset//8}.jpg',quality=90)
print(dest)
