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
```

### Option 2: Install directly from GitHub
To install it on any machine without cloning the repo manually:

```bash
pip install git+[https://github.com/ohharsen/contextuaize.git](https://github.com/ohharsen/contextuaize.git)
```

## 🛠 Usage

Once installed, the command `contextuaize` is available globally in your terminal.

### 1. Basic Usage
Navigate to the root of the project you want to capture and run:

```bash
contextuaize
```
*This will generate `codebase_context.txt` in the current directory.*

### 2. Specifying Paths and Output
You can point to a specific directory and customize the output filename:

```bash
# Scan a specific project folder and save the output to your Desktop
contextuaize /Users/arsen/my-react-project -o ~/Desktop/full_context.txt
```

### 3. Usage with LLMs
1. Run the tool.
2. Upload the resulting `.txt` file to Claude/ChatGPT.
3. Use a prompt like:
   > "I have attached a snapshot of my full-stack codebase. Please parse this to understand the current architecture, component structure, and backend logic. Wait for my next instruction."

## ⚙️ Configuration

Currently, the ignored directories and included file extensions are defined in `src/contextuaize.py`. 

To add custom file extensions (e.g., `.rust`, `.go`), edit the `INCLUDE_EXTENSIONS` set in the source code:

```python
INCLUDE_EXTENSIONS = {
    '.py', '.js', '.tsx', ... # Add your extensions here
}
```

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---
**Author:** Arsen Ohanyan  
[GitHub Profile](https://github.com/ohharsen)