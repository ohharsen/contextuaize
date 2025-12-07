import os
import fnmatch

# Configuration
# ------------------------------------------------------------------------------
# The root directory to scan ('.' means current directory)
ROOT_DIR = '.' 

# The output file name
OUTPUT_FILE = 'codebase_context.txt'

# File extensions to include (add more as needed)
INCLUDE_EXTENSIONS = {
    # Backend
    '.py', '.ini', '.toml', '.env.example', 
    # Frontend
    '.js', '.jsx', '.ts', '.tsx', '.css', '.json', '.html',
    # Config/Docs
    '.md', '.yml', '.yaml', 'Dockerfile'
}

# Directories to always ignore
IGNORE_DIRS = {
    'node_modules', 'venv', '.venv', '__pycache__', '.git', 
    'dist', 'build', 'coverage', '.idea', '.vscode'
}

# Specific files to ignore
IGNORE_FILES = {
    'package-lock.json', 'yarn.lock', '.DS_Store', OUTPUT_FILE
}

# ------------------------------------------------------------------------------

def is_ignored(path, names):
    """
    Returns a list of names to ignore from the current directory `path`
    so os.walk knows to skip them.
    """
    ignored = set()
    for name in names:
        if name in IGNORE_DIRS or name in IGNORE_FILES:
            ignored.add(name)
    return list(ignored)

def get_file_content(filepath):
    """
    Reads file content with error handling for encoding issues.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # Fallback for some windows files or mixed encoding
        try:
            with open(filepath, 'r', encoding='latin-1') as f:
                return f.read()
        except Exception:
            return "[Error: Could not decode file]"
    except Exception as e:
        return f"[Error reading file: {e}]"

def main():
    print(f"🚀 Starting codebase crawl from: {os.path.abspath(ROOT_DIR)}")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        # Write a header for the LLM
        outfile.write("PROJECT CONTEXT SNAPSHOT\n")
        outfile.write("========================\n\n")
        
        file_count = 0
        
        for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
            # Modify dirnames in-place to skip ignored directories
            dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
            
            for filename in filenames:
                if filename in IGNORE_FILES:
                    continue
                
                _, ext = os.path.splitext(filename)
                
                # Check if we should include this file
                if ext in INCLUDE_EXTENSIONS or filename in INCLUDE_EXTENSIONS:
                    full_path = os.path.join(dirpath, filename)
                    relative_path = os.path.relpath(full_path, ROOT_DIR)
                    
                    print(f"Processing: {relative_path}")
                    
                    content = get_file_content(full_path)
                    
                    # FORMATTING FOR LLM
                    # We wrap the content in XML-style tags or Markdown blocks
                    # to help the LLM distinguish files.
                    outfile.write(f"--- START FILE: {relative_path} ---\n")
                    outfile.write(content)
                    outfile.write(f"\n--- END FILE: {relative_path} ---\n\n")
                    
                    file_count += 1

    print(f"\n✅ Done! Concatenated {file_count} files into '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()