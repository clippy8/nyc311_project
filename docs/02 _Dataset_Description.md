Although no primary data was collected for this project, the NYC 311 data used constitutes **secondary use of primary data** — originally reported by residents, centrally collected, and published by the city. Quality assurance is partially automated by municipal systems.

## Data Source

The dataset originates from the **official Open Data Portal of the City of New York**:

- **Dataset:** 311 Service Requests from 2010 to Present  
- **Link:** [https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)  
- **License:** Public Domain (Open Data NYC)

---

## Filtering Criteria (Preprocessing)

To address the research question meaningfully, the data was filtered as follows:

| Criterion           | Selection                                         |
|---------------------|---------------------------------------------------|
| **Time Range**       | 01 January 2023 – 12 July 2025                   |
| **Borough**          | Manhattan only                                   |
| **Complaint Types**  | `'HEAT/HOT WATER'`, `'Noise'`, `'Noise - Residential'` |

---

## Data Structure

### Selected Columns

| Column Name       | Type      | Description                                               |
|-------------------|-----------|-----------------------------------------------------------|
| `Unique Key`      | Integer   | Unique ID of each service request                        |
| `Created Date`    | DateTime  | Timestamp when the complaint was filed                   |
| `Closed Date`     | DateTime  | Timestamp when the case was closed (if available)        |
| `Status`          | String    | Processing status (`Open`, `Closed`, etc.)               |
| `Borough`         | String    | Borough name (only `Manhattan` selected)                 |
| `Complaint Type`  | String    | General category of the complaint                        |
| `Descriptor`      | String    | Further specification of the complaint                   |
| `Longitude`       | Float     | Geographic longitude                                     |
| `Latitude`        | Float     | Geographic latitude                                      |

---

## Data Volume

- After filtering, approx. **15,000 rows** of relevant complaints remained.
- The dataset was exported as a `.csv` file and processed locally using Python/Pandas.

---

The CSV file was created following standard recommendations for tabular data:

- One table per file  
- One observation per row  
- Consistent date formatting (ISO 8601)  
- No colored cells or in-cell comments
