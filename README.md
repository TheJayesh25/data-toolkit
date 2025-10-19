# Data Toolkit

A lightweight Python toolkit for **dataset inspection, cleaning, validation, and statistical analysis**.

This repository contains a collection of reusable utilities designed to make working with tabular datasets faster and more systematic. The tools focus on common data preparation tasks such as detecting missing values, summarizing columns, validating schemas, identifying outliers, and profiling datasets.

The toolkit is designed to be **simple, modular, and easy to integrate into data analysis workflows**.

---

## Purpose

Working with real-world datasets often involves repetitive tasks such as:

- Checking dataset structure
- Identifying missing values
- Detecting duplicates
- Understanding column distributions
- Validating schema constraints
- Cleaning formatting issues

This toolkit provides **small focused utilities** that automate many of these steps so analysts can quickly understand and prepare datasets before deeper analysis or modeling.

---

## Features

- Dataset profiling
- Missing value analysis
- Duplicate detection
- Outlier detection
- Distribution summaries
- Correlation analysis
- Schema validation
- Column type identification
- Dataset loading utilities
- Data cleaning helpers

Each tool is designed to solve **one specific task clearly and reliably**.

---

## Project Structure

```
data-toolkit
│
├── cleaning
│ ├── duplicate_detector.py
│ ├── missing_value_analyzer.py
│ └── whitespace_cleaner.py
│
├── profiling
│ ├── column_summary.py
│ ├── dataset_profiler.py
│ └── memory_usage_analyzer.py
│
├── statistics
│ ├── correlation_analyzer.py
│ ├── distribution_summary.py
│ └── outlier_detector.py
│
├── validation
│ ├── column_type_identifier.py
│ ├── schema_validator.py
│ └── value_range_validator.py
│
├── utils
│ ├── column_renamer.py
│ ├── dataframe_summary.py
│ └── dataset_loader.py
│
├── LICENSE
└── README.md
```

---

## Modules

### Cleaning

Utilities focused on **data quality and cleaning**.

| Tool | Description |
|-----|-------------|
| `duplicate_detector.py` | Detect duplicate rows in datasets |
| `missing_value_analyzer.py` | Analyze missing values across columns |
| `whitespace_cleaner.py` | Remove leading/trailing whitespace from string columns |

---

### Profiling

Tools that help understand **dataset structure and characteristics**.

| Tool | Description |
|-----|-------------|
| `dataset_profiler.py` | Generates a high-level overview of the dataset |
| `column_summary.py` | Provides summary statistics per column |
| `memory_usage_analyzer.py` | Analyzes memory usage of dataframe columns |

---

### Statistics

Utilities for **statistical insights and exploratory analysis**.

| Tool | Description |
|-----|-------------|
| `distribution_summary.py` | Summarizes value distributions |
| `correlation_analyzer.py` | Computes correlations between numeric columns |
| `outlier_detector.py` | Detects outliers using statistical methods |

---

### Validation

Tools for **data validation and schema checks**.

| Tool | Description |
|-----|-------------|
| `schema_validator.py` | Validates datasets against expected schema |
| `column_type_identifier.py` | Identifies inferred column types |
| `value_range_validator.py` | Checks if values fall within expected ranges |

---

### Utilities

General helper utilities for working with dataframes.

| Tool | Description |
|-----|-------------|
| `dataset_loader.py` | Utility for loading datasets |
| `column_renamer.py` | Rename columns using rules or mappings |
| `dataframe_summary.py` | Quick overview of dataframe structure |

---

## Example Usage

Example: loading a dataset and generating a quick summary.

```
from utils.dataset_loader import load_dataset
from utils.dataframe_summary import summarize_dataframe

df = load_dataset("data.csv")

summary = summarize_dataframe(df)
print(summary)
```

---

## Design Philosophy

This toolkit follows a few simple principles:
- Single responsibility – each tool solves one problem
- Modular design – tools can be used independently
- Minimal dependencies
- Readable code
- Practical utility for everyday data work

---

## Use Cases

This toolkit can be useful for:
- Data exploration
- Data quality checks
- Dataset validation
- Preprocessing pipelines
- Feature exploration before modeling

---

## Future Improvements

Potential enhancements include:
- Integration with pandas profiling tools
- Automated dataset reports
- Visualization utilities
- CLI interface for quick checks
- Extended statistical diagnostics

---

## Author

**Jayesh Suryawanshi**
Data Analyst / Analytics Engineering
GitHub: https://github.com/TheJayesh25

---

## License
MIT License - This project is licensed under the terms specified in the LICENSE file.