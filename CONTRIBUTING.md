# Contributing to Sound AImagination

Thank you for your interest in contributing to Sound AImagination! This document provides guidelines for contributing to the project.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/sound-aimagination.git
   cd sound-aimagination
   ```
3. **Set up the development environment**:
   ```bash
   setup.bat
   ```

## 🔧 Development Setup

- Python 3.13 or higher
- Virtual environment (`.venv/`)
- All dependencies from `requirements.txt`
- LM Studio for testing prompt generation

## 📝 Coding Guidelines

### Python Style
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose

### Code Structure
```python
"""
Module docstring explaining purpose.
"""

import standard_library
import third_party
from local_module import LocalClass


class MyClass:
    """Class docstring."""
    
    def __init__(self):
        """Initialize the class."""
        pass
    
    def my_method(self, param):
        """
        Method docstring.
        
        Args:
            param (type): Description
            
        Returns:
            type: Description
        """
        pass
```

## 🎯 What to Contribute

### Bug Fixes
- Check existing issues before creating new ones
- Describe the bug clearly with steps to reproduce
- Include system information (OS, Python version, etc.)

### New Features
- Open an issue first to discuss the feature
- Explain the use case and benefits
- Consider backward compatibility

### Documentation
- Fix typos and improve clarity
- Add examples and use cases
- Update README for new features

### Performance Improvements
- Profile code before and after changes
- Document performance gains
- Ensure no functionality breaks

## 🔀 Pull Request Process

1. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes** with clear, logical commits:
   ```bash
   git commit -m "Add amazing feature"
   ```

3. **Test thoroughly**:
   - Test with GUI
   - Test with command line
   - Verify all features still work

4. **Push to your fork**:
   ```bash
   git push origin feature/amazing-feature
   ```

5. **Open a Pull Request**:
   - Clear title describing the change
   - Detailed description of what and why
   - Reference any related issues
   - Include screenshots if UI changes

## ✅ Testing

Before submitting:
- [ ] Code runs without errors
- [ ] GUI launches and works correctly
- [ ] Audio recording functions properly
- [ ] Image generation completes successfully
- [ ] No new warnings or errors in console
- [ ] Documentation updated if needed

## 📦 Commit Messages

Use clear, descriptive commit messages:

**Good:**
- `Add timeline visualization to results screen`
- `Fix audio buffer overflow on long recordings`
- `Improve LM Studio error handling`

**Bad:**
- `Update file`
- `Fix bug`
- `Changes`

## 🐛 Reporting Bugs

Include:
- **Description**: What happened vs. what you expected
- **Steps to Reproduce**: Numbered list of exact steps
- **Environment**: OS, Python version, GPU info
- **Logs**: Console output or error messages
- **Screenshots**: If UI-related

## 💡 Suggesting Features

Include:
- **Use Case**: Why is this feature needed?
- **Expected Behavior**: What should it do?
- **Alternatives**: Other solutions you considered
- **Examples**: Similar features in other apps

## 📄 Documentation

- Update README.md for user-facing changes
- Add inline comments for complex logic
- Update docstrings when changing functions
- Keep code examples current

## 🙏 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Give credit where due
- Keep discussions professional

## 📞 Questions?

- Open an issue with the "question" label
- Check existing issues first
- Be specific about your question

---

Thank you for contributing to Sound AImagination! 🎵✨
