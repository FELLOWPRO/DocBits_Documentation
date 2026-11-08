#!/usr/bin/env python3
"""Rebuild of the audit checker (identical rules) for re-verification."""
import argparse
import os
import re
import sys

NUM = re.compile(r"\d[\d.,]*")
HEAD = re.compile(r"^(#{1,6}) (.*)$")
IMG = re.compile(r"<img[^>]*src=\"([^\"]+)\"")
MDLINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)")
CODE = re.compile(r"`([^`]+)`")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def headings(text):
    return [HEAD.match(l).group(2).strip() for l in text.splitlines() if HEAD.match(l)]


def rows(text):
    return [l for l in text.splitlines() if l.strip().startswith("|")]


def figures(text):
    return text.count("<figure")


def imgs(text):
    return IMG.findall(text)


def codes(text):
    return [c.strip() for c in CODE.findall(text) if len(c.strip()) > 2]


def digit_tokens(text):
    out = []
    for m in NUM.findall(text):
        digits = re.sub(r"\D", "", m)
        if digits:
            out.append(digits)
    return out


def arrow_elements(text):
    els = []
    for line in text.splitlines():
        if "\u2192" not in line and "->" not in line and "\u203a" not in line:
            continue
        parts = re.split(r"\s*(?:\u2192|->|\u203a)\s*", line)
        for p in parts:
            p = p.strip().strip("*_`|")
            p = p.split("**")[0].strip()
            if not p:
                continue
            els.append(p)
    return els


def link_targets(text):
    targets = []
    for t in MDLINK.findall(text):
        if t.startswith(("http://", "https://", "mailto:", "#")):
            continue
        targets.append(t.split("#")[0])
    for s in IMG.findall(text):
        if s.startswith(("http://", "https://")):
            continue
        targets.append(s)
    return [t for t in targets if t]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--dst", required=True)
    ap.add_argument("--root", required=True)
    ap.add_argument("--lang", default="")
    args = ap.parse_args()

    src, dst = read(args.src), read(args.dst)
    problems, notes = [], []

    h_src, h_dst = headings(src), headings(dst)
    if len(h_src) != len(h_dst):
        problems.append("heading count %d != %d" % (len(h_dst), len(h_src)))

    r_src, r_dst = rows(src), rows(dst)
    if len(r_src) != len(r_dst):
        problems.append("table-row count %d != %d" % (len(r_dst), len(r_src)))

    if figures(src) != figures(dst):
        problems.append("figure count %d != %d" % (figures(dst), figures(src)))

    i_src, i_dst = imgs(src), imgs(dst)
    if len(i_src) != len(i_dst):
        problems.append("image count %d != %d" % (len(i_dst), len(i_src)))
    dst_dir = os.path.dirname(os.path.abspath(args.dst))
    for a, b in zip(i_src, i_dst):
        sa, sb = os.path.basename(a), os.path.basename(b)
        if sa != sb and args.lang and args.lang not in sb:
            problems.append("image %s is not a %s variant of %s" % (sb, args.lang, sa))
        target = os.path.normpath(os.path.join(dst_dir, b)) if not b.startswith("http") else None
        if target and not os.path.exists(target):
            problems.append("missing image file: " + b)

    c_src = set(codes(src))
    missing_codes = sorted(c for c in c_src if c not in dst)
    if missing_codes:
        problems.append("%d code span(s) from src missing in dst" % len(missing_codes))
        for c in missing_codes[:10]:
            notes.append("  missing code span: %r" % (c,))

    from collections import Counter
    cn_src, cn_dst = Counter(digit_tokens(src)), Counter(digit_tokens(dst))
    for tok, n in cn_src.items():
        if cn_dst[tok] < n and len(tok) > 1:
            notes.append("  number %s appears %dx, src %dx" % (tok, cn_dst[tok], n))
    tot_src, tot_dst = sum(cn_src.values()), sum(cn_dst.values())
    if abs(tot_src - tot_dst) > max(6, tot_src * 0.1):
        problems.append("numeric token count %d vs src %d" % (tot_dst, tot_src))

    src_els = set(arrow_elements(src))
    bad_paths = [el for el in arrow_elements(dst) if el not in src_els]
    if bad_paths:
        problems.append("%d UI path element(s) not verbatim from src" % len(bad_paths))
        for e in bad_paths[:10]:
            notes.append("  not verbatim: %r" % (e,))

    broken = []
    for t in link_targets(dst):
        p = t if not t.startswith("/") else t.lstrip("/")
        full = os.path.normpath(os.path.join(dst_dir, p))
        if not (os.path.exists(full) or os.path.exists(full + ".md")):
            idx = os.path.join(full, "README.md")
            if not os.path.exists(idx) and not os.path.isdir(full):
                broken.append(t)
    if broken:
        problems.append("%d broken internal link(s)" % len(broken))
        for b in broken[:12]:
            notes.append("  broken: " + b)

    slugs = set(re.findall(r"<a id=\"([^\"]+)\"", dst))
    used = set(re.findall(r"\]\(\./#([^)\s]+)\)", dst)) | set(re.findall(r"\]\(#([^)\s]+)\)", dst))

    def slugify(h):
        h = re.sub(r"<[^>]+>", "", h)
        h = h.lower()
        h = re.sub(r"[^\w\s-]", "", h)
        return re.sub(r"[\s_]+", "-", h).strip("-")

    dst_slugs = {slugify(h) for h in headings(dst)}
    for u in sorted(used):
        if u not in slugs and u not in dst_slugs:
            problems.append("anchor #%s has no target in dst" % u)

    print("src: %s (%d lines)" % (args.src, len(src.splitlines())))
    print("dst: %s (%d lines)" % (args.dst, len(dst.splitlines())))
    print("headings %d/%d rows %d/%d figures %d/%d imgs %d/%d" % (
        len(h_dst), len(h_src), len(r_dst), len(r_src),
        figures(dst), figures(src), len(i_dst), len(i_src)))
    if notes:
        print("notes:")
        for n in notes:
            print(n)
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print(" - " + p)
        return 1
    print("OK: no blocking findings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
