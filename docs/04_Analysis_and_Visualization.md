## Analysis Objective

The goal was to examine how complaints related to **HEAT/HOT WATER** and **NOISE** vary over the course of the year – specifically within **Manhattan**.

To achieve this, the following steps were taken:
- Counted monthly complaint volumes per category  
- Created a visual comparison  
- Conducted a structural (non-statistical) analysis

---

## Processing Steps (in Python)

- Although OpenRefine was introduced in the course for data cleaning, this project used Python. Nonetheless, **similar concepts** were applied (e.g., data profiling, transformation, error correction).

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("311_Manhattan.csv")

# Convert date column
df["Created Date"] = pd.to_datetime(df["Created Date"], errors="coerce")

# Keep only valid entries
df = df.dropna(subset=["Created Date"])

# Create new column: Year-Month
df["Month"] = df["Created Date"].dt.to_period("M")

# Consolidate NOISE types
df["Complaint Group"] = df["Complaint Type"].replace({
    "Noise - Residential": "NOISE_TOTAL",
    "Noise": "NOISE_TOTAL"
})

# Filter and count
summary = df[df["Complaint Group"].isin(["HEAT/HOT WATER", "NOISE_TOTAL"])]
monthly = summary.groupby(["Month", "Complaint Group"]).size().unstack(fill_value=0)

# Visualization
monthly.plot(marker="o", figsize=(12, 6))
plt.title("Monthly 311 Complaints in Manhattan (HEAT/HOT WATER vs. NOISE)")
plt.xlabel("Month")
plt.ylabel("Number of Complaints")
plt.legend(title="Complaint Type")
plt.tight_layout()
plt.savefig("diagramm.png")
plt.show()
```

---

## Result

The following chart shows the monthly volume of complaints:  
![[Pasted image 20250719152711.png]]

---

## Observations

- Prior to analysis, all **data cleaning steps** were documented and applied to **avoid distortions caused by incomplete or faulty entries**.

| Category         | Pattern Description |
|------------------|---------------------|
| **HEAT/HOT WATER** | Clear peaks in winter (Dec–Feb); almost no complaints in summer |
| **NOISE_TOTAL**    | Relatively constant throughout the year, with slight increases in summer (due to events, outdoor activity) |

---

## Reusability

This analysis is **fully reproducible**:

- Raw data provided as CSV  
- Script fully commented  
- Chart exported  
- Structure consistently documented
