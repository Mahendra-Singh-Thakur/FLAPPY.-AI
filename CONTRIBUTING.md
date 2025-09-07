# Contributing to FlappyBird AI

First off, thank you for considering contributing to FlappyBird AI! It's people like you that make FlappyBird AI such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed and expected**
* **Include screenshots if possible**
* **Include your environment details** (OS, Python version, PyTorch version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a detailed description of the suggested enhancement**
* **Provide specific examples to demonstrate the enhancement**
* **Describe the current behavior and expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the style guidelines
6. Issue that pull request!

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/flappy-bird-ai.git
   cd flappy-bird-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

## Style Guidelines

### Python Style Guide

We use [Black](https://github.com/psf/black) for code formatting and [isort](https://github.com/PyCQA/isort) for import sorting.

```bash
# Format your code
black src/ tests/

# Sort imports
isort src/ tests/

# Check code style
flake8 src/ tests/

# Type checking
mypy src/
```

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Use conventional commits format:
  * `feat:` for new features
  * `fix:` for bug fixes
  * `docs:` for documentation changes
  * `style:` for formatting changes
  * `refactor:` for code refactoring
  * `test:` for adding tests
  * `chore:` for maintenance tasks

### Documentation

* Use docstrings for all public modules, functions, classes, and methods
* Follow [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) for docstrings
* Update the README.md if needed
* Comment your code where necessary

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_dqn_agent.py

# Run with verbose output
pytest -v
```

### Writing Tests

* Write tests for any new functionality
* Ensure all tests pass before submitting PR
* Aim for high test coverage (>80%)
* Use meaningful test names that describe what is being tested

## Project Structure

```
src/
├── ai/           # AI/ML code (keep separate from game logic)
├── entities/     # Game entities (keep game logic here)
├── utils/        # Utility functions
└── flappy.py     # Main game file

tests/
├── test_ai/      # Tests for AI components
├── test_entities/# Tests for game entities
└── test_utils/   # Tests for utilities
```

## Performance Guidelines

* Profile your code if adding computationally intensive features
* Optimize training loops for speed
* Use vectorized operations where possible
* Consider memory usage for large-scale training

## Documentation Guidelines

* Update docstrings for any modified functions
* Include type hints for function parameters
* Update README.md for significant changes
* Add examples for complex features

## Review Process

1. **Automated checks** - All CI tests must pass
2. **Code review** - At least one maintainer review required
3. **Documentation** - Ensure docs are updated
4. **Testing** - New features must include tests

## Questions?

Feel free to open an issue with the tag `question` if you have any questions about contributing!

## Recognition

Contributors will be recognized in our README.md file. Thank you for your contributions!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
