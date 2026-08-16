#!/usr/bin/env python3
"""Regenerate files/manifest.json from the contents of the files/ folder.

Run this after adding, removing or renaming files inside files/:

    python3 generate-manifest.py

It writes a plain JSON array of {"name": ..., "size": ...} objects that
files/index.html reads to render the file explorer. No dependencies beyond
the Python 3 standard library.
"""

import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(ROOT, "files")
MANIFEST = os.path.join(FILES_DIR, "manifest.json")

SKIP = {"manifest.json", ".DS_Store"}


def main():
    if not os.path.isdir(FILES_DIR):
        raise SystemExit(f"No existe la carpeta: {FILES_DIR}")

    entries = []
    for name in sorted(os.listdir(FILES_DIR), key=str.lower):
        if name in SKIP or name.startswith("."):
            continue
        path = os.path.join(FILES_DIR, name)
        if os.path.isfile(path):
            entries.append({"name": name, "size": os.path.getsize(path)})

    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
        f.write("\n")

    plural = "" if len(entries) == 1 else "s"
    print(f"OK: {len(entries)} fichero{plural} escrito{plural} en {os.path.relpath(MANIFEST, ROOT)}")


if __name__ == "__main__":
    main()
