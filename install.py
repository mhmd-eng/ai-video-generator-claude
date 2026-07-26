#!/usr/bin/env python3
"""
Seedance 2.0 Creator Skills — Installer
========================================
Install AI video prompt engineering skills into Claude Code.

Usage:
    python install.py              # Interactive selection
    python install.py --all        # Install all skills
    python install.py --list       # List available skills
    python install.py --help       # Show help
"""

import sys
import shutil
import re
from pathlib import Path

# The Windows console defaults to cp1252, which cannot encode the box-drawing
# and check characters used below.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── Colors ──────────────────────────────────────────────────────────

class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    YELLOW = "\033[1;33m"
    CYAN = "\033[0;36m"
    BOLD = "\033[1m"
    NC = "\033[0m"


def header(text: str) -> None:
    print(f"\n{Colors.BLUE}{'═' * 56}{Colors.NC}")
    print(f"{Colors.BLUE} {text}{Colors.NC}")
    print(f"{Colors.BLUE}{'═' * 56}{Colors.NC}\n")


def ok(text: str) -> None:
    print(f"  {Colors.GREEN}✓{Colors.NC} {text}")


def warn(text: str) -> None:
    print(f"  {Colors.YELLOW}⚠{Colors.NC} {text}")


def err(text: str) -> None:
    print(f"  {Colors.RED}✗{Colors.NC} {text}")


# ── Skill discovery ─────────────────────────────────────────────────

def get_script_dir() -> Path:
    return Path(__file__).resolve().parent


def get_skills_source() -> Path:
    src = get_script_dir() / "skills"
    if not src.is_dir():
        err("Skills directory not found")
        sys.exit(1)
    return src


def discover_skills() -> list[dict]:
    """Find all skills with a SKILL.md file and extract their title."""
    src = get_skills_source()
    skills = []
    for skill_dir in sorted(src.iterdir()):
        skill_file = skill_dir / "SKILL.md"
        if skill_dir.is_dir() and skill_file.exists():
            skills.append({
                "name": skill_dir.name,
                "install_name": extract_skill_name(skill_file) or skill_dir.name,
                "path": skill_dir,
                "title": extract_title(skill_file),
            })
    return skills


def extract_skill_name(skill_file: Path) -> str | None:
    """Read `name:` from the SKILL.md YAML frontmatter.

    Claude Code identifies a skill by this name, so it is what the installed
    directory must be called — not the numbered source directory.
    """
    try:
        with open(skill_file, "r", encoding="utf-8") as f:
            if f.readline().strip() != "---":
                return None
            for line in f:
                if line.strip() == "---":
                    break
                match = re.match(r"name:\s*(\S+)", line)
                if match:
                    return match.group(1)
    except OSError:
        pass
    return None


def extract_title(skill_file: Path) -> str:
    """Extract the first H1 heading from a SKILL.md file."""
    try:
        with open(skill_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception:
        pass
    return "(untitled)"


# ── Claude skills directory ─────────────────────────────────────────

def detect_skills_dir() -> Path:
    """Claude Code reads user skills from ~/.claude/skills on every platform."""
    return Path.home() / ".claude" / "skills"


def ensure_skills_dir(skills_dir: Path) -> None:
    if skills_dir.exists():
        return
    warn(f"Claude skills directory not found: {skills_dir}")
    reply = input("  Create it? (y/n): ").strip().lower()
    if reply in ("y", "yes"):
        skills_dir.mkdir(parents=True, exist_ok=True)
        ok(f"Created: {skills_dir}")
    else:
        err("Cannot proceed without skills directory")
        sys.exit(1)


# ── Installation ────────────────────────────────────────────────────

def install_skill(skill: dict, dest_dir: Path) -> bool:
    """Copy a single skill into the Claude skills directory."""
    target = dest_dir / skill["install_name"]

    if target.exists():
        reply = input(f"  Overwrite {skill['install_name']}? (y/n): ").strip().lower()
        if reply not in ("y", "yes"):
            return False
        shutil.rmtree(target)

    shutil.copytree(skill["path"], target)
    ok(f"{skill['name']} → {skill['install_name']}")
    return True


# ── Commands ────────────────────────────────────────────────────────

def cmd_list(skills: list[dict]) -> None:
    header("Available Seedance 2.0 Creator Skills")
    for i, s in enumerate(skills, 1):
        print(f"  {Colors.CYAN}{i:2d}){Colors.NC} {s['name']:<22s} {s['title'][:50]}")
    print()
    ok(f"{len(skills)} skills available")


def cmd_install_all(skills: list[dict], dest: Path) -> int:
    header("Installing all skills")
    installed = sum(1 for s in skills if install_skill(s, dest))
    return installed


def cmd_interactive(skills: list[dict], dest: Path) -> int:
    header("Seedance 2.0 Creator Skills — Installer")

    for i, s in enumerate(skills, 1):
        print(f"  {i:2d}) {s['name']:<22s} {s['title'][:50]}")

    print(f"\n  Enter numbers (e.g. 1 3 5), 'all', or 'quit'")
    sel = input("  > ").strip().lower()

    if sel == "quit":
        sys.exit(0)

    if sel == "all":
        return sum(1 for s in skills if install_skill(s, dest))

    installed = 0
    for token in sel.split():
        try:
            num = int(token)
            if 1 <= num <= len(skills):
                if install_skill(skills[num - 1], dest):
                    installed += 1
            else:
                err(f"Invalid: {num}")
        except ValueError:
            err(f"Invalid: {token}")

    return installed


# ── Main ────────────────────────────────────────────────────────────

def main() -> None:
    skills = discover_skills()
    if not skills:
        err("No skills found in skills/ directory")
        sys.exit(1)

    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print(__doc__)
        return

    if "--list" in args:
        cmd_list(skills)
        return

    dest = detect_skills_dir()
    ensure_skills_dir(dest)

    if "--all" in args:
        installed = cmd_install_all(skills, dest)
    else:
        installed = cmd_interactive(skills, dest)

    print(f"\n{Colors.GREEN}Done.{Colors.NC} {installed} skill(s) installed to: {dest}")
    print("Restart Claude to load new skills.")


if __name__ == "__main__":
    main()
