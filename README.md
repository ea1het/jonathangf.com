# jonathangf — Open Data

Personal website data as a public JSON endpoint.  
No auth. No rate limits. Build whatever UI you want.

## Endpoint

```
https://YOUR_USERNAME.github.io/YOUR_REPO/data.json
```

## Usage

### JavaScript
```js
const res = await fetch('https://YOUR_USERNAME.github.io/YOUR_REPO/data.json');
const data = await res.json();

console.log(data.pages.home.bio);
console.log(data.pages.home.skills);
console.log(data.pages.about.hobbies);
```

### Python
```python
import requests
data = requests.get('https://YOUR_USERNAME.github.io/YOUR_REPO/data.json').json()
print(data['pages']['home']['skills'])
```

### cURL
```bash
curl https://YOUR_USERNAME.github.io/YOUR_REPO/data.json | jq .
```

## Schema

| Field | Description |
|---|---|
| `site` | Title, URL, description |
| `nav` | Navigation links |
| `pages.home` | Headline, bio, skills, hero image |
| `pages.about` | Sections, hobbies, location, ham radio |
| `blog.posts` | Blog posts array |
| `meta` | Generation date and source |

## Files

```
/
├── index.html   ← API documentation landing page
├── data.json    ← The actual data
└── README.md    ← This file
```

## License

Data is free to use. Attribution appreciated but not required.  
© [Jonathan González](https://jonathangf.com)
