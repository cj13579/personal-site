# Repository Guidelines

## Project Structure & Module Organization

This repository is a small static personal site. `build.py` is the Python build script that renders Markdown through Pandoc. Source content lives in `src/`: top-level pages such as `index.md`, `projects.md`, and `cv.md` render to `html/*.html`, while posts in `src/blog/` render to `html/blog/`. Pandoc templates are in `templates/main.html` and `templates/post.html`. Static files belong in `assets/` and are copied to `html/assets/`. The `html/` directory is generated output and should be rebuilt after source, template, or asset changes.

## Build, Test, and Development Commands

- `python3 build.py`: rebuilds the site into `html/`, regenerates the blog index, and copies assets.
- `python3 -m http.server 8080 -d html`: serves the generated site locally at `http://localhost:8080`.
- `docker build -t cjb13579/personal-site:latest .`: builds the nginx image from generated static files.
- `docker run --rm -p 8080:80 cjb13579/personal-site:latest`: runs the container locally.

The build requires `python3` and `pandoc`; there are no third-party Python packages.

## Coding Style & Naming Conventions

Keep Python changes compatible with the existing style in `build.py`: 4-space indentation, type hints where useful, `pathlib.Path` for filesystem paths, and small functions with direct responsibilities. Keep Markdown filenames lowercase and URL-friendly. Blog post filenames should start with an ISO date, for example `src/blog/2026-05-26-introducing-family-wishlists.md`.

## Content Guidelines

Blog posts require YAML-style front matter:

```yaml
---
title: My Post Title
date: 2026-04-08 09:30:00
---
```

Use the exact `YYYY-MM-DD HH:MM:SS` date format because `build.py` parses it for reverse chronological sorting. Add images or downloads to `assets/`, then reference them with paths that work after copying to `html/assets/`.

## Testing Guidelines

There is no automated test suite. Validate changes by running `python3 build.py` and checking the generated pages in `html/`. For template or layout edits, serve `html/` locally and review the affected pages and at least one blog post.

## Commit & Pull Request Guidelines

Recent commits use short, imperative messages, often with gitmoji prefixes such as `:memo:` for docs and `:sparkles:` for features. Keep commits focused. Pull requests should describe the source changes, note whether `python3 build.py` was run, link any related issue, and include screenshots for visible site changes.
