import streamlit as st
import zipfile
import io
import os

st.set_page_config(page_title="patternscope Package", layout="wide")

st.title("patternscope - PyPI-Ready Python Package")
st.markdown("A tiny (<200 lines) CSV pattern-analysis tool ready for GitHub and PyPI upload.")

PACKAGE_DIR = "patternscope"

PACKAGE_FILES = [
    "patternscope/__init__.py",
    "patternscope/core.py",
    "patternscope/metrics.py",
    "patternscope/visualize.py",
    "tests/test_core.py",
    "tests/test_metrics.py",
    "README.md",
    "pyproject.toml",
    "LICENSE",
]

st.header("Package Structure")
st.code("""patternscope/
├── patternscope/
│   ├── __init__.py
│   ├── core.py
│   ├── metrics.py
│   └── visualize.py
├── tests/
│   ├── test_core.py
│   └── test_metrics.py
├── README.md
├── pyproject.toml
└── LICENSE""", language="text")

st.header("Download Clean Package")
st.markdown("Download a ZIP file containing **only** the files needed for PyPI - no `.replit`, no `__pycache__`, no virtual environment files.")

def create_clean_zip():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in PACKAGE_FILES:
            full_path = os.path.join(PACKAGE_DIR, file_path)
            if os.path.exists(full_path):
                zf.write(full_path, os.path.join("patternscope", file_path))
    buffer.seek(0)
    return buffer

zip_buffer = create_clean_zip()

st.download_button(
    label="Download patternscope.zip",
    data=zip_buffer,
    file_name="patternscope.zip",
    mime="application/zip"
)

st.header("File Contents")

tabs = st.tabs(["__init__.py", "core.py", "metrics.py", "visualize.py", "pyproject.toml", "README.md", "LICENSE"])

file_map = {
    0: "patternscope/__init__.py",
    1: "patternscope/core.py",
    2: "patternscope/metrics.py",
    3: "patternscope/visualize.py",
    4: "pyproject.toml",
    5: "README.md",
    6: "LICENSE",
}

for i, tab in enumerate(tabs):
    with tab:
        file_path = os.path.join(PACKAGE_DIR, file_map[i])
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read()
            lang = "python" if file_path.endswith(".py") else "toml" if file_path.endswith(".toml") else "markdown" if file_path.endswith(".md") else "text"
            st.code(content, language=lang)
        else:
            st.error(f"File not found: {file_path}")

st.header("Next Steps")
st.markdown("""
1. **Download** the ZIP file above
2. **Extract** it to your local machine
3. **Push to GitHub**: `git init && git add . && git commit -m "Initial commit" && git push`
4. **Upload to PyPI**:
   ```bash
   pip install build twine
   python -m build
   twine upload dist/*
   ```
""")
