from __future__ import annotations

import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = 18
MANUAL = set()

def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()

def main() -> int:
    errors = []
    manifest = json.loads((ROOT / "manifests" / "catalog.json").read_text(encoding="utf-8"))
    if len(manifest) != EXPECTED:
        errors.append(f"catalog count: {len(manifest)}")
    for host in ("common", "chatgpt-codex", "claude-code", "opencode"):
        root = ROOT / "skills" / host
        skills = [item for item in root.iterdir() if item.is_dir() and (item / "SKILL.md").is_file()]
        if len(skills) != EXPECTED:
            errors.append(f"{host} skill count: {len(skills)}")
        for skill in skills:
            text = (skill / "SKILL.md").read_text(encoding="utf-8")
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
            if not match or not re.search(rf"(?m)^name:\s*['\"]?{re.escape(skill.name)}['\"]?\s*$", match.group(1)):
                errors.append(f"frontmatter mismatch: {host}/{skill.name}")
            if host == "chatgpt-codex" and not (skill / "agents" / "openai.yaml").is_file():
                errors.append(f"missing OpenAI sidecar: {skill.name}")
    forbidden = re.compile(r"curl[^\n]*\|\s*(?:ba)?sh|wget[^\n]*\|\s*(?:ba)?sh", re.I)
    personal = re.compile(r"C:[/\\]Users[/\\]Gaming", re.I)
    for item in ROOT.rglob("*"):
        if not item.is_file() or item.suffix.lower() not in {".md", ".txt", ".py", ".yaml", ".yml", ".json"}:
            continue
        text = item.read_text(encoding="utf-8", errors="replace")
        if forbidden.search(text) and "Never pipe" not in text:
            errors.append(f"active pipe-to-shell: {item.relative_to(ROOT)}")
        if personal.search(text):
            errors.append(f"personal or machine data: {item.relative_to(ROOT)}")
    for package in (ROOT / "packages").rglob("*.zip"):
        with zipfile.ZipFile(package) as archive:
            if archive.testzip() is not None:
                errors.append(f"CRC failure: {package.relative_to(ROOT)}")
            for member in archive.infolist():
                pure = PurePosixPath(member.filename.replace("\\", "/"))
                if pure.is_absolute() or ".." in pure.parts:
                    errors.append(f"unsafe ZIP member: {package.relative_to(ROOT)}::{member.filename}")
    for line in (ROOT / "manifests" / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        expected, relative = line.split(None, 1)
        target = ROOT / relative.strip()
        if not target.is_file() or digest(target) != expected:
            errors.append(f"checksum mismatch: {relative.strip()}")
    if errors:
        print("VALIDATION FAILED")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print("VALIDATION OK: 18 finance skills, four source trees, packages, and checksums")
    return 0

if __name__ == "__main__":
    sys.exit(main())
