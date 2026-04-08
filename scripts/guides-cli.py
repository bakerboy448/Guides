#!/usr/bin/env python3
"""Universal CLI tool for TRaSH Guides contributors.

Automates common operations that require coordinated changes across multiple
JSON files, enforcing all naming conventions and cross-reference rules from
CONTRIBUTING.md.

Supported commands:
    add-cf-to-group      Add an existing Custom Format to a cf-group
    include-group-in-profile  Add a quality profile to a cf-group's include list
    add-profile-to-group Register a quality profile in groups.json
    new-cf-group         Scaffold a new cf-group JSON file
    validate             Run all validation checks
    list-profiles        List all quality profiles for an app
    list-cf-groups       List all cf-groups for an app
    list-cfs             List all Custom Formats for an app

Requirements: Python 3.9+ (stdlib only, no external dependencies).
Works on Linux, macOS, and Windows.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

APPS = ("radarr", "sonarr")
BASE = Path("docs/json")
FILENAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def fatal(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def info(msg: str) -> None:
    print(f"  {msg}")


def success(msg: str) -> None:
    print(f"  OK: {msg}")


def load_json(path: Path) -> dict | list | None:
    """Load and return parsed JSON, or None on failure."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        fatal(f"Failed to read {path}: {exc}")
        return None  # unreachable, but keeps type checkers happy


def save_json(path: Path, data: dict | list) -> None:
    """Write JSON with consistent formatting (2-space indent, trailing newline)."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def generate_trash_id(name: str) -> str:
    """Generate an MD5-based trash_id from a name string."""
    return hashlib.md5(name.encode("utf-8")).hexdigest()


def slugify(name: str) -> str:
    """Convert a display name to a valid filename slug.

    Rules from CONTRIBUTING.md:
    - Lowercase
    - Spaces replaced by dashes
    - '+' replaced by 'plus'
    - Only alphanumeric and dashes allowed
    """
    slug = name.lower()
    slug = slug.replace("+", "plus")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    # Collapse multiple dashes
    slug = re.sub(r"-+", "-", slug)
    return slug


def validate_app_arg(app: str) -> str:
    """Validate and return the app argument."""
    app = app.lower()
    if app not in APPS:
        fatal(f"Invalid app '{app}'. Must be one of: {', '.join(APPS)}")
    return app


def resolve_base() -> Path:
    """Find the repo root by looking for docs/json/."""
    current = Path(".").resolve()
    candidates = [current, *current.parents]
    for candidate in candidates:
        if (candidate / "docs" / "json").is_dir():
            return candidate / "docs" / "json"
    fatal(
        "Cannot find docs/json/ directory. "
        "Run this script from the repository root or a subdirectory."
    )
    return BASE  # unreachable


# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------


def load_cf_index(base: Path, app: str) -> dict[str, tuple[str, str]]:
    """Return {trash_id: (filename, cf_name)} for all CFs in an app."""
    cf_dir = base / app / "cf"
    index: dict[str, tuple[str, str]] = {}
    if not cf_dir.is_dir():
        return index
    for f in sorted(cf_dir.glob("*.json")):
        data = load_json(f)
        if data and isinstance(data, dict):
            tid = data.get("trash_id", "")
            name = data.get("name", "")
            if tid:
                index[tid] = (f.name, name)
    return index


def load_profile_index(base: Path, app: str) -> dict[str, dict]:
    """Return {slug: profile_data} for all quality profiles in an app."""
    profiles_dir = base / app / "quality-profiles"
    index: dict[str, dict] = {}
    if not profiles_dir.is_dir():
        return index
    for f in sorted(profiles_dir.glob("*.json")):
        data = load_json(f)
        if data and isinstance(data, dict):
            index[f.stem] = data
    return index


def load_groups(base: Path, app: str) -> list[dict]:
    """Load quality-profile-groups/groups.json for an app."""
    groups_file = base / app / "quality-profile-groups" / "groups.json"
    if not groups_file.is_file():
        fatal(f"groups.json not found: {groups_file}")
    data = load_json(groups_file)
    if not isinstance(data, list):
        fatal(f"Expected JSON array in {groups_file}")
    return data


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------


def cmd_add_cf_to_group(args: argparse.Namespace) -> int:
    """Add a Custom Format to an existing cf-group."""
    base = resolve_base()
    app = validate_app_arg(args.app)

    cf_index = load_cf_index(base, app)

    # Resolve the CF
    cf_tid = args.cf_trash_id
    if cf_tid not in cf_index:
        fatal(
            f"Custom Format with trash_id '{cf_tid}' not found in {app}/cf/. "
            f"Use 'list-cfs --app {app}' to see available CFs."
        )
    cf_filename, cf_name = cf_index[cf_tid]

    # Resolve the cf-group file
    group_file = base / app / "cf-groups" / args.group_file
    if not group_file.suffix:
        group_file = group_file.with_suffix(".json")
    if not group_file.is_file():
        fatal(
            f"cf-group file not found: {group_file}. "
            f"Use 'list-cf-groups --app {app}' to see available groups."
        )

    group_data = load_json(group_file)
    if not isinstance(group_data, dict):
        fatal(f"Expected JSON object in {group_file}")

    # Check if CF already exists in the group
    existing_tids = {
        entry.get("trash_id") for entry in group_data.get("custom_formats", [])
    }
    if cf_tid in existing_tids:
        fatal(f"CF '{cf_name}' ({cf_tid}) already exists in {group_file.name}")

    # Build the new entry
    required = args.required if args.required is not None else True
    new_entry: dict = {
        "name": cf_name,
        "trash_id": cf_tid,
        "required": required,
    }
    if args.default is not None:
        new_entry["default"] = args.default

    group_data.setdefault("custom_formats", []).append(new_entry)
    save_json(group_file, group_data)

    success(f"Added CF '{cf_name}' ({cf_tid}) to {app}/cf-groups/{group_file.name}")
    if not required:
        info("  (required: false — user can individually toggle this CF)")
    return 0


def cmd_include_group_in_profile(args: argparse.Namespace) -> int:
    """Add a quality profile reference to a cf-group's quality_profiles.include."""
    base = resolve_base()
    app = validate_app_arg(args.app)

    profiles = load_profile_index(base, app)

    # Resolve profile by slug
    slug = args.profile_slug
    if slug not in profiles:
        fatal(
            f"Profile '{slug}' not found in {app}/quality-profiles/. "
            f"Use 'list-profiles --app {app}' to see available profiles."
        )
    profile_data = profiles[slug]
    profile_name = profile_data.get("name", "")
    profile_tid = profile_data.get("trash_id", "")

    # Resolve the cf-group file
    group_file = base / app / "cf-groups" / args.group_file
    if not group_file.suffix:
        group_file = group_file.with_suffix(".json")
    if not group_file.is_file():
        fatal(f"cf-group file not found: {group_file}")

    group_data = load_json(group_file)
    if not isinstance(group_data, dict):
        fatal(f"Expected JSON object in {group_file}")

    # Ensure quality_profiles.include structure exists
    if "quality_profiles" not in group_data:
        group_data["quality_profiles"] = {"include": {}}
    elif "include" not in group_data["quality_profiles"]:
        group_data["quality_profiles"]["include"] = {}

    include = group_data["quality_profiles"]["include"]

    # Check if profile already included
    if profile_name in include:
        fatal(
            f"Profile '{profile_name}' already in "
            f"{group_file.name} quality_profiles.include"
        )

    include[profile_name] = profile_tid
    save_json(group_file, group_data)

    success(
        f"Added profile '{profile_name}' ({profile_tid}) "
        f"to {app}/cf-groups/{group_file.name}"
    )
    return 0


def cmd_add_profile_to_group(args: argparse.Namespace) -> int:
    """Register a quality profile in quality-profile-groups/groups.json."""
    base = resolve_base()
    app = validate_app_arg(args.app)

    profiles = load_profile_index(base, app)
    slug = args.profile_slug
    if slug not in profiles:
        fatal(
            f"Profile '{slug}' not found in {app}/quality-profiles/. "
            f"Use 'list-profiles --app {app}' to see available profiles."
        )
    profile_tid = profiles[slug].get("trash_id", "")

    groups_file = base / app / "quality-profile-groups" / "groups.json"
    groups_data = load_groups(base, app)

    group_name = args.group_name

    # Find or report available groups
    target_group = None
    available = []
    for group in groups_data:
        available.append(group.get("name", ""))
        if group.get("name", "") == group_name:
            target_group = group

    if target_group is None:
        fatal(
            f"Group '{group_name}' not found in groups.json. "
            f"Available groups: {', '.join(available)}"
        )

    # Check if slug already present
    if slug in target_group.get("profiles", {}):
        fatal(f"Profile '{slug}' already in group '{group_name}'")

    target_group.setdefault("profiles", {})[slug] = profile_tid
    save_json(groups_file, groups_data)

    success(
        f"Added profile '{slug}' ({profile_tid}) to group '{group_name}' "
        f"in {app}/quality-profile-groups/groups.json"
    )
    return 0


def cmd_new_cf_group(args: argparse.Namespace) -> int:
    """Scaffold a new cf-group JSON file."""
    base = resolve_base()
    app = validate_app_arg(args.app)

    name = args.name
    slug = slugify(name)

    if not FILENAME_RE.match(slug):
        fatal(
            f"Generated slug '{slug}' violates naming convention. "
            "Must be lowercase alphanumeric with dashes only."
        )

    out_file = base / app / "cf-groups" / f"{slug}.json"
    if out_file.exists():
        fatal(f"File already exists: {out_file}")

    trash_id = generate_trash_id(name)
    description = args.description or f"Collection of Custom Formats for {name}"

    group_data: dict = {
        "name": name,
        "trash_id": trash_id,
        "trash_description": description,
        "custom_formats": [],
        "quality_profiles": {
            "include": {}
        },
    }

    if args.default:
        group_data["default"] = "true"

    save_json(out_file, group_data)

    success(f"Created {app}/cf-groups/{slug}.json")
    info(f"  trash_id: {trash_id}")
    info(f"  name: {name}")
    info("")
    info("Next steps:")
    info(f"  1. Add CFs:     python scripts/guides-cli.py add-cf-to-group --app {app} --group-file {slug}.json --cf-trash-id <TRASH_ID>")
    info(f"  2. Link profiles: python scripts/guides-cli.py include-group-in-profile --app {app} --group-file {slug}.json --profile-slug <SLUG>")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    """Run all validation checks (calls existing validation scripts)."""
    import subprocess

    scripts_dir = Path(__file__).resolve().parent
    errors = 0

    print("Running Custom Format validation...")
    cf_script = scripts_dir / "validate-custom-formats.py"
    if cf_script.is_file():
        result = subprocess.run(
            [sys.executable, str(cf_script)],
            capture_output=False,
        )
        if result.returncode != 0:
            errors += 1
    else:
        print(f"  WARNING: {cf_script} not found, skipping")

    print("\nRunning Quality Profile validation...")
    qp_script = scripts_dir / "validate-quality-profiles.py"
    if qp_script.is_file():
        result = subprocess.run(
            [sys.executable, str(qp_script)],
            capture_output=False,
        )
        if result.returncode != 0:
            errors += 1
    else:
        print(f"  WARNING: {qp_script} not found, skipping")

    if errors:
        print(f"\n{errors} validation script(s) failed.")
        return 1

    print("\nAll validations passed.")
    return 0


def cmd_list_profiles(args: argparse.Namespace) -> int:
    """List all quality profiles for an app."""
    base = resolve_base()
    app = validate_app_arg(args.app)

    profiles = load_profile_index(base, app)
    groups_data = load_groups(base, app)

    # Build reverse lookup: slug -> group name
    slug_to_group: dict[str, str] = {}
    for group in groups_data:
        for slug in group.get("profiles", {}):
            slug_to_group[slug] = group.get("name", "")

    print(f"\nQuality Profiles for {app} ({len(profiles)} total):\n")
    print(f"  {'Slug':<45} {'Name':<45} {'Group':<15} {'trash_id'}")
    print(f"  {'─' * 45} {'─' * 45} {'─' * 15} {'─' * 32}")

    for slug in sorted(profiles):
        data = profiles[slug]
        name = data.get("name", "")
        tid = data.get("trash_id", "")
        group = slug_to_group.get(slug, "(none)")
        print(f"  {slug:<45} {name:<45} {group:<15} {tid}")

    return 0


def cmd_list_cf_groups(args: argparse.Namespace) -> int:
    """List all cf-groups for an app."""
    base = resolve_base()
    app = validate_app_arg(args.app)

    cf_groups_dir = base / app / "cf-groups"
    if not cf_groups_dir.is_dir():
        fatal(f"cf-groups directory not found: {cf_groups_dir}")

    groups: list[tuple[str, str, str, int, int]] = []
    for f in sorted(cf_groups_dir.glob("*.json")):
        data = load_json(f)
        if data and isinstance(data, dict):
            name = data.get("name", "")
            tid = data.get("trash_id", "")
            n_cfs = len(data.get("custom_formats", []))
            n_profiles = len(
                data.get("quality_profiles", {}).get("include", {})
            )
            groups.append((f.stem, name, tid, n_cfs, n_profiles))

    print(f"\nCF-Groups for {app} ({len(groups)} total):\n")
    print(f"  {'File':<50} {'Name':<40} {'CFs':>4} {'Profiles':>8} {'trash_id'}")
    print(f"  {'─' * 50} {'─' * 40} {'─' * 4} {'─' * 8} {'─' * 32}")

    for slug, name, tid, n_cfs, n_profiles in groups:
        print(f"  {slug:<50} {name:<40} {n_cfs:>4} {n_profiles:>8} {tid}")

    return 0


def cmd_list_cfs(args: argparse.Namespace) -> int:
    """List all Custom Formats for an app."""
    base = resolve_base()
    app = validate_app_arg(args.app)

    cf_index = load_cf_index(base, app)

    print(f"\nCustom Formats for {app} ({len(cf_index)} total):\n")
    print(f"  {'trash_id':<34} {'Name'}")
    print(f"  {'─' * 34} {'─' * 50}")

    for tid in sorted(cf_index, key=lambda t: cf_index[t][1].lower()):
        filename, name = cf_index[tid]
        print(f"  {tid}  {name}")

    return 0


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="guides-cli",
        description="TRaSH Guides contributor CLI — automate common JSON operations.",
        epilog="Run '<command> --help' for command-specific help.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -- add-cf-to-group --
    p = subparsers.add_parser(
        "add-cf-to-group",
        help="Add a Custom Format to an existing cf-group",
    )
    p.add_argument("--app", required=True, choices=APPS, help="Target app (radarr or sonarr)")
    p.add_argument("--group-file", required=True, help="cf-group filename (e.g. audio-formats.json)")
    p.add_argument("--cf-trash-id", required=True, help="trash_id of the Custom Format to add")
    p.add_argument("--required", type=lambda v: v.lower() == "true", default=None, help="Whether the CF is required (true/false, default: true)")
    p.add_argument("--default", type=lambda v: v.lower() == "true", default=None, help="Whether the CF is checked by default (only for required=false)")

    # -- include-group-in-profile --
    p = subparsers.add_parser(
        "include-group-in-profile",
        help="Add a quality profile to a cf-group's quality_profiles.include",
    )
    p.add_argument("--app", required=True, choices=APPS, help="Target app")
    p.add_argument("--group-file", required=True, help="cf-group filename")
    p.add_argument("--profile-slug", required=True, help="Quality profile slug (filename without .json)")

    # -- add-profile-to-group --
    p = subparsers.add_parser(
        "add-profile-to-group",
        help="Register a quality profile in groups.json",
    )
    p.add_argument("--app", required=True, choices=APPS, help="Target app")
    p.add_argument("--profile-slug", required=True, help="Quality profile slug")
    p.add_argument("--group-name", required=True, help="Group name in groups.json (e.g. Standard, Anime, French)")

    # -- new-cf-group --
    p = subparsers.add_parser(
        "new-cf-group",
        help="Scaffold a new cf-group JSON file",
    )
    p.add_argument("--app", required=True, choices=APPS, help="Target app")
    p.add_argument("--name", required=True, help="Display name for the group (e.g. '[Audio] Audio Formats')")
    p.add_argument("--description", help="Description of the group")
    p.add_argument("--default", action="store_true", help="Enable the group by default")

    # -- validate --
    subparsers.add_parser(
        "validate",
        help="Run all validation checks",
    )

    # -- list-profiles --
    p = subparsers.add_parser(
        "list-profiles",
        help="List all quality profiles for an app",
    )
    p.add_argument("--app", required=True, choices=APPS, help="Target app")

    # -- list-cf-groups --
    p = subparsers.add_parser(
        "list-cf-groups",
        help="List all cf-groups for an app",
    )
    p.add_argument("--app", required=True, choices=APPS, help="Target app")

    # -- list-cfs --
    p = subparsers.add_parser(
        "list-cfs",
        help="List all Custom Formats for an app",
    )
    p.add_argument("--app", required=True, choices=APPS, help="Target app")

    return parser


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

COMMANDS = {
    "add-cf-to-group": cmd_add_cf_to_group,
    "include-group-in-profile": cmd_include_group_in_profile,
    "add-profile-to-group": cmd_add_profile_to_group,
    "new-cf-group": cmd_new_cf_group,
    "validate": cmd_validate,
    "list-profiles": cmd_list_profiles,
    "list-cf-groups": cmd_list_cf_groups,
    "list-cfs": cmd_list_cfs,
}


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    handler = COMMANDS.get(args.command)
    if handler is None:
        parser.print_help()
        return 1
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
