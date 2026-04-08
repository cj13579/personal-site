#!/usr/bin/env python3

from __future__ import annotations

import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "src"
HTML_DIR = ROOT / "html"
ASSETS_DIR = ROOT / "assets"
BLOG_DIR = SRC_DIR / "blog"
TEMPLATES_DIR = ROOT / "templates"
TMP_BLOG = Path("/tmp/blog.md")


def run_command(args: list[str]) -> None:
    subprocess.run(args, check=True, cwd=ROOT)


def parse_front_matter(markdown_file: Path) -> dict[str, str]:
    lines = markdown_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("'\"")
    return metadata


def render_main_markdown(markdown_file: Path) -> None:
    print(f"mdfile: {markdown_file.as_posix()}")
    htmlfile = markdown_file.with_suffix(".html").name
    print(f"htmlfile: {htmlfile}")
    run_command(
        [
            "pandoc",
            "--standalone",
            "--template",
            str(TEMPLATES_DIR / "main.html"),
            str(markdown_file),
            "-o",
            str(HTML_DIR / htmlfile),
        ]
    )


def render_blog() -> None:
    blog_index = SRC_DIR / "blog.md"
    shutil.copyfile(blog_index, TMP_BLOG)

    posts = []
    for post_file in BLOG_DIR.glob("*.md"):
        metadata = parse_front_matter(post_file)
        date = metadata.get("date", "")
        parsed_date = datetime.min
        if date:
            parsed_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        posts.append((parsed_date, post_file, metadata))

    for _, post_file, metadata in sorted(posts, key=lambda post: post[0], reverse=True):
        print(f"mdfile: {post_file.as_posix()}")
        htmlfile = Path("blog") / f"{post_file.stem}.html"
        print(f"htmlfile: {htmlfile}")

        title = metadata.get("title", "")
        date = metadata.get("date", "")
        display_date = date.split(" ", 1)[0] if date else ""

        run_command(
            [
                "pandoc",
                "--standalone",
                "--template",
                str(TEMPLATES_DIR / "post.html"),
                str(post_file),
                "-o",
                str(HTML_DIR / htmlfile),
            ]
        )

        with TMP_BLOG.open("a", encoding="utf-8") as handle:
            handle.write(f"- [{display_date} - {title}]({htmlfile})\n")

    run_command(
        [
            "pandoc",
            "--standalone",
            "--template",
            str(TEMPLATES_DIR / "main.html"),
            str(TMP_BLOG),
            "-o",
            str(HTML_DIR / "blog.html"),
        ]
    )


def copy_assets() -> None:
    destination = HTML_DIR / "assets"
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(ASSETS_DIR, destination)


def main() -> int:
    for markdown_file in sorted(SRC_DIR.glob("*.md")):
        if markdown_file.name == "blog.md":
            render_blog()
            continue
        render_main_markdown(markdown_file)
    copy_assets()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Command failed with exit code {exc.returncode}: {exc.cmd}", file=sys.stderr)
        raise SystemExit(exc.returncode)
