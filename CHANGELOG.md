# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project documentation with README, CONTRIBUTING, and CHANGELOG

### Changed
- Project structure and documentation organization

### Fixed
- Documentation clarity and completeness

## [0.1.0] - 2026-06-22

### Added
- Initial playground repository setup
- Version endpoint (`GET /version`)
- Health check endpoint (`GET /health`) with version and uptime metrics
- Status page endpoint (`GET /status`)
- Calculator module with basic arithmetic operations
- Python project configuration and dependencies
- Comprehensive documentation

### Infrastructure
- GitHub Actions CI/CD configuration
- Test suite with pytest
- Code quality tools (Black, Flake8, mypy)
- .gitignore for Python projects

## Guidelines for Future Releases

### Version Numbering
- **MAJOR**: Incompatible API changes
- **MINOR**: Backwards-compatible new features
- **PATCH**: Backwards-compatible bug fixes

### Release Process
1. Update version in setup.py and __init__.py
2. Update CHANGELOG.md with changes
3. Create git tag: `git tag vX.Y.Z`
4. Create GitHub release with changelog notes
5. Publish to package repository (if applicable)

### Supported Python Versions
- Python 3.8+
- Python 3.9+
- Python 3.10+
- Python 3.11+
- Python 3.12+
