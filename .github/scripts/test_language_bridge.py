"""Tests for language_bridge.py: the checks that keep a broken page from
reaching a GitBook import, and the guarantees of the sync itself."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import language_bridge as lb  # noqa: E402

SUMMARY = """# Table of contents

## Group

* [Home](README.md)
  * [Page A](a/page-a.md)
  * [Page B](b.md)
"""


def make_branch(root: Path, pages: dict[str, str], summary: str = SUMMARY, assets: dict[str, bytes] | None = None) -> Path:
    readme = root / "readme"
    (readme / ".gitbook" / "assets").mkdir(parents=True)
    (readme / "SUMMARY.md").write_text(summary, encoding="utf-8")
    for rel, text in pages.items():
        (readme / rel).parent.mkdir(parents=True, exist_ok=True)
        (readme / rel).write_text(text, encoding="utf-8")
    for name, data in (assets or {}).items():
        (readme / ".gitbook" / "assets" / name).write_bytes(data)
    return readme


GOOD = {"README.md": "# Home\n", "a/page-a.md": "# A\n", "b.md": "---\ndescription: hello world\n---\n\n# B\n"}


def run(tmp: Path, pages: dict[str, str], **kw):
    readme = make_branch(tmp / "src", pages, **kw)
    dest = tmp / "dest" / "deutsch"
    dest.mkdir(parents=True)
    return lb.plan_sync(readme, dest), dest


def test_parse_summary_keeps_order_and_indent():
    nav = lb.parse_summary(SUMMARY)
    assert nav == [(0, "Home", "README.md"), (2, "Page A", "a/page-a.md"), (2, "Page B", "b.md")]


def test_good_branch_has_no_errors(tmp_path):
    (rep, plan), _ = run(tmp_path, GOOD)
    assert rep.errors == []
    assert "SUMMARY.md" in rep.pages and len(rep.pages) == 4


def test_navigation_entry_without_file_is_an_error(tmp_path):
    pages = dict(GOOD)
    del pages["b.md"]
    (rep, _), _ = run(tmp_path, pages)
    assert any("navigation entry without file: b.md" in e for e in rep.errors)


def test_front_matter_with_embed_block_is_rejected(tmp_path):
    # the Dutch Power BI page had its {% embed %} inside the front matter
    bad = "---\ndescription: Hoe PowerBI te configureren\n\n{% embed url=\"https://x\" %}\n{% endembed %}\n\n---\n\n# T\n"
    assert lb.front_matter_errors(bad)
    (rep, _), _ = run(tmp_path, {**GOOD, "b.md": bad})
    assert any("front matter" in e for e in rep.errors)


def test_unquoted_colon_in_description_is_invalid_yaml():
    assert lb.front_matter_errors("---\ndescription: hello: world\n---\n\n# T\n")
    assert lb.front_matter_errors('---\ndescription: "hello: world"\n---\n\n# T\n') == []


def test_unclosed_front_matter_is_rejected():
    assert lb.front_matter_errors("---\ndescription: x\n\n# T\n") == ["front matter is not closed"]


def test_page_without_front_matter_is_fine():
    assert lb.front_matter_errors("# Title\n\ntext\n") == []


def test_unbalanced_hint_is_rejected():
    assert lb.tag_errors('{% hint style="info" %}\ntext\n') != []
    assert lb.tag_errors('{% hint style="info" %}\ntext\n{% endhint %}\n') == []


def test_file_block_to_missing_file_blocks_the_sync(tmp_path):
    # the XRechnung example page referenced an attachment that exists nowhere
    page = '# A\n\n{% file src="../.gitbook/assets/missing.xml" %}\n'
    (rep, _), _ = run(tmp_path, {**GOOD, "a/page-a.md": page})
    assert any("missing file" in e for e in rep.errors)


def test_file_block_to_existing_asset_is_copied(tmp_path):
    page = '# A\n\n{% file src="../.gitbook/assets/example.xml" %}\n'
    (rep, plan), dest = run(tmp_path, {**GOOD, "a/page-a.md": page}, assets={"example.xml": b"<x/>"})
    assert rep.errors == []
    assert rep.assets == ["example.xml"]
    assert dest / ".gitbook" / "assets" / "example.xml" in plan


def test_image_names_with_parentheses_and_spaces(tmp_path):
    page = '# A\n\n![](<../.gitbook/assets/image (83).png>)\n\n<img src="../.gitbook/assets/Picture 1.png" alt="">\n'
    (rep, _), _ = run(tmp_path, {**GOOD, "a/page-a.md": page}, assets={"image (83).png": b"1", "Picture 1.png": b"2"})
    assert sorted(rep.assets) == ["Picture 1.png", "image (83).png"]
    assert rep.warnings == []


def test_missing_image_is_only_a_warning(tmp_path):
    (rep, _), _ = run(tmp_path, {**GOOD, "a/page-a.md": "# A\n\n![](../.gitbook/assets/nowhere.png)\n"})
    assert rep.errors == []
    assert len(rep.warnings) == 1


def test_stub_pages_are_counted(tmp_path):
    (rep, _), _ = run(tmp_path, {**GOOD, "b.md": "# DE - TRANSLATED\n\nTranslated to Deutsch\n"})
    assert rep.stubs == 1


def test_sync_copies_and_is_idempotent(tmp_path):
    src = make_branch(tmp_path / "src", GOOD)
    dest = tmp_path / "dest" / "deutsch"
    rep, plan = lb.plan_sync(src, dest)
    lb.apply_plan(plan)
    assert (dest / "a" / "page-a.md").read_text() == "# A\n"
    rep2, plan2 = lb.plan_sync(src, dest)
    assert rep2.changed == 0 and plan2 == {}


def test_sync_never_deletes_other_files(tmp_path):
    src = make_branch(tmp_path / "src", GOOD)
    dest = tmp_path / "dest" / "deutsch"
    (dest / "old").mkdir(parents=True)
    (dest / "old" / "kept.md").write_text("old page", encoding="utf-8")
    lb.apply_plan(lb.plan_sync(src, dest)[1])
    assert (dest / "old" / "kept.md").read_text() == "old page"


def test_invalid_branch_writes_nothing(tmp_path):
    src = tmp_path / "src"
    make_branch(src, {**GOOD, "b.md": "---\ndescription: x\n\n# T\n"})
    dest_root = tmp_path / "dest"
    (dest_root / "deutsch").mkdir(parents=True)
    rc = lb.main(["sync", "--lang", "de", "--source", str(src), "--dest", str(dest_root)])
    assert rc == 1
    assert list((dest_root / "deutsch").iterdir()) == []


def test_main_ok_and_unknown_language(tmp_path, capsys):
    src = tmp_path / "src"
    make_branch(src, GOOD)
    dest_root = tmp_path / "dest"
    assert lb.main(["sync", "--lang", "de", "--source", str(src), "--dest", str(dest_root)]) == 0
    assert "RESULT lang=de status=ok pages=4" in capsys.readouterr().out
    assert lb.main(["sync", "--lang", "xx", "--source", str(src), "--dest", str(dest_root)]) == 2


def test_dry_run_writes_nothing(tmp_path):
    src = tmp_path / "src"
    make_branch(src, GOOD)
    dest_root = tmp_path / "dest"
    assert lb.main(["sync", "--lang", "es", "--source", str(src), "--dest", str(dest_root), "--dry-run"]) == 0
    assert not (dest_root / "espanol").exists()


def test_every_language_has_its_own_folder():
    assert len(set(lb.LANGS.values())) == len(lb.LANGS) == 7
    assert pytest is not None


# --- path traversal / symlink hardening -------------------------------------


@pytest.mark.parametrize("bad", ["../../escape.md", "/etc/passwd.md", "a/../../x.md"])
def test_unsafe_navigation_path_is_an_error(tmp_path, bad):
    summary = SUMMARY + f"  * [Evil]({bad})\n"
    (rep, plan), dest = run(tmp_path, GOOD, summary=summary)
    assert any("unsafe navigation path" in e for e in rep.errors)
    assert all(str(d).startswith(str(dest)) for d in plan)


def test_symlinked_page_is_rejected(tmp_path):
    secret = tmp_path / "secret.md"
    secret.write_text("# runner secret\n")
    readme = make_branch(tmp_path / "src", {k: v for k, v in GOOD.items() if k != "b.md"})
    (readme / "b.md").symlink_to(secret)
    dest = tmp_path / "dest" / "deutsch"
    dest.mkdir(parents=True)
    rep, plan = lb.plan_sync(readme, dest)
    assert any("symlink" in e for e in rep.errors)
    assert dest / "b.md" not in plan


def test_symlinked_directory_in_page_path_is_rejected(tmp_path):
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "page-a.md").write_text("# leaked\n")
    readme = make_branch(tmp_path / "src", {k: v for k, v in GOOD.items() if k != "a/page-a.md"})
    (readme / "a").symlink_to(outside, target_is_directory=True)
    dest = tmp_path / "dest" / "deutsch"
    dest.mkdir(parents=True)
    rep, _ = lb.plan_sync(readme, dest)
    assert any("symlink" in e for e in rep.errors)


def test_symlinked_asset_is_not_copied(tmp_path):
    secret = tmp_path / "secret.png"
    secret.write_bytes(b"secret")
    page = "# A\n\n![](../.gitbook/assets/leak.png)\n"
    readme = make_branch(tmp_path / "src", {**GOOD, "a/page-a.md": page})
    (readme / ".gitbook" / "assets" / "leak.png").symlink_to(secret)
    dest = tmp_path / "dest" / "deutsch"
    dest.mkdir(parents=True)
    rep, plan = lb.plan_sync(readme, dest)
    assert rep.assets == [] and not any(d.name == "leak.png" for d in plan)


def test_dotdot_in_image_reference_does_not_escape_assets(tmp_path):
    page = "# A\n\n![](../.gitbook/assets/../../b.md)\n"
    (rep, plan), _ = run(tmp_path, {**GOOD, "a/page-a.md": page})
    assert rep.assets == []
    assert not any(d.name == "b.md" and ".gitbook" in d.parts for d in plan)


def test_symlinked_destination_is_rejected(tmp_path):
    readme = make_branch(tmp_path / "src", GOOD)
    target = tmp_path / "elsewhere"
    target.mkdir()
    dest = tmp_path / "dest" / "deutsch"
    dest.mkdir(parents=True)
    (dest / "b.md").symlink_to(target / "b.md")
    rep, _ = lb.plan_sync(readme, dest)
    assert any("destination is a symlink" in e for e in rep.errors)


def test_symlinked_summary_is_rejected(tmp_path):
    readme = make_branch(tmp_path / "src", GOOD)
    real = tmp_path / "real-summary.md"
    real.write_text(SUMMARY)
    (readme / "SUMMARY.md").unlink()
    (readme / "SUMMARY.md").symlink_to(real)
    dest = tmp_path / "dest" / "deutsch"
    dest.mkdir(parents=True)
    rep, _ = lb.plan_sync(readme, dest)
    assert rep.errors
