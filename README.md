# jonathangf.com

Personal website. `index.html` is a static template that fetches `data.json`
at runtime and renders every section from it — `data.json` is the single
source of truth for the site's content, not a separate document.

## How it works

```text
index.html  →  fetch('data.json')  →  render() populates the page
```

Opening `index.html` directly from disk (`file://`) won't work: browsers
block that fetch for local files. Serve the folder over HTTP instead, e.g.:

```bash
python3 -m http.server
```

then open `http://localhost:8000/`.

## Editing content

To change anything on the page — copy, experience entries, skills,
credentials, contact details — edit `data.json`. No HTML changes needed.

## Schema

| Field | Description |
| --- | --- |
| `site` | Title, tagline, brand wordmark, meta description |
| `labels` | Section labels and small UI copy (`// about me`, "Earlier career", etc.) |
| `page_nav` | Header navigation links |
| `pages.home.hero` | Hero tag + heading |
| `pages.home.bio` | About-section body copy (paragraphs separated by a blank line) |
| `pages.home.about.location` | Location line under the bio |
| `pages.home.skill_groups` | Expertise tags, grouped under category titles |
| `experience` | Timeline entries (role, company, period, context, highlights) |
| `earlier_career` | Condensed list of earlier roles |
| `credentials` | Certifications, education, insights, languages |
| `contact` | Contact heading, paragraph, email and LinkedIn (with button labels) |
| `footer` | Footer text and links |

## Files

```text
/
├── index.html   ← template + renderer (reads data.json)
├── data.json    ← all site content
└── README.md    ← this file
```

## License

© [Jonathan González](https://jonathangf.com)
