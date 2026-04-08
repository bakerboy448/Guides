#!/usr/bin/env python3
"""Test suite for guides-cli.py.

Uses isolated temporary fixtures via --base-dir so tests never touch real data.
Runs with stdlib unittest — no pytest or other external dependencies required.

Usage:
    python scripts/test-guides-cli.py          # run all tests
    python scripts/test-guides-cli.py -v       # verbose output
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = str(Path(__file__).resolve().parent / "guides-cli.py")


# ---------------------------------------------------------------------------
# Fixture helpers
# ---------------------------------------------------------------------------


def create_fixture(tmp: Path) -> Path:
    """Build a minimal but valid docs/json tree and return the base path."""
    base = tmp  # The --base-dir points directly at the content root

    for app in ("radarr", "sonarr"):
        # cf/ directory with two sample CFs
        cf_dir = base / app / "cf"
        cf_dir.mkdir(parents=True)

        save(cf_dir / "truehd-atmos.json", {
            "trash_id": "496f355514737f7d83bf7aa4d24f8169",
            "trash_scores": {"default": 5000},
            "name": "TrueHD ATMOS",
            "includeCustomFormatWhenRenaming": False,
            "specifications": [],
        })
        save(cf_dir / "3d.json", {
            "trash_id": "b8cd450cbfa689c0259a01d9e29ba3d6",
            "trash_scores": {"default": -10000},
            "name": "3D",
            "includeCustomFormatWhenRenaming": False,
            "specifications": [],
        })
        save(cf_dir / "br-disk.json", {
            "trash_id": "ed38b889b31be83fda192888e2286d83",
            "trash_scores": {"default": -10000},
            "name": "BR-DISK",
            "includeCustomFormatWhenRenaming": False,
            "specifications": [],
        })

        # cf-groups/ directory with one sample group
        cfg_dir = base / app / "cf-groups"
        cfg_dir.mkdir(parents=True)

        save(cfg_dir / "audio-formats.json", {
            "name": "[Audio] Audio Formats",
            "trash_id": "9d5acd8f1da78dfbae788182f7605200",
            "trash_description": "Audio Formats collection",
            "custom_formats": [
                {
                    "name": "TrueHD ATMOS",
                    "trash_id": "496f355514737f7d83bf7aa4d24f8169",
                    "required": True,
                },
            ],
            "quality_profiles": {
                "include": {
                    "HD Bluray + WEB": "d1d67249d3890e49bc12e275d989a7e9",
                },
            },
        })

        # quality-profiles/ with one profile
        qp_dir = base / app / "quality-profiles"
        qp_dir.mkdir(parents=True)

        save(qp_dir / "hd-bluray-web.json", {
            "trash_id": "d1d67249d3890e49bc12e275d989a7e9",
            "name": "HD Bluray + WEB",
            "trash_description": "Quality Profile",
            "group": 1,
            "upgradeAllowed": True,
            "cutoff": "Bluray-1080p",
            "minFormatScore": 0,
            "cutoffFormatScore": 10000,
            "minUpgradeFormatScore": 1,
            "language": "Original",
            "items": [{"name": "Bluray-1080p", "allowed": True}],
            "formatItems": {
                "BR-DISK": "ed38b889b31be83fda192888e2286d83",
            },
        })
        save(qp_dir / "remux-web-1080p.json", {
            "trash_id": "9ca12ea80aa55ef916e3751f4b874151",
            "name": "Remux + WEB 1080p",
            "trash_description": "Quality Profile",
            "group": 1,
            "upgradeAllowed": True,
            "cutoff": "Remux-1080p",
            "minFormatScore": 0,
            "cutoffFormatScore": 10000,
            "minUpgradeFormatScore": 1,
            "language": "Original",
            "items": [{"name": "Remux-1080p", "allowed": True}],
            "formatItems": {},
        })

        # quality-profile-groups/
        gpg_dir = base / app / "quality-profile-groups"
        gpg_dir.mkdir(parents=True)

        save(gpg_dir / "groups.json", [
            {
                "name": "Standard",
                "profiles": {
                    "hd-bluray-web": "d1d67249d3890e49bc12e275d989a7e9",
                },
            },
            {
                "name": "Anime",
                "profiles": {},
            },
        ])

    return base


def save(path: Path, data: dict | list) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def load(path: Path) -> dict | list:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def run_cli(*args: str) -> subprocess.CompletedProcess:
    """Run guides-cli.py with the given arguments."""
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True,
        text=True,
    )


# ---------------------------------------------------------------------------
# Unit tests: helper functions
# ---------------------------------------------------------------------------


class TestSlugify(unittest.TestCase):
    def test_basic_lowercase(self):
        # Import the function directly
        sys.path.insert(0, str(Path(SCRIPT).parent))
        from importlib import import_module
        mod = import_module("guides-cli")
        self.assertEqual(mod.slugify("HD Bluray + WEB"), "hd-bluray-plus-web")
        self.assertEqual(mod.slugify("TrueHD ATMOS"), "truehd-atmos")
        self.assertEqual(mod.slugify("[Audio] Audio Formats"), "audio-audio-formats")
        self.assertEqual(mod.slugify("simple"), "simple")
        self.assertEqual(mod.slugify("a--b"), "a-b")


class TestGenerateTrashId(unittest.TestCase):
    def test_deterministic(self):
        sys.path.insert(0, str(Path(SCRIPT).parent))
        from importlib import import_module
        mod = import_module("guides-cli")
        # Same input produces same output
        self.assertEqual(mod.generate_trash_id("test"), mod.generate_trash_id("test"))
        # Different inputs produce different outputs
        self.assertNotEqual(mod.generate_trash_id("a"), mod.generate_trash_id("b"))
        # Output is 32-char hex
        result = mod.generate_trash_id("BR-DISK")
        self.assertEqual(len(result), 32)
        self.assertTrue(all(c in "0123456789abcdef" for c in result))


# ---------------------------------------------------------------------------
# Integration tests: commands against fixtures
# ---------------------------------------------------------------------------


class FixtureTestCase(unittest.TestCase):
    """Base class that sets up a temp fixture directory per test."""

    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp(prefix="guides-cli-test-")
        self.base = create_fixture(Path(self.tmp_dir))

    def tearDown(self):
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def cli(self, *args: str) -> subprocess.CompletedProcess:
        return run_cli("--base-dir", str(self.base), *args)


# -- add-cf-to-group --

class TestAddCfToGroup(FixtureTestCase):
    def test_success(self):
        """Add a CF that doesn't exist in the group yet."""
        result = self.cli(
            "add-cf-to-group", "--app", "radarr",
            "--group-file", "audio-formats.json",
            "--cf-trash-id", "b8cd450cbfa689c0259a01d9e29ba3d6",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = load(self.base / "radarr" / "cf-groups" / "audio-formats.json")
        tids = [cf["trash_id"] for cf in data["custom_formats"]]
        self.assertIn("b8cd450cbfa689c0259a01d9e29ba3d6", tids)
        # Check name was resolved correctly
        added = [cf for cf in data["custom_formats"] if cf["trash_id"] == "b8cd450cbfa689c0259a01d9e29ba3d6"][0]
        self.assertEqual(added["name"], "3D")
        self.assertTrue(added["required"])

    def test_with_required_false(self):
        """Add a CF with required=false."""
        result = self.cli(
            "add-cf-to-group", "--app", "radarr",
            "--group-file", "audio-formats.json",
            "--cf-trash-id", "b8cd450cbfa689c0259a01d9e29ba3d6",
            "--required", "false",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = load(self.base / "radarr" / "cf-groups" / "audio-formats.json")
        added = [cf for cf in data["custom_formats"] if cf["trash_id"] == "b8cd450cbfa689c0259a01d9e29ba3d6"][0]
        self.assertFalse(added["required"])

    def test_with_default_flag(self):
        """Add a CF with --default true."""
        result = self.cli(
            "add-cf-to-group", "--app", "radarr",
            "--group-file", "audio-formats.json",
            "--cf-trash-id", "b8cd450cbfa689c0259a01d9e29ba3d6",
            "--required", "false", "--default", "true",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = load(self.base / "radarr" / "cf-groups" / "audio-formats.json")
        added = [cf for cf in data["custom_formats"] if cf["trash_id"] == "b8cd450cbfa689c0259a01d9e29ba3d6"][0]
        self.assertTrue(added["default"])

    def test_duplicate_rejected(self):
        """Adding the same CF twice should fail."""
        result = self.cli(
            "add-cf-to-group", "--app", "radarr",
            "--group-file", "audio-formats.json",
            "--cf-trash-id", "496f355514737f7d83bf7aa4d24f8169",  # already in fixture
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("already exists", result.stderr)

    def test_invalid_trash_id(self):
        """Non-existent trash_id should fail."""
        result = self.cli(
            "add-cf-to-group", "--app", "radarr",
            "--group-file", "audio-formats.json",
            "--cf-trash-id", "00000000000000000000000000000000",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("not found", result.stderr)

    def test_missing_group_file(self):
        """Non-existent cf-group file should fail."""
        result = self.cli(
            "add-cf-to-group", "--app", "radarr",
            "--group-file", "nonexistent.json",
            "--cf-trash-id", "b8cd450cbfa689c0259a01d9e29ba3d6",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("not found", result.stderr)

    def test_sonarr_works(self):
        """Ensure sonarr app works too."""
        result = self.cli(
            "add-cf-to-group", "--app", "sonarr",
            "--group-file", "audio-formats.json",
            "--cf-trash-id", "b8cd450cbfa689c0259a01d9e29ba3d6",
        )
        self.assertEqual(result.returncode, 0, result.stderr)


# -- add-cf-to-profile --

class TestAddCfToProfile(FixtureTestCase):
    def test_success(self):
        """Add a CF to a profile's formatItems."""
        result = self.cli(
            "add-cf-to-profile", "--app", "radarr",
            "--profile-slug", "hd-bluray-web",
            "--cf-trash-id", "496f355514737f7d83bf7aa4d24f8169",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = load(self.base / "radarr" / "quality-profiles" / "hd-bluray-web.json")
        self.assertIn("TrueHD ATMOS", data["formatItems"])
        self.assertEqual(data["formatItems"]["TrueHD ATMOS"], "496f355514737f7d83bf7aa4d24f8169")

    def test_duplicate_by_name(self):
        """Adding a CF that's already in formatItems (by name) should fail."""
        result = self.cli(
            "add-cf-to-profile", "--app", "radarr",
            "--profile-slug", "hd-bluray-web",
            "--cf-trash-id", "ed38b889b31be83fda192888e2286d83",  # BR-DISK already in fixture
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("already in", result.stderr)

    def test_invalid_profile(self):
        """Non-existent profile slug should fail."""
        result = self.cli(
            "add-cf-to-profile", "--app", "radarr",
            "--profile-slug", "nonexistent",
            "--cf-trash-id", "496f355514737f7d83bf7aa4d24f8169",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("not found", result.stderr)

    def test_preserves_existing_items(self):
        """Existing formatItems should be preserved after adding a new one."""
        result = self.cli(
            "add-cf-to-profile", "--app", "radarr",
            "--profile-slug", "hd-bluray-web",
            "--cf-trash-id", "496f355514737f7d83bf7aa4d24f8169",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = load(self.base / "radarr" / "quality-profiles" / "hd-bluray-web.json")
        # Original entry still present
        self.assertIn("BR-DISK", data["formatItems"])
        # New entry added
        self.assertIn("TrueHD ATMOS", data["formatItems"])


# -- include-group-in-profile --

class TestIncludeGroupInProfile(FixtureTestCase):
    def test_success(self):
        """Add a profile to a cf-group's include list."""
        result = self.cli(
            "include-group-in-profile", "--app", "radarr",
            "--group-file", "audio-formats.json",
            "--profile-slug", "remux-web-1080p",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = load(self.base / "radarr" / "cf-groups" / "audio-formats.json")
        include = data["quality_profiles"]["include"]
        self.assertIn("Remux + WEB 1080p", include)
        self.assertEqual(include["Remux + WEB 1080p"], "9ca12ea80aa55ef916e3751f4b874151")

    def test_duplicate_rejected(self):
        """Adding the same profile twice should fail."""
        result = self.cli(
            "include-group-in-profile", "--app", "radarr",
            "--group-file", "audio-formats.json",
            "--profile-slug", "hd-bluray-web",  # already in fixture
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("already in", result.stderr)

    def test_invalid_profile(self):
        """Non-existent profile should fail."""
        result = self.cli(
            "include-group-in-profile", "--app", "radarr",
            "--group-file", "audio-formats.json",
            "--profile-slug", "nonexistent",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("not found", result.stderr)


# -- add-profile-to-group --

class TestAddProfileToGroup(FixtureTestCase):
    def test_success(self):
        """Register a profile in groups.json under an existing group."""
        result = self.cli(
            "add-profile-to-group", "--app", "radarr",
            "--profile-slug", "remux-web-1080p",
            "--group-name", "Standard",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        groups = load(self.base / "radarr" / "quality-profile-groups" / "groups.json")
        standard = [g for g in groups if g["name"] == "Standard"][0]
        self.assertIn("remux-web-1080p", standard["profiles"])
        self.assertEqual(standard["profiles"]["remux-web-1080p"], "9ca12ea80aa55ef916e3751f4b874151")

    def test_duplicate_rejected(self):
        """Adding an already-registered profile should fail."""
        result = self.cli(
            "add-profile-to-group", "--app", "radarr",
            "--profile-slug", "hd-bluray-web",  # already in Standard
            "--group-name", "Standard",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("already in", result.stderr)

    def test_invalid_group_name(self):
        """Non-existent group name should fail with available groups listed."""
        result = self.cli(
            "add-profile-to-group", "--app", "radarr",
            "--profile-slug", "remux-web-1080p",
            "--group-name", "Nonexistent",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("not found", result.stderr)
        self.assertIn("Standard", result.stderr)

    def test_invalid_profile(self):
        """Non-existent profile slug should fail."""
        result = self.cli(
            "add-profile-to-group", "--app", "radarr",
            "--profile-slug", "nonexistent",
            "--group-name", "Standard",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("not found", result.stderr)


# -- new-cf-group --

class TestNewCfGroup(FixtureTestCase):
    def test_success(self):
        """Scaffold a new cf-group file."""
        result = self.cli(
            "new-cf-group", "--app", "radarr",
            "--name", "[Test] My Group",
            "--description", "A test group",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        path = self.base / "radarr" / "cf-groups" / "test-my-group.json"
        self.assertTrue(path.exists(), f"Expected {path} to be created")
        data = load(path)
        self.assertEqual(data["name"], "[Test] My Group")
        self.assertEqual(len(data["trash_id"]), 32)
        self.assertEqual(data["trash_description"], "A test group")
        self.assertEqual(data["custom_formats"], [])
        self.assertEqual(data["quality_profiles"], {"include": {}})

    def test_with_default_flag(self):
        """Scaffold with --default should set default: true."""
        result = self.cli(
            "new-cf-group", "--app", "radarr",
            "--name", "[Test] Default Group",
            "--default",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        path = self.base / "radarr" / "cf-groups" / "test-default-group.json"
        data = load(path)
        self.assertEqual(data["default"], "true")

    def test_duplicate_rejected(self):
        """Creating a cf-group that already exists should fail."""
        result = self.cli(
            "new-cf-group", "--app", "radarr",
            "--name", "Audio Formats",  # slug "audio-formats" matches existing file
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("already exists", result.stderr)

    def test_auto_description(self):
        """Omitting --description should generate a default one."""
        result = self.cli(
            "new-cf-group", "--app", "radarr",
            "--name", "My Group",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        data = load(self.base / "radarr" / "cf-groups" / "my-group.json")
        self.assertIn("My Group", data["trash_description"])


# -- new-profile-group --

class TestNewProfileGroup(FixtureTestCase):
    def test_success(self):
        """Create a new group category in groups.json."""
        result = self.cli(
            "new-profile-group", "--app", "radarr",
            "--name", "Spanish",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        groups = load(self.base / "radarr" / "quality-profile-groups" / "groups.json")
        names = [g["name"] for g in groups]
        self.assertIn("Spanish", names)
        spanish = [g for g in groups if g["name"] == "Spanish"][0]
        self.assertEqual(spanish["profiles"], {})

    def test_duplicate_rejected(self):
        """Creating a group that already exists should fail."""
        result = self.cli(
            "new-profile-group", "--app", "radarr",
            "--name", "Standard",  # already exists
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("already exists", result.stderr)

    def test_preserves_existing_groups(self):
        """Existing groups should not be modified."""
        result = self.cli(
            "new-profile-group", "--app", "radarr",
            "--name", "Italian",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        groups = load(self.base / "radarr" / "quality-profile-groups" / "groups.json")
        standard = [g for g in groups if g["name"] == "Standard"][0]
        self.assertIn("hd-bluray-web", standard["profiles"])


# -- list commands --

class TestListCommands(FixtureTestCase):
    def test_list_profiles(self):
        result = self.cli("list-profiles", "--app", "radarr")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("hd-bluray-web", result.stdout)
        self.assertIn("HD Bluray + WEB", result.stdout)
        self.assertIn("2 total", result.stdout)

    def test_list_cf_groups(self):
        result = self.cli("list-cf-groups", "--app", "radarr")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("audio-formats", result.stdout)
        self.assertIn("1 total", result.stdout)

    def test_list_cfs(self):
        result = self.cli("list-cfs", "--app", "radarr")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("TrueHD ATMOS", result.stdout)
        self.assertIn("3D", result.stdout)
        self.assertIn("3 total", result.stdout)


# -- edge cases --

class TestEdgeCases(FixtureTestCase):
    def test_invalid_app(self):
        """Invalid app argument should fail."""
        result = run_cli(
            "--base-dir", str(self.base),
            "list-cfs", "--app", "lidarr",
        )
        self.assertNotEqual(result.returncode, 0)

    def test_base_dir_not_found(self):
        """Non-existent --base-dir should fail."""
        result = run_cli(
            "--base-dir", "/tmp/nonexistent-dir-xyz",
            "list-cfs", "--app", "radarr",
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("not found", result.stderr)

    def test_json_output_trailing_newline(self):
        """All JSON files should end with a trailing newline."""
        self.cli(
            "new-cf-group", "--app", "radarr",
            "--name", "Newline Test Group",
        )
        path = self.base / "radarr" / "cf-groups" / "newline-test-group.json"
        content = path.read_text(encoding="utf-8")
        self.assertTrue(content.endswith("\n"), "JSON file should end with newline")
        # And it should be valid JSON
        json.loads(content)


# -- workflow simulation: full end-to-end --

class TestEndToEndWorkflow(FixtureTestCase):
    """Simulate a contributor creating a new cf-group, adding CFs, linking profiles."""

    def test_full_cf_group_workflow(self):
        """End-to-end: create group -> add CFs -> link profile."""
        # 1. Create a new cf-group
        r = self.cli(
            "new-cf-group", "--app", "radarr",
            "--name", "[Streaming] Test Services",
            "--description", "Test streaming services",
        )
        self.assertEqual(r.returncode, 0, r.stderr)

        # 2. Add CFs to it
        r = self.cli(
            "add-cf-to-group", "--app", "radarr",
            "--group-file", "streaming-test-services.json",
            "--cf-trash-id", "b8cd450cbfa689c0259a01d9e29ba3d6",
        )
        self.assertEqual(r.returncode, 0, r.stderr)

        r = self.cli(
            "add-cf-to-group", "--app", "radarr",
            "--group-file", "streaming-test-services.json",
            "--cf-trash-id", "ed38b889b31be83fda192888e2286d83",
            "--required", "false", "--default", "true",
        )
        self.assertEqual(r.returncode, 0, r.stderr)

        # 3. Link a profile
        r = self.cli(
            "include-group-in-profile", "--app", "radarr",
            "--group-file", "streaming-test-services.json",
            "--profile-slug", "hd-bluray-web",
        )
        self.assertEqual(r.returncode, 0, r.stderr)

        # 4. Verify final state
        data = load(self.base / "radarr" / "cf-groups" / "streaming-test-services.json")
        self.assertEqual(data["name"], "[Streaming] Test Services")
        self.assertEqual(len(data["custom_formats"]), 2)
        self.assertIn("HD Bluray + WEB", data["quality_profiles"]["include"])

        # CF entries
        cf_names = [cf["name"] for cf in data["custom_formats"]]
        self.assertIn("3D", cf_names)
        self.assertIn("BR-DISK", cf_names)

        # BR-DISK should be optional with default
        br = [cf for cf in data["custom_formats"] if cf["name"] == "BR-DISK"][0]
        self.assertFalse(br["required"])
        self.assertTrue(br["default"])

    def test_full_profile_workflow(self):
        """End-to-end: create profile group -> register profile -> add CF to profile."""
        # 1. Create a new group category
        r = self.cli(
            "new-profile-group", "--app", "radarr",
            "--name", "Spanish",
        )
        self.assertEqual(r.returncode, 0, r.stderr)

        # 2. Register an existing profile under it
        r = self.cli(
            "add-profile-to-group", "--app", "radarr",
            "--profile-slug", "remux-web-1080p",
            "--group-name", "Spanish",
        )
        self.assertEqual(r.returncode, 0, r.stderr)

        # 3. Add a CF to the profile's formatItems
        r = self.cli(
            "add-cf-to-profile", "--app", "radarr",
            "--profile-slug", "remux-web-1080p",
            "--cf-trash-id", "496f355514737f7d83bf7aa4d24f8169",
        )
        self.assertEqual(r.returncode, 0, r.stderr)

        # 4. Verify groups.json
        groups = load(self.base / "radarr" / "quality-profile-groups" / "groups.json")
        spanish = [g for g in groups if g["name"] == "Spanish"][0]
        self.assertIn("remux-web-1080p", spanish["profiles"])

        # 5. Verify profile formatItems
        profile = load(self.base / "radarr" / "quality-profiles" / "remux-web-1080p.json")
        self.assertIn("TrueHD ATMOS", profile["formatItems"])


if __name__ == "__main__":
    unittest.main()
