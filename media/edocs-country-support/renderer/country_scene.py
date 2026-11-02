"""Country selection, effective configuration and acceptance as causal diagrams."""
import json
import os
from pathlib import Path

from manim import Scene, Text, VGroup, RoundedRectangle, Arrow, Line, ImageMobject, FadeIn, FadeOut, Create, Indicate, config
from brand import BG, SURFACE, BORDER, INK, MUTED, CYAN, GREEN, AMBER
from scenes.common import check_glyphs, font

ROOT = Path(__file__).resolve().parent
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 30
config.renderer = 'cairo'
config.background_color = BG


class CountryScene(Scene):
    def text(self, value, width=13.6, color=INK, size=48):
        check_glyphs(value, self.locale)
        def render(text):
            return Text(text, font=font(self.locale), font_size=size, color=color)
        item = render(value)
        if item.width > width:
            words = list(value) if self.locale == 'zh' else value.split()
            separator = '' if self.locale == 'zh' else ' '
            lines, line = [], []
            for word in words:
                proposed = separator.join(line + [word])
                if line and render(proposed).width > width:
                    lines.append(separator.join(line))
                    line = [word]
                else:
                    line.append(word)
            lines.append(separator.join(line))
            item = render('\n'.join(lines))
        scale = min(1, width / max(item.width, .01), 1.5 / max(item.height, .01))
        if scale < .78:
            raise ValueError(f'Label exceeds teaching panel: {self.locale}: {value}')
        return item.scale(scale)

    def word(self, key, point, width=13.6, color=INK, size=48):
        return self.text(self.content['labels'][key], width, color, size).move_to(point)

    def card(self, value, point, width=5.8, color=CYAN, literal=False):
        title = self.text(value if literal else self.content['labels'][value], width-.6)
        box = RoundedRectangle(width=width, height=max(1.35,title.height+.4), corner_radius=.15, stroke_color=color, stroke_width=3, fill_color=SURFACE, fill_opacity=1)
        return VGroup(box, title).move_to(point)

    def reveal(self, *objects):
        self.play(*[FadeIn(item) for item in objects], run_time=.4)

    def arrow(self, start, end, color=CYAN):
        return Arrow(start,end,buff=.1,color=color,stroke_width=5,max_tip_length_to_length_ratio=.15)

    def formats(self):
        self.reveal(self.text(self.content['country'],color=CYAN,size=52).move_to([0,2.65,0]))
        if self.content['status']=='unconfirmed':
            self.reveal(self.card('unconfirmed',[0,.8,0],13.4,AMBER))
            self.reveal(self.word('source',[0,-1,0],color=GREEN))
            return
        self.reveal(self.card(self.content['representative'],[0,.8,0],13.4,CYAN,True))
        self.reveal(self.card(self.content['syntax'],[0,-1.15,0],13.4,GREEN,True))
        self.play(Indicate(self.mobjects[-1],color=GREEN),run_time=.6)

    def workflow(self):
        self.reveal(self.word('workflow',[0,2.65,0],color=CYAN,size=50))
        if self.content['status']=='unconfirmed':
            self.reveal(self.card('source',[-4.2,.8,0]))
            self.reveal(self.card('unconfirmed',[4.2,.8,0],color=AMBER))
            self.play(Create(self.arrow([-1.2,.8,0],[1.2,.8,0],AMBER)),run_time=.4)
            return
        self.reveal(self.card('source',[-4.2,1,0]),self.card('detect',[4.2,1,0]))
        self.play(Create(self.arrow([-1.2,1,0],[1.2,1,0])),run_time=.4)
        nodes=[m for m in self.mobjects if m not in self.chrome and m is not self.mobjects[len(self.chrome)]]
        self.play(*[FadeOut(m) for m in nodes],run_time=.3)
        self.reveal(self.card('transform',[-3.6,.5,0],6.5),self.card('preview',[3.6,.5,0],6.5))
        self.reveal(self.card('extract',[0,-1.3,0],13.4))
        self.reveal(self.word('custom',[0,-2.8,0],color=AMBER,size=44))

    def accept(self):
        self.reveal(self.word('accept',[0,2.65,0],color=CYAN,size=50))
        self.reveal(self.card('invoice',[-4.2,1,0]),self.card('credit',[4.2,1,0]))
        self.reveal(self.card('fields',[-4.2,-1,0],color=GREEN))
        self.play(Create(self.arrow([-1.2,-1,0],[1.2,-1,0],GREEN)),run_time=.4)
        self.reveal(self.card('export',[4.2,-1,0],color=GREEN))
        self.reveal(self.word('limits',[0,-2.65,0],color=AMBER,size=44))

    def construct(self):
        self.locale=os.environ['VIDEO_LOCALE']
        self.content=json.loads((ROOT/f'content/{self.page_key}/locales/{self.locale}.json').read_text())
        timing=json.loads(Path(os.environ['VIDEO_TIMING']).read_text())
        self.add(ImageMobject(str(ROOT/'cache/brand/logo_white.png')).set(width=2.1).move_to([-5.9,3.65,0]))
        self.add(Line([-6.9,-3.65,0],[6.9,-3.65,0],color=BORDER))
        chrome=list(self.mobjects)
        self.chrome=chrome
        for segment,plan in zip(self.content['segments'],timing):
            self.next_section(segment['id'])
            start=self.time
            self.wait(.3)
            getattr(self,segment['scene_id'])()
            remaining=plan['frames']/30-(self.time-start)-.3
            if remaining<-.04:
                raise ValueError('Animation exceeds narration timing: '+segment['id'])
            if remaining>0:
                self.wait(round(remaining*30)/30)
            self.play(*[FadeOut(m) for m in self.mobjects if m not in chrome],run_time=.3)
