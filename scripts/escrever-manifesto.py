#!/usr/bin/env python3
"""Rewrite exports/manifest.json from the current .figcraft and vitrine PNGs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "KalangoOS-DesignSystem.figcraft"
VITRINE = ROOT / "exports" / "vitrine"
OUT = ROOT / "exports" / "manifest.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    pages: list[dict] = []
    if VITRINE.is_dir():
        for p in sorted(VITRINE.iterdir()):
            if p.is_dir():
                pages.append(
                    {
                        "dir": p.name,
                        "files": sorted(x.name for x in p.glob("*.png")),
                    }
                )
    manifest = {
        "figcraft": FIG.name,
        "sha256": sha256(FIG) if FIG.is_file() else None,
        "bytes": FIG.stat().st_size if FIG.is_file() else None,
        "vitrine": pages,
        "note": "Showcase PNGs; regenerate with ./scripts/exportar-telas.sh",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
