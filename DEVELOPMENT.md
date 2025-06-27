# Development Guide

This guide is for contributors who want to improve the Python Kata-Machine system.

## Development Setup

```bash
# Clone and build
git clone <repo-url>
cd python-kata-machine
docker-compose up -d --build

# Enter development container
docker-compose exec python-kata bash

# Run tests on the system itself
python -m pytest tests/ -v

# Test the daily workflow
python kata.py daily
python kata.py test
python kata.py complete
```

## Project Architecture

### Core Components

- **kata.py** - Main CLI interface, routes commands to scripts
- **config_loader.py** - Handles configuration loading and validation
- **scripts/daily.py** - Daily practice generator with progress tracking
- **test_runner.py** - Test execution engine for daily practice
- **kata.config.py** - Course progression and configuration

### Daily Practice Flow

1. User runs `python kata.py daily`
2. `scripts/daily.py` reads `.kata_progress.json` 
3. Generates algorithm file for current day in `day{N}/`
4. User implements algorithm
5. `python kata.py test` runs tests via `test_runner.py`
6. `python kata.py complete` advances progress

### Configuration System

- **kata.config.py** - Defines `COURSE_PROGRESSION` list
- **config_loader.py** - Validates and loads configuration
- Compatible with original kata-machine config patterns

## Adding New Features

### Adding a New Algorithm

1. Add algorithm name to `COURSE_PROGRESSION` in `kata.config.py`
2. Create test file in `tests/test_{algorithm}.py` (optional but recommended)
3. Test the daily generation: `python kata.py daily`

### Adding New Commands

1. Add command logic to appropriate script in `scripts/`
2. Update `kata.py` command mapping
3. Update help text in `kata.py`
4. Test with: `python kata.py {new-command}`

### Modifying Test System

- Tests live in `tests/` directory
- `conftest.py` handles algorithm imports and fixtures
- `test_runner.py` executes tests for daily practice
- Tests automatically import from current day directory

## Code Style

```bash
# Format code
black .

# Type checking
mypy *.py scripts/*.py

# Run system tests
python -m pytest tests/ -v
```

## Container Development

- **Dockerfile** - `docker/Dockerfile`
- **Dependencies** - `docker/requirements.txt`
- **Build optimization** - `docker/.dockerignore`

```bash
# Rebuild container after changes
docker-compose down
docker-compose up -d --build

# View container logs
docker-compose logs python-kata
```

## Testing Changes

### Test Daily Workflow
```bash
python kata.py reset          # Start fresh
python kata.py daily          # Generate day 1
cd day1                       # Check generated files
python kata.py test           # Should show test results
python kata.py complete       # Advance to day 2
python kata.py progress       # Check progress tracking
```

### Test Configuration
```bash
python kata.py config         # Validate current config
# Modify kata.config.py
python kata.py config         # Should catch any errors
```

### Test Cleanup
```bash
python kata.py clear          # Clean up practice files
ls                           # Should only show core system files
```

## Release Checklist

- [ ] All system tests pass
- [ ] Daily workflow works end-to-end
- [ ] Configuration validates correctly
- [ ] README is up to date
- [ ] Docker container builds successfully
- [ ] No practice files committed (.gitignore working)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes using development setup above
4. Test thoroughly with daily workflow
5. Submit pull request with clear description

The goal is to maintain a simple, effective daily practice system that helps developers learn algorithms through spaced repetition.
