# Contributing to harry-factory-playground

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the harry-factory-playground project.

## Code of Conduct

This project adheres to a Code of Conduct that all contributors must follow. By participating, you are expected to:
- Be respectful and inclusive
- Provide constructive feedback
- Report any issues through appropriate channels

## Getting Started with Development

### Fork and Clone
```bash
git clone https://github.com/your-org/harry-factory-playground.git
cd harry-factory-playground
```

### Local Development Environment

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install development dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Development Workflow

### Branching Strategy

- **main**: Production-ready code
- **factory/\***: Feature development branches following the factory pattern
- **feature/\***: Feature branches
- **bugfix/\***: Bug fix branches
- **docs/\***: Documentation updates

### Making Changes

1. Create a new branch from `main`
2. Make your changes with clear, logical commits
3. Test thoroughly before submitting
4. Update documentation as needed
5. Submit a pull request

### Commit Message Format

Follow the Conventional Commits specification:

```
type(scope): subject

body

footer
```

Examples:
- `feat(api): add new health endpoint`
- `fix(calculator): correct multiplication function`
- `docs(readme): update getting started section`
- `test(app): add comprehensive test coverage`

### Types
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **test**: Test additions or updates
- **refactor**: Code refactoring
- **perf**: Performance improvements
- **chore**: Build process, dependencies, etc.

## Testing Requirements

All contributions must include appropriate tests:

### Unit Tests
- Write tests for new functions/methods
- Maintain test coverage above 80%
- Use pytest as the testing framework

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_app.py -v
```

### Test Structure
```
tests/
├── test_app.py
├── test_calculator.py
└── conftest.py
```

## Code Style and Quality

### Python Standards
- Follow [PEP 8](https://pep8.org/) guidelines
- Use meaningful variable and function names
- Include docstrings for all public functions

### Formatting
```bash
# Auto-format with Black
black .

# Lint with Flake8
flake8 . --max-line-length=120

# Type checking
mypy .
```

### Pre-commit Hooks (Optional)
```bash
pip install pre-commit
pre-commit install
```

## Documentation

- Update README.md for user-facing changes
- Add docstrings to all public APIs
- Update CHANGELOG.md for significant changes
- Include examples for new features

### Documentation Structure
- **README.md**: Overview and getting started
- **CONTRIBUTING.md**: Contribution guidelines (this file)
- **CHANGELOG.md**: Version history and changes
- **docs/**: Detailed technical documentation

## Pull Request Process

1. Update documentation and tests
2. Ensure all tests pass locally
3. Push to your fork and create a pull request
4. Fill in the PR template completely
5. Link related issues (if any)
6. Address review comments

### PR Title Format
Use the same format as commit messages:
- `feat: add new status page feature`
- `fix: resolve version endpoint bug`
- `docs: improve getting started guide`

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
Describe how changes were tested

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Review Process

All pull requests will be reviewed for:
- Code quality and style
- Test coverage
- Documentation completeness
- Alignment with project goals

Reviewers may request changes. This is a normal part of the process.

## Becoming a Maintainer

Consistent contributors may be invited to become maintainers. This includes:
- Code review responsibilities
- Release management
- Community support

## Questions?

- Create a discussion in the repository
- Check existing issues and discussions
- Contact the maintainers directly

## Thank You!

Your contributions help make this project better. Thank you for your time and effort!
