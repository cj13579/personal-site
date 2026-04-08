# personal-site

This repository contains the source for Christopher Blake's personal website.

The site is built from Markdown files using `pandoc` and a small Python build script. Top-level pages such as `index.md`, `projects.md`, and `cv.md` are read from `src/` and rendered into static HTML, and blog posts in `src/blog/` are rendered into `html/blog/`.

## Repository layout

- `build.py` builds the static site into `html/`
- `src/` contains the Markdown source for pages and blog posts
- `templates/` contains the Pandoc templates for main pages and blog posts
- `assets/` contains images and other static assets copied into `html/assets/`
- `html/` contains the generated site output

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
- rebuild the blog index page from `src/blog.md`
- sort blog links by the front matter `date` field in descending order
- copy `assets/` into `html/assets/`

## Writing content

### Pages

Edit the top-level Markdown files in `src/`:

- `src/index.md`
- `src/projects.md`
- `src/cv.md`
- `src/sql2rest.md`

### Blog posts

Add new posts as Markdown files in `src/blog/` with front matter at the top. For example:

```yaml
---
title: My Post Title
date: 2026-04-08 09:30:00
---
```

The `date` field is used to order blog posts in descending order on the blog index. Link text on the blog page shows the date portion only, in `YYYY-MM-DD` format.

## Publishing

The generated site lives in `html/`.

## Docker

The generated site can be packaged into a minimal container that serves the static files with `nginx`.

Build the image with:

```bash
docker build -t cjb13579/personal-site:latest .
```

Run it locally with:

```bash
docker run --rm -p 8080:80 cjb13579/personal-site:latest
```

Then open `http://localhost:8080`.

The image is published to Docker Hub as `cjb13579/personal-site:latest`.
