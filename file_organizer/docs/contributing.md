# Contributing to File Organizer

Thank you for your interest in contributing to File Organizer! This guide will help you get started with setting up your development environment and making contributions.

## Setting Up Development Environment

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   ```
3. Install the package in development mode:
   ```bash
   pip install -e .
   ```
4. Install development dependencies:
   ```bash
   pip install pytest pytest-cov black isort flake8
   ```

## Development Workflow

1. Create a branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes, following the coding standards

3. Run tests to ensure your changes don't break existing functionality:
   ```bash
   pytest
   ```

4. Format your code:
   ```bash
   black file_organizer
   isort file_organizer
   ```

5. Run linting checks:
   ```bash
   flake8 file_organizer
   ```

6. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add feature: your feature description"
   ```

7. Push your branch to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

8. Create a Pull Request from your forked repository to the main repository

## Coding Standards

- Follow PEP 8 style guidelines
- Use descriptive variable names
- Write docstrings for all functions, classes, and methods
- Add type hints where appropriate
- Keep functions focused on a single responsibility

## Adding New Features

### New File Categories

To add support for new file extensions:

1. Update `file_organizer/categories.py` to include the new extensions
2. Add tests for the new categories
3. Update the documentation to reflect the new categories

### New CLI Options

To add new command-line options:

1. Update `file_organizer/main.py` to add the new argument
2. Add the logic to handle the new option
3. Update the documentation

## Testing

We use pytest for testing. To run the test suite:

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=file_organizer
```

### Writing Tests

When adding new features, please include tests that cover:

1. Expected functionality
2. Edge cases
3. Error handling

## Documentation

When making changes, please update the relevant documentation:

- Update docstrings for any modified code
- Update the README.md if the changes affect user-facing functionality
- Update or add to the documentation in the `docs` directory

## Pull Request Process

1. Ensure all tests pass and code is formatted correctly
2. Update documentation to reflect your changes
3. Include a clear description of the changes in your PR
4. Link any related issues in your PR description

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person

Thank you for contributing to File Organizer! 