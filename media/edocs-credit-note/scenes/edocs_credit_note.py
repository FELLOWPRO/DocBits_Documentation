"""Eight causal diagrams for electronic credit note classification.

These are teaching diagrams, not screenshots or simulated product controls.
No customer data or organization changes are involved.
"""

import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from manim import (
    Scene,
    Text,
    VGroup,
    RoundedRectangle,
    Arrow,
    Line,
    ImageMobject,
    FadeIn,
    FadeOut,
    Create,
    Indicate,
    config,
)
from brand import BG, SURFACE, BORDER, INK, MUTED, CYAN, GREEN, AMBER, ERROR
from scenes.common import check_glyphs, font

config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 30
config.renderer = "cairo"
config.background_color = BG


class Edocs_credit_note(Scene):
    def text(self, value, width=13.6, color=INK, size=46):
        check_glyphs(value, self.locale)

        def render(text):
            return Text(text, font=font(self.locale), font_size=size, color=color)

        item = render(value)
        if item.width <= width:
            return item
        words = list(value) if self.locale == "zh" else value.split()
        separator = "" if self.locale == "zh" else " "
        lines, line = [], []
        for word in words:
            proposed = separator.join(line + [word])
            if line and render(proposed).width > width:
                lines.append(separator.join(line))
                line = [word]
            else:
                line.append(word)
        lines.append(separator.join(line))
        item = render("\n".join(lines))
        # Some languages use a single long word where English uses two words.
        # Keep it intact and allow a small size adjustment, with a readable floor.
        scale = min(1, width / item.width, 1.75 / item.height)
        if scale < 0.78:
            raise ValueError(f"Label exceeds teaching panel: {self.locale}: {value}")
        item.scale(scale)
        return item

    def word(self, key, point, width=13.6, color=INK, size=46):
        return self.text(self.content["labels"][key], width, color, size).move_to(point)

    def card(self, value, point, width=5.7, color=CYAN, literal=False):
        title = self.text(
            value if literal else self.content["labels"][value], width - 0.6
        )
        box = RoundedRectangle(
            width=width,
            height=max(1.35, title.height + 0.5),
            corner_radius=0.15,
            stroke_color=color,
            stroke_width=3,
            fill_color=SURFACE,
            fill_opacity=1,
        )
        return VGroup(box, title).move_to(point)

    def arrow(self, start, end, color=CYAN):
        return Arrow(
            start,
            end,
            buff=0.1,
            color=color,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15,
        )

    def reveal(self, *objects):
        self.play(*[FadeIn(item) for item in objects], run_time=0.4)

    def heading(self, key):
        self.reveal(self.word(key, [0, 2.65, 0], color=CYAN, size=52))

    def symptom(self):
        self.heading("xml")
        source = self.card("TypeCode 381", [-4.3, 0.4, 0], 5.1, literal=True)
        result = self.card("invoice", [4.3, 0.4, 0], 5.1, ERROR)
        self.reveal(source)
        self.play(
            Create(self.arrow([-1.65, 0.4, 0], [1.65, 0.4, 0], ERROR)), run_time=0.4
        )
        self.reveal(result, self.word("stored", [4.3, -1.2, 0], 5.5, MUTED))
        self.play(
            Indicate(source, color=GREEN), Indicate(result, color=ERROR), run_time=0.6
        )

    def codes(self):
        self.heading("credit_codes")
        self.reveal(self.card("381  /  261", [0, 1.1, 0], 7.8, GREEN, True))
        self.reveal(
            self.card("383", [-4.1, -0.7, 0], 5.7, AMBER, True),
            self.card("384", [4.1, -0.7, 0], 5.7, AMBER, True),
        )
        self.reveal(
            self.word("debit", [-4.1, -2.2, 0], 6.8),
            self.word("corrected", [4.1, -2.2, 0], 6.8),
        )

    def source(self):
        self.heading("source")
        default = self.card("default", [-4.2, 1, 0], 5.8, MUTED)
        custom = self.card("custom", [-4.2, -1, 0], 5.8, GREEN)
        active = self.card("active", [4.2, -1, 0], 5.8, GREEN)
        self.reveal(default, custom)
        self.play(Create(self.arrow([-1.2, -1, 0], [1.2, -1, 0], GREEN)), run_time=0.4)
        self.reveal(active)
        self.play(Indicate(custom, color=GREEN), run_time=0.6)
        self.reveal(self.text("FACTURX", color=CYAN).move_to([4.2, 1, 0]))

    def transform(self):
        self.heading("transform")
        self.reveal(self.text("INVOICE_TYPE", color=MUTED).move_to([0, 1.3, 0]))
        bad = self.card("invoice", [-4.2, -0.2, 0], 5.8, ERROR)
        good = self.card("credit", [4.2, -0.2, 0], 5.8, GREEN)
        self.reveal(bad, self.word("constant", [-4.2, -1.7, 0], 6.6, AMBER))
        self.play(Create(self.arrow([-1.2, -0.2, 0], [1.2, -0.2, 0])), run_time=0.4)
        self.reveal(good, self.word("compare", [4.2, -1.7, 0], 6.6, GREEN))

    def paths(self):
        self.heading("paths")
        self.reveal(
            self.card("transformed", [-4.2, 1, 0], 5.8),
            self.card("invoice_type", [4.2, 1, 0], 5.8, literal=True),
        )
        self.play(Create(self.arrow([-1.2, 1, 0], [1.2, 1, 0])), run_time=0.4)
        self.reveal(
            self.card("scripts", [-4.2, -1.3, 0], 5.8, AMBER),
            self.card("stored", [4.2, -1.3, 0], 5.8, GREEN),
        )
        self.play(
            Create(self.arrow([3.8, 0.1, 0], [-3.8, -0.4, 0])),
            Create(self.arrow([-1.2, -1.3, 0], [1.2, -1.3, 0])),
            run_time=0.4,
        )

    def activate(self):
        self.heading("draft")
        self.reveal(
            self.card("save", [-4.2, 1, 0], 5.8), self.card("saved", [4.2, 1, 0], 5.8)
        )
        self.play(Create(self.arrow([-1.2, 1, 0], [1.2, 1, 0])), run_time=0.4)
        self.reveal(
            self.card("test", [-4.2, -1.3, 0], 5.8, GREEN),
            self.card("activate", [4.2, -1.3, 0], 5.8, GREEN),
        )
        self.play(
            Create(self.arrow([-1.2, -1.3, 0], [1.2, -1.3, 0], GREEN)), run_time=0.4
        )
        self.reveal(self.word("check", [4.2, -2.65, 0], 6.8, GREEN))

    def safety(self):
        self.heading("safety")
        self.reveal(self.card("preserve", [0, 1, 0], 13.4, GREEN))
        self.reveal(self.word("history", [0, -0.5, 0], 13.4, AMBER))
        self.reveal(
            self.card("approvals", [-4.7, -2, 0], 4.3, AMBER),
            self.card("exports", [0, -2, 0], 4.3, AMBER),
            self.card("edits", [4.7, -2, 0], 4.3, AMBER),
        )

    def sign(self):
        self.heading("sign")
        self.reveal(
            self.word("enabled", [0, 1.3, 0], 13.4, GREEN),
            self.word("configurable", [0, 0.2, 0], 13.4, AMBER),
        )
        self.reveal(
            self.card("credit", [-4.2, -1.5, 0], 5.8, GREEN),
            self.card("Infor ERP / SAP", [4.2, -1.5, 0], 5.8, GREEN, True),
        )
        self.play(
            Create(self.arrow([-1.2, -1.5, 0], [1.2, -1.5, 0], GREEN)), run_time=0.4
        )

    def construct(self):
        self.locale = os.environ["VIDEO_LOCALE"]
        self.content = json.loads(
            (ROOT / f"content/edocs_credit_note/locales/{self.locale}.json").read_text()
        )
        timing = json.loads(Path(os.environ["VIDEO_TIMING"]).read_text())
        self.add(
            ImageMobject(str(ROOT / "cache/brand/logo_white.png"))
            .set(width=2.1)
            .move_to([-5.9, 3.65, 0])
        )
        self.add(Line([-6.9, -3.65, 0], [6.9, -3.65, 0], color=BORDER))
        chrome = list(self.mobjects)
        for segment, plan in zip(self.content["segments"], timing):
            self.next_section(segment["id"])
            start = self.time
            self.wait(0.3)
            getattr(self, segment["scene_id"])()
            remaining = plan["frames"] / 30 - (self.time - start) - 0.3
            if remaining < -0.04:
                raise ValueError("Animation exceeds narration timing: " + segment["id"])
            if remaining > 0:
                self.wait(round(remaining * 30) / 30)
            self.play(
                *[FadeOut(m) for m in self.mobjects if m not in chrome], run_time=0.3
            )
