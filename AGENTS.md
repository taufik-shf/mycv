# AGENTS.md

Guidance for agentic coding agents working in this repository.

## Project Overview

A YAML-driven CV builder. Content lives in `cv.yaml`, is rendered via a Jinja2 template into `index.html`, then exported to PDF with WeasyPrint. Managed with `uv` package manager.

## Repository Structure

```
mycv/
├── cv.yaml              # All CV content (data source of truth)
├── templates/
│   ├── index.html       # Jinja2 HTML template
│   └── style.css        # Styles + @media print + @page rules (inlined into HTML via Jinja2 include)
├── build.py             # Renders cv.yaml + template → index.html
├── assets/
│   └── profile.jpg      # Profile photo
├── Makefile             # Build commands
├── pyproject.toml       # uv project config with dependencies
├── uv.lock              # uv lockfile
├── .venv/               # Python venv (gitignored)
├── index.html           # Generated HTML output (gitignored, self-contained)
├── cv.pdf               # Generated PDF output (gitignored)
└── AGENTS.md            # This file
```

## Commands

- `make build` - Render cv.yaml + Jinja2 template → index.html
- `make pdf` - Build HTML then export to PDF using WeasyPrint
- `make serve` - Start local HTTP server on port 8080 for browser preview
- `make clean` - Remove generated index.html and cv.pdf

## Key Technologies

- YAML for CV data
- Jinja2 for HTML templating
- HTML5 + CSS3 (no frameworks)
- WeasyPrint (Python) for PDF generation
- `uv` for Python package management
- `@page` and `@media print` rules control PDF layout

## Editing Content

Edit `cv.yaml`. All personal info, experience, education, projects, skills, etc. are defined there. Never edit the generated `index.html` directly.

## Editing Template

Edit `templates/index.html` (Jinja2 syntax). Use `{{ variable }}` and `{% for item in list %}` patterns matching the structure in `cv.yaml`.

## Editing Styles

Edit `templates/style.css`. The CSS is inlined into the HTML output via `{% include 'style.css' %}` in the template. Screen and print styles are in the same file. The `@page` block at the top controls PDF page size and margins. The `@media screen` block handles web view styling. The `@media print` block handles print-specific overrides. The generated `index.html` is fully self-contained (no external CSS file).

## Style Guidelines

- Use 2-space indentation in HTML, CSS, and YAML
- Keep HTML template semantic (sections, h2, h3, ul/li, etc.)
- Use CSS custom properties in `:root` for colors and fonts
- Use `break-inside: avoid` on `.entry` and `.section` for clean page breaks
- Do not modify `.venv/` contents

## PDF Export Notes

- `make pdf` runs `build.py` first (generates index.html), then WeasyPrint
- Profile photo uses a relative path (`assets/profile.jpg`)
- All Python commands run via `uv run` (no manual venv activation needed)
- WeasyPrint runs from the local `.venv` managed by uv
