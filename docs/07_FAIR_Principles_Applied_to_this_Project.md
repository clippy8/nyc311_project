The FAIR principles (Findable, Accessible, Interoperable, Reusable) aim to make research data transparent, open, and sustainably usable.  
This chapter refers exclusively to **the project's own data product** — not the original NYC data source.

The project was assessed using the FAIR Self-Assessment Tool provided by ARDC and was systematically improved based on its criteria.  
This document summarizes the implementation status at project completion.

---

## F – Findable

| Criterion                     | Implementation                                                                                                                              |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Source documented            | NYC Open Data with persistent URL ([Link](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)) |
| Files clearly named          | `311_Manhattan.csv`, `seasonal_complaint_analysis.py`, `complaints_over_time.png`, `README.md`                                               |
| Metadata available           | Provided via `README.md`, `metadata.json`, `codemeta.json`, `CITATION.cff`                                                                  |
| Persistent Identifier (DOI)  | DOI via Zenodo: [10.5281/zenodo.16232949](https://doi.org/10.5281/zenodo.16232949)                                                           |
| Publication                  | Publicly accessible on Zenodo (data) and GitHub (code & metadata)                                                                            |

---

## A – Accessible

| Criterion                    | Implementation                                                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Source openly accessible    | NYC data is freely accessible without login or API key                                                                                |
| Analysis results published  | Project publicly available on GitHub: [https://github.com/clippy8/nyc311_project](https://github.com/clippy8/nyc311_project)         |
| File formats                | `.csv`, `.py`, `.ipynb`, `.md`, `.png` — all open, machine-readable, and platform-independent                                         |
| Metadata availability       | Metadata permanently accessible via Zenodo, GitHub, and machine-readable files                                                       |
| License information         | Machine-readable licensing included in `LICENSE`, `README.md`, `CITATION.cff`, `codemeta.json`                                       |

---

## I – Interoperable

| Criterion                    | Implementation                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| File formats                | Standardized formats: `.csv` (UTF-8, ISO date), `.json`, `.cff`                |
| Tool compatibility          | Compatible with Python, Excel, LibreOffice, OpenRefine, R, Jupyter             |
| Field naming                | NYC standard preserved (`Complaint Type`, `Created Date`, etc.)                |
| Standard vocabularies       | Metadata compliant with schema.org and Codemeta (`metadata.json`, `codemeta.json`) |
| Resource linking            | References to data source, GitHub repo, and DOI included for both humans and machines |

---

## R – Reusable

| Criterion                   | Implementation                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| License                    | Code under MIT, data & content under CC-BY 4.0 — both documented and machine-readable                     |
| Documentation              | Full workflow documented in `README.md`, Jupyter notebook, and inline Python comments                     |
| Provenance                 | Data origin, filters, time range, and processing documented (`README.md`, `FAIR.md`, `Data_Lifecycle.md`) |
| Version control            | GitHub repository, `v1.0.0` release, versioned DOI on Zenodo                                              |
| Extensibility              | Modular design: expandable with new timeframes, complaint types, or boroughs                              |
| Metadata standard          | Codemeta, CITATION.cff, and schema.org-compliant metadata (`metadata.json`)                              |
| FAIR-compliance achieved   | Project includes DOI, licenses, machine-readable metadata, and is publicly accessible on Zenodo and GitHub |

---

## Overall Evaluation

This project fulfills the FAIR principles across all core areas:

- **Findable** → Clear file naming, structured metadata, DOI  
- **Accessible** → Freely available on GitHub & Zenodo, using open formats  
- **Interoperable** → Standards-based formats & machine-readable interfaces  
- **Reusable** → Legally sound, well-documented, modular, and transparent

The implementation goes beyond minimum FAIR requirements and aligns with current best practices recommended by DFG, EOSC, and Helmholtz.
