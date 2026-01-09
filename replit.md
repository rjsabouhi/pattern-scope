# patternscope Package Generator

## Overview
This project contains a clean, standalone Python package called `patternscope` that is ready for PyPI upload. The package provides CSV pattern analysis capabilities including monotonicity scoring, outlier detection, and inflection point estimation.

## Project Structure
```
.
├── app.py                    # Streamlit app for viewing/downloading the package
├── patternscope/             # The clean PyPI-ready package
│   ├── patternscope/         # Package source code
│   │   ├── __init__.py
│   │   ├── core.py           # Main analyze() function
│   │   ├── metrics.py        # monotonic_score, outlier_score, inflection_points
│   │   └── visualize.py      # plot_patterns function
│   ├── tests/                # Test files
│   │   ├── test_core.py
│   │   └── test_metrics.py
│   ├── README.md
│   ├── pyproject.toml
│   └── LICENSE               # MIT License
└── .streamlit/config.toml    # Streamlit server config
```

## The patternscope Package
The package analyzes numerical columns in CSV files and computes:
- **Monotonicity score**: Measures how consistently values increase or decrease
- **Outlier count**: Counts values with |z-score| > 3
- **Inflection points**: Detects curvature shifts via 2nd derivative peaks

## Usage
```python
from patternscope.core import analyze
summary = analyze("data.csv", plot=True)
print(summary)
```

## Package Export
The Streamlit app provides a download button that creates a clean ZIP file containing only the files needed for PyPI - no Replit configuration files, no __pycache__, no virtual environment metadata.

## Recent Changes
- 2026-01-09: Initial creation of patternscope package with all required files
