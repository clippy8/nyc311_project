# NYC 311 Seasonal Complaint Analysis – Manhattan (2023–2025)

**Author**: Robin Zaumseil  
**Project period**: July 2025  
**Licenses**:  
- Code: [MIT License](LICENSE)  
- Data & content: [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
**DOI**: [10.5281/zenodo.16232949](https://doi.org/10.5281/zenodo.16232949)
**Data source**: [NYC Open Data Portal – 311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

---

## Project Description

This project analyzes seasonal complaint patterns in the borough of **Manhattan**, based on publicly available 311 service request data. The focus is on the complaint types:

- `HEAT/HOT WATER` – complaints about lack of heating or hot water  
- `Noise`, `Noise - Residential` – general and residential noise complaints

The goal is to reveal trends over time and visualize them effectively.

---

## Project Structure

| File/Folder                     | Description                                                    |
|--------------------------------|----------------------------------------------------------------|
| `seasonal_complaint_analysis.py`     | Python script for data processing and visualization             |
| `seasonal_complaint_analysis.ipynb`  | Jupyter notebook for exploratory analysis                       |
| `data/311_Manhattan.csv`             | Filtered dataset with 311 complaints from Manhattan              |
| `diagramm/complaints_over_time.png` | Time series chart of monthly complaint types                    |
| `requirements.txt`                  | Python dependencies for environment setup                       |
| `README.md`                         | Project overview and FAIR documentation                         |
| `LICENSE`                           | Combined license for code and content                           |
| `CITATION.cff` / `metadata.json` / `codemeta.json` | Machine-readable metadata files for citation and FAIR compliance |

---

## Data Provenance

- **Source**: NYC Open Data Portal  
- **Downloaded**: July 15, 2025  
- **Filtering criteria**:
  - `Borough = Manhattan`
  - `Date: 2023-01-01 to 2025-07-12`
  - `Complaint Types`: `"HEAT/HOT WATER"`, `"Noise"`, `"Noise - Residential"`
- **Transformations**:
  - Parsed timestamps to ISO format (`YYYY-MM-DD hh:mm:ss`)
  - Aggregated by month (`.dt.to_period('M')`)
  - Grouped by complaint type
- **Tools used**: Python 3.11, pandas, matplotlib

---

## Data Formats

- `CSV` (UTF-8): tabular data with headers  
  - Columns: `Created Date`, `Complaint Type`  
  - Time format: `YYYY-MM-DD hh:mm:ss`
- `PNG`: line chart of monthly complaint volumes
- `PY`/`IPYNB`: executable code for analysis reproducibility

---

## Reuse & Licensing

**This project is published under two open licenses**:

- **Code (Python scripts and notebooks):**  
  MIT License — free to use, with attribution  
  [→ See `LICENSE`](LICENSE)

- **Data & content (CSV, diagrams, README):**  
  Creative Commons Attribution 4.0 International (CC-BY 4.0)  
  → Attribution required, commercial use allowed

The underlying raw data is in the public domain as provided by NYC Open Data.

---

## Usage Instructions

1. Install the required Python packages:
```bash
pip install -r requirements.txt
```
2. Run the analysis script:
```
python seasonal_complaint_analysis.py
```
The script will load the dataset and generate a line plot showing monthly complaint trends for heating and noise issues between January 1, 2023, and July 15, 2025.