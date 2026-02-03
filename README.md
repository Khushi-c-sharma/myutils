# 🛠️ myutils

> A lightweight, modular Python utility library for common programming tasks

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## 📖 Overview

**myutils** is a collection of reusable Python utilities designed to streamline common development tasks. Built with modern Python best practices, this package provides clean, well-tested modules for authentication, validation, text processing, mathematical operations, and more.

### ✨ Why myutils?

- **🎯 Focused & Modular** - Each module solves a specific problem
- **🔒 Type-Safe** - Built with Pydantic for robust validation
- **📦 Easy Integration** - Simple imports, zero configuration
- **🧪 Production-Ready** - Industry-standard packaging practices
- **🚀 Lightweight** - Minimal dependencies

---

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Module Reference](#-module-reference)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Features

| Module | Description | Use Cases |
|--------|-------------|-----------|
| **🔐 auth** | Password validation & authentication | User registration, security checks |
| **✉️ validation** | Email validation (rule-based & regex) | Form validation, user input |
| **📝 text_ops** | Text processing utilities | Word frequency, string manipulation |
| **🔢 math_ops** | Mathematical operations | Prime checking, number utilities |
| **✅ eligibility** | Logic for eligibility & grading | Academic systems, approval workflows |
| **💾 storage** | Simple data storage helpers | Config management, caching |
| **⚙️ operations** | General-purpose operations | Helper functions, utilities |

---

## 📦 Installation

### From GitHub (Recommended)

```bash
pip install git+https://github.com/Khushi-c-sharma/myutils.git
```

### For Development (Editable Mode)

```bash
# Clone the repository
git clone https://github.com/Khushi-c-sharma/myutils.git
cd myutils

# Install in editable mode
pip install -e .
```

### Requirements

- Python ≥ 3.9
- Pydantic ≥ 2.0

---

## 🚀 Quick Start

### Email Validation

```python
from myutils.validation import RuleBasedEmailUser, RegexEmailUser

# Rule-based validation
user = RuleBasedEmailUser(email="john.doe@example.com")
print(user.email)  # Output: john.doe@example.com

# Regex-based validation
user = RegexEmailUser(email="jane@company.org")
print(user.is_valid)  # Output: True
```

### Password Strength Validation

```python
from myutils.auth import PasswordUser

# Validates password strength requirements
user = PasswordUser(password="SecureP@ssw0rd!")
print(user.is_strong)  # Output: True
```

### Text Processing

```python
from myutils.text_ops.frequency import word_frequency

# Count word occurrences
result = word_frequency("hello world hello python world")
print(result)  # Output: {'hello': 2, 'world': 2, 'python': 1}
```

### Math Utilities

```python
from myutils.math_ops.prime_checker import is_prime

# Check if a number is prime
print(is_prime(17))   # Output: True
print(is_prime(18))   # Output: False
```

---

## 📚 Module Reference

### 🔐 Authentication (`myutils.auth`)

**Classes:**
- `PasswordUser` - Password validation with strength requirements

**Features:**
- Minimum length enforcement
- Special character requirements
- Number and uppercase validation

---

### ✉️ Validation (`myutils.validation`)

**Classes:**
- `RuleBasedEmailUser` - Email validation using custom rules
- `RegexEmailUser` - Email validation using regex patterns

**Features:**
- Domain validation
- Format checking
- Custom validation rules

---

### 📝 Text Operations (`myutils.text_ops`)

**Functions:**
- `word_frequency(text: str) -> dict` - Count word occurrences
- `capitalize_words(text: str) -> str` - Smart capitalization
- `remove_punctuation(text: str) -> str` - Clean text

**Use Cases:**
- NLP preprocessing
- Text analysis
- Data cleaning

---

### 🔢 Math Operations (`myutils.math_ops`)

**Functions:**
- `is_prime(n: int) -> bool` - Prime number checker
- `factorial(n: int) -> int` - Calculate factorial
- `gcd(a: int, b: int) -> int` - Greatest common divisor

**Use Cases:**
- Algorithm implementation
- Mathematical computations
- Number theory problems

---

### ✅ Eligibility (`myutils.eligibility`)

**Functions:**
- `check_grade(score: float) -> str` - Determine letter grade
- `is_eligible(criteria: dict) -> bool` - Evaluate eligibility

**Use Cases:**
- Academic grading systems
- Approval workflows
- Conditional logic

---

### 💾 Storage (`myutils.storage`)

**Classes:**
- `SimpleStorage` - Key-value storage
- `ConfigManager` - Configuration handler

**Features:**
- JSON serialization
- File persistence
- In-memory caching

---

### ⚙️ Operations (`myutils.operations`)

**Functions:**
- `batch_process(items: list, func: callable) -> list`
- `retry_on_failure(func: callable, max_attempts: int)`

**Features:**
- Batch processing
- Error handling
- Retry logic

---

## 🏗️ Project Structure

```
myutils/
├── .github/
│   └── workflows/
│       └── ci.yml                  # CI/CD pipeline (optional)
│
├── src/
│   └── myutils/
│       ├── __init__.py
│       ├── auth/
│       │   ├── __init__.py
│       │   └── password.py
│       ├── validation/
│       │   ├── __init__.py
│       │   ├── rule_based.py
│       │   └── regex_based.py
│       ├── text_ops/
│       │   ├── __init__.py
│       │   └── frequency.py
│       ├── math_ops/
│       │   ├── __init__.py
│       │   └── prime_checker.py
│       ├── eligibility/
│       │   └── __init__.py
│       ├── storage/
│       │   └── __init__.py
│       └── operations/
│           └── __init__.py
│
├── tests/                          # Unit tests (pytest)
│   ├── test_auth.py
│   ├── test_validation.py
│   └── test_text_ops.py
│
├── pyproject.toml                  # Package metadata & dependencies
├── README.md                       # This file
├── LICENSE                         # MIT License
└── .gitignore                      # Git ignore rules
```

### 📐 Design Philosophy

This project follows the **`src/` layout** pattern, which:

- ✅ Prevents accidental local imports
- ✅ Mirrors production package structures
- ✅ Ensures proper package installation
- ✅ Facilitates testing and distribution

---

## 🧪 Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/Khushi-c-sharma/myutils.git
cd myutils

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e .[dev]
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=myutils --cov-report=html

# Run specific test file
pytest tests/test_auth.py
```

### Code Quality

```bash
# Format code
black src/

# Lint code
flake8 src/

# Type checking
mypy src/
```

---

## 🔍 Verification

After installation, verify the package is correctly installed:

```bash
# Check installation
python -c "import myutils; print(myutils.__file__)"

# Expected output (example):
# /path/to/myutils/src/myutils/__init__.py
```

### Using with Jupyter Notebooks

Ensure Jupyter runs in the same environment where `myutils` is installed:

```bash
# Install kernel
python -m ipykernel install --user --name myutils-env

# Launch Jupyter
jupyter notebook
```

Then import normally:

```python
from myutils.validation import RuleBasedEmailUser
```

---

## 🗺️ Roadmap

### v0.2.0 (Planned)
- [ ] Comprehensive test suite (pytest)
- [ ] API documentation (Sphinx)
- [ ] Type stubs for better IDE support
- [ ] Performance benchmarks

### v0.3.0 (Future)
- [ ] Async support for I/O operations
- [ ] CLI tools for common tasks
- [ ] Plugin system for extensibility
- [ ] Integration with popular frameworks

### Long-term
- [ ] Publish to PyPI
- [ ] GitHub Actions CI/CD
- [ ] Pre-commit hooks
- [ ] Contribution guidelines

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add type hints to all functions
- Write tests for new features
- Update documentation as needed
- Keep commits atomic and meaningful

### Code of Conduct

Please be respectful and constructive in all interactions. We're here to build something great together! 🚀

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Khushi Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Acknowledgments

- Built with [Pydantic](https://pydantic-docs.helpmanual.io/) for robust data validation
- Inspired by modern Python packaging best practices
- Thanks to the open-source community

---

## 📬 Contact & Support

**Khushi Sharma**  
Data Science Enthusiast 

- 🐙 GitHub: [@yourusername](https://github.com/Khushi-c-sharma)

---

<div align="center">

### ⭐ Star this repo if you find it useful!

**Made with ❤️ and Python**

[Report Bug](https://github.com/yourusername/myutils/issues) · [Request Feature](https://github.com/yourusername/myutils/issues) · [Documentation](https://github.com/yourusername/myutils/wiki)

</div>
