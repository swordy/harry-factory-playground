#!/usr/bin/env python3
"""
Test suite for documentation validation.
Ensures all required documentation files are present and properly formatted.
"""

import os
import re
from pathlib import Path


class DocumentationValidator:
    """Validates project documentation completeness and quality."""

    def __init__(self, project_root="."):
        self.project_root = Path(project_root)
        self.errors = []
        self.warnings = []

    def validate(self):
        """Run all validation checks."""
        self.check_required_files()
        self.check_readme_sections()
        self.check_file_quality()
        return len(self.errors) == 0

    def check_required_files(self):
        """Verify all required documentation files exist."""
        required_files = [
            "README.md",
            "CONTRIBUTING.md",
            "CHANGELOG.md",
            "ARCHITECTURE.md",
            "SUPPORT.md",
            "LICENSE",
            ".gitignore",
        ]

        for filename in required_files:
            filepath = self.project_root / filename
            if not filepath.exists():
                self.errors.append(f"❌ Missing required file: {filename}")
            else:
                self._print(f"✓ Found: {filename}")

    def check_readme_sections(self):
        """Verify README contains all required sections."""
        readme_path = self.project_root / "README.md"

        if not readme_path.exists():
            self.errors.append("README.md not found")
            return

        readme_content = readme_path.read_text()

        required_sections = {
            "introduction": r"## Introduction",
            "getting_started": r"## Getting Started",
            "build_and_test": r"## Build and Test",
            "contributing": r"## Contributing",
        }

        for section_name, pattern in required_sections.items():
            if re.search(pattern, readme_content, re.IGNORECASE):
                self._print(f"✓ Found section: {section_name}")
            else:
                self.errors.append(f"❌ Missing README section: {section_name}")

    def check_file_quality(self):
        """Check markdown file quality and formatting."""
        markdown_files = list(self.project_root.glob("*.md"))

        for md_file in markdown_files:
            content = md_file.read_text()

            # Check for empty files
            if len(content.strip()) == 0:
                self.errors.append(f"❌ Empty file: {md_file.name}")
                continue

            # Check for proper markdown headers
            if not re.search(r"^#\s+", content, re.MULTILINE):
                self.warnings.append(f"⚠ No H1 header in: {md_file.name}")

            # Check for valid markdown links
            invalid_links = re.findall(r"\[([^\]]+)\]\(\)", content)
            if invalid_links:
                self.errors.append(f"❌ Invalid markdown links in: {md_file.name}")

            self._print(f"✓ Validated: {md_file.name}")

    def print_report(self):
        """Print validation report."""
        print("\n" + "=" * 60)
        print("Documentation Validation Report")
        print("=" * 60)

        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(f"  {error}")

        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")

        print("\n" + "=" * 60)
        if not self.errors:
            print("✅ All documentation checks passed!")
        else:
            print(f"❌ Validation failed with {len(self.errors)} error(s)")
        print("=" * 60 + "\n")

    def _print(self, message):
        """Print verbose message."""
        print(f"  {message}")


def test_documentation_completeness():
    """Test that all required documentation files are present."""
    validator = DocumentationValidator()
    validator.print_report()
    assert validator.validate(), "Documentation validation failed"


def test_readme_has_introduction():
    """Test that README has Introduction section."""
    readme_path = Path("README.md")
    assert readme_path.exists(), "README.md not found"

    content = readme_path.read_text()
    assert "## Introduction" in content, "Introduction section missing from README"


def test_readme_has_getting_started():
    """Test that README has Getting Started section."""
    readme_path = Path("README.md")
    assert readme_path.exists(), "README.md not found"

    content = readme_path.read_text()
    assert "## Getting Started" in content, "Getting Started section missing from README"


def test_readme_has_build_and_test():
    """Test that README has Build and Test section."""
    readme_path = Path("README.md")
    assert readme_path.exists(), "README.md not found"

    content = readme_path.read_text()
    assert "## Build and Test" in content, "Build and Test section missing from README"


def test_readme_has_contributing():
    """Test that README has Contributing section."""
    readme_path = Path("README.md")
    assert readme_path.exists(), "README.md not found"

    content = readme_path.read_text()
    assert "## Contributing" in content, "Contributing section missing from README"


def test_contributing_file_exists():
    """Test that CONTRIBUTING.md exists."""
    filepath = Path("CONTRIBUTING.md")
    assert filepath.exists(), "CONTRIBUTING.md not found"
    assert len(filepath.read_text()) > 0, "CONTRIBUTING.md is empty"


def test_changelog_file_exists():
    """Test that CHANGELOG.md exists."""
    filepath = Path("CHANGELOG.md")
    assert filepath.exists(), "CHANGELOG.md not found"
    assert len(filepath.read_text()) > 0, "CHANGELOG.md is empty"


def test_architecture_file_exists():
    """Test that ARCHITECTURE.md exists."""
    filepath = Path("ARCHITECTURE.md")
    assert filepath.exists(), "ARCHITECTURE.md not found"
    assert len(filepath.read_text()) > 0, "ARCHITECTURE.md is empty"


def test_support_file_exists():
    """Test that SUPPORT.md exists."""
    filepath = Path("SUPPORT.md")
    assert filepath.exists(), "SUPPORT.md not found"
    assert len(filepath.read_text()) > 0, "SUPPORT.md is empty"


def test_license_file_exists():
    """Test that LICENSE file exists."""
    filepath = Path("LICENSE")
    assert filepath.exists(), "LICENSE file not found"
    assert len(filepath.read_text()) > 0, "LICENSE file is empty"


def test_gitignore_file_exists():
    """Test that .gitignore exists."""
    filepath = Path(".gitignore")
    assert filepath.exists(), ".gitignore file not found"
    assert len(filepath.read_text()) > 0, ".gitignore file is empty"


if __name__ == "__main__":
    validator = DocumentationValidator()
    validator.validate()
    validator.print_report()

    # Exit with appropriate code
    exit(0 if not validator.errors else 1)
