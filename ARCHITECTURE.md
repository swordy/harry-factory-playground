# Architecture

## Project Structure

```
harry-factory-playground/
├── README.md                 # Main project documentation
├── CONTRIBUTING.md           # Contribution guidelines
├── CHANGELOG.md             # Version history
├── LICENSE                  # Project license
├── ARCHITECTURE.md          # This file
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
├── requirements-dev.txt    # Development dependencies
├── setup.py               # Package configuration
├── app.py                # Main application entry point
├── calculator/            # Calculator module
│   ├── __init__.py
│   └── operations.py
├── tests/                 # Test suite
│   ├── conftest.py       # Pytest configuration
│   ├── test_app.py       # Application tests
│   └── test_calculator.py # Calculator tests
├── .github/               # GitHub specific files
│   └── workflows/         # CI/CD workflows
│       ├── test.yml       # Test workflow
│       └── deploy.yml     # Deployment workflow
└── docs/                  # Additional documentation
    ├── api.md            # API documentation
    ├── deployment.md     # Deployment guide
    └── troubleshooting.md # Troubleshooting guide
```

## Core Components

### 1. Main Application (`app.py`)

The Flask/FastAPI application entry point that serves HTTP endpoints:
- **Version Endpoint**: `GET /version` — Returns git short SHA
- **Health Endpoint**: `GET /health` — Returns version and uptime metrics
- **Status Endpoint**: `GET /status` — Returns current system status

### 2. Calculator Module (`calculator/`)

Provides basic arithmetic operations:
- Addition
- Multiplication
- Subtraction
- Division

Used to demonstrate modular architecture and reusable components.

### 3. Test Suite (`tests/`)

Comprehensive test coverage using pytest:
- Unit tests for calculator operations
- Integration tests for HTTP endpoints
- Fixture and configuration in conftest.py

### 4. CI/CD Workflows (`.github/workflows/`)

Automated workflows for:
- Running tests on push and pull requests
- Building and deploying releases
- Code quality checks

## Design Principles

### Modularity
- Separate concerns into distinct modules
- Reusable components (calculator module)
- Clear interfaces between components

### Testability
- Comprehensive test coverage
- Isolated unit tests
- Integration test examples

### Documentation
- Inline code documentation via docstrings
- README with quick start guide
- Contribution guidelines
- API documentation

### Factory Pattern
- Leverages factory-driven development
- Structured branching strategy
- Automated code review and testing

## Dependency Management

### Runtime Dependencies
- **Flask/FastAPI**: Web framework
- **Python 3.8+**: Core runtime

### Development Dependencies
- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **black**: Code formatting
- **flake8**: Linting
- **mypy**: Type checking
- **pre-commit**: Git hooks

## API Endpoints

### GET /version
Returns the current version (git short SHA):
```json
{
  "version": "abc1234"
}
```

### GET /health
Returns health metrics:
```json
{
  "status": "healthy",
  "version": "abc1234",
  "uptime_seconds": 3600
}
```

### GET /status
Returns detailed status information:
```json
{
  "application": "healthy",
  "dependencies": "healthy",
  "timestamp": "2026-06-22T10:00:00Z"
}
```

## Development Workflow

### Local Development
1. Create virtual environment
2. Install dependencies
3. Run application with `python app.py`
4. Access at `http://localhost:5000`

### Testing
1. Write tests in `tests/` directory
2. Run `pytest` to execute
3. Check coverage with `pytest --cov`

### Code Review
1. Follow commit message conventions
2. Ensure tests pass
3. Request review on pull request
4. Address feedback

## Deployment

### Environment Configuration
- Environment variables for configuration
- Separate configs for dev/staging/prod
- Secure credential management

### Containerization (Optional)
- Dockerfile for container deployment
- Docker Compose for local development
- Registry integration for CI/CD

## Security Considerations

- Input validation on all endpoints
- Secure dependency management
- Regular security audits
- Responsible disclosure policy

## Performance Considerations

- Efficient endpoint routing
- Minimal dependencies
- Database query optimization (if applicable)
- Caching strategies

## Monitoring and Logging

- Health check endpoint for uptime monitoring
- Structured logging for debugging
- Error tracking and reporting
- Metrics collection

## Future Enhancements

- Database integration
- Authentication and authorization
- Advanced calculator operations
- Comprehensive metrics and monitoring
- Mobile API support
- WebSocket support for real-time updates
