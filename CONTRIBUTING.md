# Contributing to Agentic AI Patterns

Thank you for your interest in contributing to this educational project! 🎉

## 🎯 Project Purpose

This is an **educational project** created for the .NET Conf 2025 presentation. The goal is to help developers learn about agentic design patterns through practical, runnable examples.

## 🤝 How to Contribute

### Ways to Contribute

1. **Improve Documentation**
   - Fix typos or unclear explanations
   - Add more examples or use cases
   - Translate documentation
   - Add diagrams or visualizations

2. **Enhance Demos**
   - Improve UI/UX
   - Add error handling
   - Optimize performance
   - Add new features

3. **Add New Patterns**
   - Implement additional agentic patterns
   - Create new demo scenarios
   - Build integration examples

4. **Share Your Experience**
   - Report bugs or issues
   - Suggest improvements
   - Share your own implementations
   - Provide feedback

## 📝 Contribution Guidelines

### Before You Start

1. **Check existing issues** - Someone might already be working on it
2. **Open an issue first** - Discuss major changes before implementing
3. **Keep it educational** - Focus on learning value
4. **Maintain simplicity** - Code should be easy to understand

### Code Standards

**Python Style:**
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

**Documentation:**
- Clear and concise
- Include examples
- Explain the "why" not just the "what"
- Use proper markdown formatting

**Demos:**
- Should run out of the box
- Include clear instructions
- Provide example scenarios
- Show visual feedback

### Making Changes

1. **Fork the repository**
   ```bash
   git clone <your-fork-url>
   cd prototype
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clear, documented code
   - Test thoroughly
   - Update relevant documentation

4. **Test your changes**
   ```bash
   # Activate virtual environment
   .\venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Test the demo
   streamlit run your_demo.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Describe what you changed and why
   - Reference any related issues
   - Include screenshots if UI changes

## 🐛 Reporting Bugs

### Before Reporting

1. Check if the issue already exists
2. Try the troubleshooting guides
3. Verify your environment setup

### Bug Report Template

```markdown
**Description:**
Brief description of the bug

**Steps to Reproduce:**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- OS: [e.g., Windows 11]
- Python version: [e.g., 3.11]
- Streamlit version: [e.g., 1.29.0]
- Azure OpenAI model: [e.g., gpt-4]

**Screenshots:**
If applicable

**Additional Context:**
Any other relevant information
```

## 💡 Suggesting Enhancements

### Enhancement Template

```markdown
**Feature Description:**
What feature would you like to see?

**Use Case:**
Why is this feature useful?

**Proposed Implementation:**
How might this work?

**Alternatives Considered:**
Other approaches you've thought about

**Additional Context:**
Any other relevant information
```

## 📚 Adding New Demos

If you want to add a new demo:

1. **Choose a pattern** - Focus on one agentic pattern
2. **Create the demo file** - `demo5_your_pattern.py`
3. **Write documentation** - `DEMO5_README.md`
4. **Add to launcher** - Update `DEMO_LAUNCHER.md`
5. **Update main README** - Add to demo list
6. **Test thoroughly** - Ensure it runs smoothly

### Demo Template

```python
"""
Demo X: Pattern Name
Brief Description

This demo showcases:
- Key feature 1
- Key feature 2
- Key feature 3
"""

import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAI

load_dotenv()

st.set_page_config(
    page_title="Demo X: Pattern Name",
    page_icon="🎯",
    layout="wide"
)

# Your implementation here
```

## 🎨 UI/UX Guidelines

### Streamlit Best Practices

- Use clear, descriptive titles
- Provide example buttons for quick testing
- Show progress indicators for long operations
- Display results in expandable sections
- Use consistent icons and colors
- Add helpful tooltips and explanations

### Visual Consistency

- Follow the existing color scheme
- Use emojis consistently
- Maintain similar layout patterns
- Keep UI clean and uncluttered

## 🧪 Testing

### Manual Testing Checklist

- [ ] Demo runs without errors
- [ ] All buttons work as expected
- [ ] Example scenarios produce good results
- [ ] Error messages are helpful
- [ ] UI is responsive
- [ ] Documentation is accurate

### Edge Cases to Test

- Empty inputs
- Very long inputs
- Invalid configurations
- Network errors
- API rate limits

## 📖 Documentation Standards

### README Structure

1. **Clear title and description**
2. **What it demonstrates**
3. **How to run it**
4. **Key features**
5. **Customization options**
6. **Troubleshooting**

### Code Comments

```python
# Good: Explains why
# Use lower temperature for more factual responses
temperature = 0.3

# Bad: States the obvious
# Set temperature to 0.3
temperature = 0.3
```

## 🔒 Security

### Important Rules

- **Never commit API keys** - Use `.env` files
- **Don't include credentials** - Even in examples
- **Sanitize user input** - Prevent injection attacks
- **Validate configurations** - Check before using

### .gitignore

Ensure these are ignored:
```
.env
*.key
*.secret
venv/
__pycache__/
```

## 📦 Dependencies

### Adding New Dependencies

1. **Justify the need** - Why is this package necessary?
2. **Check compatibility** - Works with Python 3.8+
3. **Update requirements.txt** - Add with version
4. **Document usage** - Explain in README

### Version Pinning

```
# Prefer minimum version
package>=1.0.0

# Pin exact version only if necessary
critical-package==2.3.1
```

## 🎓 Educational Focus

Remember, this is a **learning project**. Contributions should:

- **Teach concepts** - Not just add features
- **Be accessible** - Beginners should understand
- **Show best practices** - Demonstrate good patterns
- **Include explanations** - Why, not just how

## 🌟 Recognition

Contributors will be:
- Listed in CHANGELOG.md
- Mentioned in release notes
- Credited in documentation

## 📞 Questions?

- Open an issue for questions
- Tag with "question" label
- Be specific about what you need help with

## 🙏 Thank You!

Every contribution, no matter how small, helps make this project better for learners worldwide. Thank you for being part of this educational journey! 🚀

---

**Happy Contributing!** 💻✨
