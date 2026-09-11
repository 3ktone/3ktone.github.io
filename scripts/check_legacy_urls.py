#!/usr/bin/env python3
"""Verify that every historical public URL still resolves in a Hugo build."""

from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


def candidates(root: Path, url: str) -> list[Path]:
    path = unquote(urlsplit(url).path)
    target = (root / path.lstrip("/")).resolve()

    # Reject encoded traversal or any path that escapes the generated site.
    try:
        target.relative_to(root)
    except ValueError:
        return []

    if Path(path).suffix:
        return [target]
    return [target / "index.html"]


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: check_legacy_urls.py BUILD_DIR URL_LIST", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    urls = [
        line.strip()
        for line in Path(sys.argv[2]).read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
    missing = [url for url in urls if not any(path.is_file() for path in candidates(root, url))]

    if missing:
        print(f"Missing {len(missing)} historical URL(s):", file=sys.stderr)
        for url in missing:
            print(f"  {url}", file=sys.stderr)
        return 1

    print(f"Verified {len(urls)} historical URLs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
