# personal-site

This repository contains the source for Christopher Blake's personal website.

The site is built from Markdown files using `pandoc` and a small Python build script. Top-level pages such as `index.md`, `projects.md`, and `cv.md` are rendered into static HTML, and blog posts in `blog/` are rendered into `html/blog/`.

## Repository layout

- `build.py` builds the static site into `html/`
- `templates/` contains the Pandoc templates for main pages and blog posts
- `assets/` contains images and other static assets copied into `html/assets/`
- `blog/` contains blog post source files with front matter
- `html/` contains the generated site output
- `_old/` contains older site content and legacy configuration

## Requirements

You will need:

- `python3`
- `pandoc`

The build script does not require any third-party Python packages.

## Building the site

Run:

```bash
python3 build.py
```

This will:

- render top-level Markdown pages into `html/`
- render blog posts into `html/blog/`
- rebuild the blog index page from `blog.md`
- sort blog links by the front matter `date` field in descending order
- copy `assets/` into `html/assets/`

## Writing content

### Pages

Edit the top-level Markdown files in the repository root:

- `index.md`
- `projects.md`
- `cv.md`
- `sql2rest.md`

### Blog posts

Add new posts as Markdown files in `blog/` with front matter at the top. For example:

```yaml
---
title: My Post Title
date: 2026-04-08 09:30:00
---
```

The `date` field is used to order blog posts in descending order on the blog index. Link text on the blog page shows the date portion only, in `YYYY-MM-DD` format.

## Publishing

The generated site lives in `html/`. If you are publishing with GitHub Pages or another static host, publish the contents of that directory using your preferred deployment process.
