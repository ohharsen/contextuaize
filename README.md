# Contextuaize

**Contextuaize** is a CLI tool designed to streamline "Context Window Engineering." It crawls a local codebase, filters for relevant files (ignoring `node_modules`, `.git`, etc.), and concatenates them into a single, formatted text file. 

This output is optimized for "reinjecting" your project context into Large Language Models like **Claude Opus**, **GPT-4**, or **Gemini** so they can understand your full stack architecture.

## 🚀 Features

- **Smart Filtering:** Automatically ignores system directories (`__pycache__`, `.git`), dependencies (`node_modules`, `venv`), and lockfiles.
- **Multi-Language Support:** Captures Python, JavaScript, TypeScript, React, HTML/CSS, Config files, and Dockerfiles out of the box.
- **LLM-Friendly Format:** Wraps file contents in clear headers so the AI understands file boundaries and paths.
- **CLI based:** Run it from anywhere on your machine.

## 📦 Installation

### Option 1: Development / Local Install
If you have cloned this repository locally and want to modify the code:

```bash
git clone [https://github.com/ohharsen/contextuaize.git](https://github.com/ohharsen/contextuaize.git)
cd contextuaize
pip install -e .