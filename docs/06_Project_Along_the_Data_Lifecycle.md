
The Data Lifecycle outlines the idealized handling of data from planning to archiving.  
This project was consistently developed in alignment with these phases.

---

## 1. Plan

- **Research question defined:**  
  *How does seasonal complaint behavior in Manhattan vary – using HEAT/HOT WATER and NOISE as examples?*

- **Data requirements identified:**  
  - NYC 311 dataset  
  - Timeframe: 01 January 2023 – 12 July 2025  
  - Only borough: Manhattan  
  - Only relevant complaint types

- **Tools selected:**  
  - Python with Pandas and Matplotlib  
  - Markdown + Obsidian for documentation

- Legal aspects reviewed (e.g., licensing, data protection)  
- No personal data involved → no GDPR-related measures required  
- License type: Public Domain → no publication restrictions

---

## 2. Collect

- **Data source:**  
  NYC Open Data  
  [311 Service Requests from 2010 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

- **Access method:**  
  Manual download via web interface (CSV export)  
  Filters: date range, borough, complaint type

- **Local storage:**  
  `311_Manhattan.csv` used as the central dataset

---

## 3. Assure

- **Data quality checked:**  
  - Invalid or empty timestamps removed (`errors='coerce'`)  
  - No duplicates found (based on `Unique Key`)  
  - Only required categories retained

- **Category cleaning:**  
  - `Noise` + `Noise - Residential` → `NOISE_TOTAL`  
  - Documented in the analysis script

- Data quality assessed based on **DAMA quality dimensions (UK 2013):**
  - **Accuracy**: Checked date formats and category mappings  
  - **Completeness**: Incomplete entries removed  
  - **Consistency**: Unified treatment of noise/heat categories

---

## 4. Describe

- **Dataset structure documented:**  
  → see `02_Dataset.md`  
  - 9 columns: time, type, geography, status  
  - Data types and column purposes explained  
  - All processing steps documented (Markdown + code comments)  
  - Field meanings and filtering criteria covered in `02_Dataset.md`  
  - Versioning handled via filenames, timestamps, and backlinks  
  - No personal data involved, but licenses are clearly documented

- **Data model for monthly aggregation developed:**  
  - New column: `Month` using `.dt.to_period("M")`  
  - Grouping with `groupby()`

- Metadata & Documentation:
  - Internal metadata included in Markdown and machine-readable formats  
  - Content documentation includes:
    - Title, source, data collection period  
    - Column descriptions and meanings  
    - Filtering and preprocessing steps

  - **Additional metadata quality aspects (based on best practices):**
    - Standardized ISO date format (e.g., 2023-06)  
    - Handling of missing values (`NaN`, `"n.d."`)  
    - Clear documentation of license and provenance  
  - Metadata formats: `README.md`, `CITATION.cff`, `codemeta.json`, `metadata.json`

---

## 5. Preserve

- **Files versioned & backed up locally:**  
  - `311_Manhattan.csv` (raw data)  
  - `seasonal_complaint_analysis.py` (script)  
  - `complaints_over_time.png` (visualization)

- **Consistent file naming & folder structure:**  
  - Chronological and thematic organization  
  - All file paths documented

---

## 6. Discover

- **Metadata fully documented:**  
  - Source, filters, timeframe, fields  
  - Machine-readable metadata via `.cff`, `.json`, `.md`

- **Publication in public repositories:**
  - GitHub (code): [https://github.com/clippy8/nyc311_project](https://github.com/clippy8/nyc311_project)  
  - Zenodo (archive incl. CSV): [https://doi.org/10.5281/zenodo.16232949](https://doi.org/10.5281/zenodo.16232949)

- **Data discovery & search skills**  
  - Use of scientific data portals (e.g., GFBio, DataONE)  
  - Knowledge of metadata standards (Dublin Core, schema.org, Codemeta)

---

## 7. Integrate

- **Integration potential for further analysis:**  
  - Combine with weather data (e.g., temperature vs. heat complaints)  
  - Link with socioeconomic indicators (e.g., poverty, population density)

- **Modular project design → expandable to other boroughs or timeframes**

---

## 8. Analyze

- **Descriptive analysis:**  
  - Monthly aggregation  
  - Comparison of HEAT vs. NOISE  
  - Line chart visualization

- **No inferential statistics used – focus on structural patterns**

- **Interpretation aligned with related studies (RentHop, Analytics Vidhya)**

---

## 9. Preserve & Publish

- **Data & code published FAIRly:**  
  - GitHub for code and metadata  
  - Zenodo for long-term archiving incl. CSV (>100 MB)

- **DOI (Persistent Identifier):**  
  [10.5281/zenodo.16232949](https://doi.org/10.5281/zenodo.16232949)

- **Licensing:**  
  - **Code**: MIT License  
  - **Data & content**: CC-BY 4.0  
  - Both licenses are machine-readable and documented in the repository

- **Repository selection criteria:**  
  - Metadata quality  
  - Version control support  
  - Access control & license compatibility  
  - DOI support & indexing (e.g., Google Dataset Search, OpenAIRE)

---

## Automate & Share Code (inspired by Open Science principles)

- Analysis performed using a self-written Python script  
- The script is:
  - Modular  
  - Commented (purpose, input, output)  
  - Portable (runs without modification on other systems)

- Versioned and shared via GitHub  
- Archived via Zenodo for long-term reusability  
- This approach aligns with the Open Science principle of **“computational reproducibility”**

---

## ✅ Conclusion

The entire project adheres to the Data Lifecycle model.  
As a result, the workflow is:
- **methodologically transparent**  
- **ethically sound**  
- **technically reproducible**  
- **interpreted with domain relevance**  
- **publicly accessible and FAIR-compliant**
