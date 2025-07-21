## Background & Motivation

This data management plan follows recommendations from the **German Research Foundation (DFG)**, the **European Commission (Horizon Europe)**, and principles of good scientific practice.

Although created retrospectively, it could have also been used proactively to:
- Plan storage needs and tools
- Clarify legal requirements early on
- Structure a FAIR-compliant publication process

---

## Data Acquisition

- Source: [NYC Open Data Portal – 311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)  
- Format: CSV (UTF-8)  
- Last download: **15 July 2025**  
- Access: manual via web interface, filtered afterwards

---

## Preprocessing & Filtering

- The locally stored CSV file was filtered by:
  - Time range: **01 January 2023 – 12 July 2025**
  - Borough: **Manhattan**
  - Complaint Types: `HEAT/HOT WATER`, `Noise`, `Noise - Residential`

- Preprocessing steps:
  - Date parsing
  - Selection of relevant columns
  - Aggregation by month
  - Merging of noise-related categories

---

## Tools & File Organization

- **Language & Tools:** Python 3.11, pandas, matplotlib  
- **Files:**
  - `data/311_Manhattan.csv` – filtered dataset  
  - `code/seasonal_complaint_analysis.py` – complete workflow script  
  - `code/seasonal_complaint_analysis.ipynb` – exploratory notebook  
  - `diagramm/complaints_over_time.png` – generated visualization  
  - `README.md`, `LICENSE`, `CITATION.cff`, `metadata.json`, `codemeta.json` – documentation & FAIR metadata

---

## Structure & File Naming

- Clear directory structure:
  - `data/` – data  
  - `code/` – analysis scripts  
  - `diagramm/` – visualizations  
  - `docs/` – documentation

- Naming conventions: `snake_case`, no special characters or spaces  
- ISO date formats (`YYYY-MM-DD`)  
- Version control managed via **Git (GitHub)** and **Zenodo releases**

---

## Documentation

- All processing steps are documented in code and the `README.md`  
- Project structure follows the Data Lifecycle (`06_Data_Lifecycle.md`)  
- FAIR metadata provided in machine-readable formats (`.cff`, `.json`)

---

## Storage & Backup

- **Local backup:**
  - Stored on SSD in structured folders (`data/`, `code/`, `diagramm/`, etc.)
- **External backup:**
  - Full project backup to external USB drive on 20 July 2025
- **Cloud backup:**
  - Manual synchronization (excluding CSV) to GitHub
  - Full archive including CSV uploaded to Zenodo (DOI)

- Backup strategy follows the **3-2-1 rule**:
  - **3 copies**: local, external, online  
  - **2 different media types**: SSD (laptop), HDD (external), cloud (Zenodo)  
  - **1 offsite copy**: Zenodo + external hard drive

---

## Data Protection & Access

> 🔍 Note: Only **publicly available, non-personal data** was used.

- **GDPR is not applicable**, because:
  - No sensitive information  
  - No personally identifiable data  
  - Original dataset is in the public domain

- Therefore:
  - No consent required  
  - No access restrictions needed  
  - Open and legally compliant publication is possible

---

## Legal & Ethical Considerations

- Original data is under the **Open Government License / Public Domain (NYC Open Data)**
- Project code and content are licensed as:
  - **MIT License** (code)
  - **CC-BY 4.0** (data & content)

- No re-identification risk, no ethics approval required  
→ The project is legally and ethically unobjectionable

---

## Provenance (Data Origin & Processing)

- Fully documented in the script `seasonal_complaint_analysis.py`
- All steps traceable:
  - Importing, filtering, aggregation, visualization

- GitHub history and Zenodo release:
  - [GitHub Repository](https://github.com/clippy8/nyc311_project)  
  - [Zenodo DOI](https://doi.org/10.5281/zenodo.16232949)

- Machine-readable provenance via `CITATION.cff`, `metadata.json`, `codemeta.json`

---

## Publication & FAIRness

- Project is publicly available via:
  - GitHub (code, metadata, documentation)
  - Zenodo (archive incl. CSV file)

- DOI: [10.5281/zenodo.16232949](https://doi.org/10.5281/zenodo.16232949)

- FAIR principles implemented via:
  - Structured metadata (`README`, `.cff`, `.json`)
  - Licensing (MIT + CC-BY 4.0)
  - Open data + open code + reproducibility

---

## Roles & Responsibilities

> This project was conducted by a single person, therefore all roles were unified:

| Role            | Responsibility                                     |
|------------------|-----------------------------------------------------|
| Data Collector   | Data research, download, filtering                 |
| Data Steward     | Quality check, cleaning, structuring               |
| Data Analyst     | Evaluation, visualization, interpretation          |
| Data Publisher   | FAIR documentation, licensing, uploads             |

→ All roles are traceable and documented throughout the project
