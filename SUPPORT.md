# Support and Troubleshooting

This document provides guidance for getting support and troubleshooting common issues with harry-factory-playground.

## Getting Help

### Documentation
- Start with [README.md](README.md) for setup and basic usage
- Check [CONTRIBUTING.md](CONTRIBUTING.md) for development setup
- Review [ARCHITECTURE.md](ARCHITECTURE.md) for system design
- See [CHANGELOG.md](CHANGELOG.md) for version history

### Community Support
- **GitHub Issues**: Report bugs or request features
- **GitHub Discussions**: Ask questions and discuss ideas
- **Documentation Wiki**: Additional resources and guides

## Common Issues and Solutions

### Installation Issues

#### Problem: "Module not found" errors after installation
**Solution:**
1. Ensure virtual environment is activated: `source venv/bin/activate`
2. Verify Python version: `python --version` (requires 3.8+)
3. Reinstall dependencies: `pip install --upgrade -r requirements.txt`

#### Problem: pip install fails with permission error
**Solution:**
1. Ensure using virtual environment (avoid system Python)
2. Never use `sudo pip`
3. Use `pip install --user` if system installation needed

### Runtime Issues

#### Problem: Application won't start
**Checklist:**
1. Verify Python installation: `python --version`
2. Activate virtual environment: `source venv/bin/activate`
3. Check port availability (default: 5000)
4. Review error messages carefully
5. Check logs in application output

#### Problem: Port 5000 already in use
**Solution:**
```bash
# On Linux/Mac
lsof -i :5000
kill -9 <PID>

# Or use a different port
python app.py --port 8000
```

#### Problem: Module import errors
**Solution:**
1. Verify current directory: `pwd` should be project root
2. Check Python path: `python -c "import sys; print(sys.path)"`
3. Reinstall package in development mode: `pip install -e .`

### Testing Issues

#### Problem: Tests fail locally
**Checklist:**
1. Ensure all dependencies installed: `pip install -r requirements-dev.txt`
2. Run tests from project root: `cd harry-factory-playground && pytest`
3. Check Python version compatibility
4. Review test output for specific errors

#### Problem: Coverage report not generated
**Solution:**
```bash
pip install pytest-cov
pytest --cov=. --cov-report=html
```

### Code Quality Issues

#### Problem: Linting errors
**Solution:**
```bash
# Install linting tools
pip install flake8 black mypy

# Auto-fix with Black
black .

# Check with Flake8
flake8 .

# Type check
mypy .
```

## Debugging

### Enable Debug Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Use a Debugger
```bash
# Install debugger
pip install ipdb

# Use in code
import ipdb; ipdb.set_trace()
```

### Print Debugging
```python
print(f"DEBUG: variable_name = {variable_name}")
```

## Performance Issues

### Slow Application Startup
- Check disk I/O
- Review dependency loading
- Profile with: `python -m cProfile app.py`

### High Memory Usage
- Check for memory leaks
- Profile with: `pip install memory-profiler`
- Use: `python -m memory_profiler app.py`

## Reporting Issues

### Before Reporting
1. Check if issue already exists on [GitHub Issues](https://github.com/your-org/harry-factory-playground/issues)
2. Try reproducing with latest code
3. Gather system information

### Creating a Report
Include:
1. **Clear title**: Briefly describe the issue
2. **Description**: What were you trying to do?
3. **Steps to reproduce**: Exact steps to reproduce
4. **Expected behavior**: What should happen?
5. **Actual behavior**: What actually happened?
6. **Environment**:
   - OS (Linux/Mac/Windows)
   - Python version
   - Output of `pip freeze` or `requirements.txt`
7. **Error messages/logs**: Full error output
8. **Screenshots**: If visually relevant

### Security Issues
For security vulnerabilities:
1. **DO NOT** open a public issue
2. Contact maintainers privately
3. Use responsible disclosure process
4. Allow time for patch before public disclosure

## Updating

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Check for Updates
```bash
git fetch origin
git log --oneline origin/main..HEAD
```

### Update to Latest Release
```bash
git pull origin main
pip install --upgrade -r requirements.txt
pytest  # Verify everything works
```

## Uninstalling

### Remove the Project
```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf venv/

# Or completely remove the directory
rm -rf harry-factory-playground/
```

## Getting More Help

### Check Logs
```bash
# Application logs (if applicable)
tail -f logs/app.log

# System logs
dmesg | tail  # Linux
log stream --predicate 'process == "python"'  # macOS
```

### Ask for Help
1. Check [existing discussions](https://github.com/your-org/harry-factory-playground/discussions)
2. Create a new discussion with your question
3. Provide context and what you've already tried
4. Be patient and polite

### Contact Maintainers
- Look for MAINTAINERS file
- Check project website
- Email via GitHub profile

## Additional Resources

- [Python Documentation](https://docs.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [Flask Documentation](https://flask.palletsprojects.com/) (if using Flask)
- [GitHub Help](https://help.github.com/)

---

**Note**: Always check for updates and ensure you're running the latest stable version before reporting issues.

Last updated: 2026-06-22
