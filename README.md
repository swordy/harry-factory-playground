# harry-factory-playground

> Playground repository for the Harry SDLC factory — a comprehensive testing and development environment for continuous integration and delivery workflows.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Build and Test](#build-and-test)
- [Contributing](#contributing)

---

## Introduction

The **harry-factory-playground** repository serves as a dedicated playground environment for the Harry SDLC factory framework. This repository is designed to:

- **Demonstrate** core functionality and best practices for SDLC automation
- **Enable experimentation** with factory-based development workflows
- **Provide a testbed** for validating CI/CD pipeline configurations
- **Showcase examples** of modern development practices including version management, health monitoring, and status endpoints

### Project Goals

This project enables development teams to:
1. Understand the principles of factory-driven software development
2. Test integration patterns in a controlled environment
3. Develop and validate automated workflows
4. Explore modular development patterns (e.g., calculator modules, version endpoints)

### Key Features

- **Version Tracking**: Exposes current version information via dedicated endpoints
- **Health Monitoring**: Provides health and uptime metrics for monitoring
- **Status Dashboard**: Offers real-time status visibility
- **Modular Architecture**: Organized into reusable components

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python** 3.8 or higher
- **Git** 2.20 or higher
- **pip** (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-org/harry-factory-playground.git
   cd harry-factory-playground
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the development server**:
   ```bash
   python app.py
   ```
   The application will be available at `http://localhost:5000`

2. **Access key endpoints**:
   - **Version Info**: `GET /version` — Returns current git short SHA
   - **Health Check**: `GET /health` — Returns version and uptime metrics
   - **Status Page**: `GET /status` — Displays current system status

### Quick Test

Verify the installation with a quick test:
```bash
curl http://localhost:5000/version
curl http://localhost:5000/health
```

---

## Build and Test

### Running Tests

The project uses **pytest** for unit testing. To run the test suite:

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_app.py

# Run with coverage report
pytest --cov=. --cov-report=html
```

### Building the Project

#### Local Build

For development builds:
```bash
python setup.py develop
```

#### Production Build

Create a distribution package:
```bash
python setup.py sdist bdist_wheel
```

### Code Quality

Maintain code quality standards:
```bash
# Format code with Black
black .

# Lint with Flake8
flake8 .

# Type checking with mypy
mypy .
```

### Continuous Integration

The project uses GitHub Actions for automated testing and deployment. CI workflows are triggered on:
- Push to `main` or `factory/*` branches
- Pull requests
- Manual dispatch via workflow_dispatch

View workflows in `.github/workflows/` directory.

### Build Artifacts

- **Distribution packages**: `dist/`
- **Test coverage reports**: `htmlcov/`
- **Python cache**: `__pycache__/` (excluded via `.gitignore`)

---

## Contributing

### Contribution Process

We follow a structured contribution workflow:

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Implement your changes**:
   - Write clean, readable code
   - Include docstrings and comments
   - Follow the existing code style

3. **Test your changes**:
   ```bash
   pytest
   ```

4. **Commit your changes** with descriptive messages:
   ```bash
   git commit -m "feat: add new feature description"
   ```

5. **Push and open a Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Review and Merge**:
   - Address code review feedback
   - Ensure CI checks pass
   - Merge to `main` once approved

### Code Standards

- **Python Style**: Follow [PEP 8](https://pep8.org/) guidelines
- **Testing**: Maintain test coverage above 80%
- **Documentation**: Update README and inline documentation
- **Commit Messages**: Use conventional commits (feat:, fix:, docs:, etc.)

### Reporting Issues

Found a bug? Please:
1. Check if it's already reported in [Issues](https://github.com/your-org/harry-factory-playground/issues)
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs. actual behavior
   - Environment details

### Development Setup

For contributors looking to set up a full development environment:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Setup pre-commit hooks (optional)
pre-commit install

# Run the full test suite
pytest --cov
```

### Release Process

Releases follow semantic versioning (MAJOR.MINOR.PATCH):
1. Update version in `__init__.py` or `setup.py`
2. Update CHANGELOG.md
3. Create a git tag: `git tag v1.2.3`
4. Push tag: `git push origin v1.2.3`
5. Create a GitHub release with notes

---

## Additional Resources

- **Factory Documentation**: See project wiki or docs/ directory
- **API Reference**: Inline code documentation via docstrings
- **Issue Tracking**: [GitHub Issues](https://github.com/your-org/harry-factory-playground/issues)
- **License**: See LICENSE file

---

## Maintenance and Support

This repository is actively maintained. For support:
- Open an issue for bug reports
- Use discussions for questions and suggestions
- See CONTRIBUTING.md for detailed guidelines

**Last Updated**: 2026-06-22
