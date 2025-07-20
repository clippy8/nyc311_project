# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Robin Zaumseil

import pandas as pd
import matplotlib.pyplot as plt
import os

# Dynamic path to the /data directory
base_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
data_path = os.path.join(base_dir, "data", "311_Manhattan.csv")

# Load CSV
df = pd.read_csv(data_path)

# Parse dates using fixed format
df['Created Date'] = pd.to_datetime(df['Created Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

# Keep only relevant columns
df = df[['Created Date', 'Complaint Type']]

# Filter for specific complaint types
df = df[df['Complaint Type'].isin(['HEAT/HOT WATER', 'Noise', 'Noise - Residential'])]

# Add monthly aggregation column
df['Month'] = df['Created Date'].dt.to_period('M')

# Group by month and complaint type, then count
counts = df.groupby(['Month', 'Complaint Type']).size().unstack(fill_value=0)

# Optionally combine different noise complaint types
if 'Noise - Residential' in counts.columns:
    counts['NOISE_TOTAL'] = counts.get('Noise', 0) + counts.get('Noise - Residential', 0)
    counts = counts.drop(columns=['Noise', 'Noise - Residential'])
else:
    counts.rename(columns={'Noise': 'NOISE_TOTAL'}, inplace=True)

# Plot the results
plt.figure(figsize=(12, 6))
counts.plot(kind='line', ax=plt.gca(), marker='o')
plt.title('Monthly 311 Complaints in Manhattan (HEAT/HOT WATER vs. NOISE)')
plt.xlabel('Month')
plt.ylabel('Number of Complaints')
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.legend(title='Complaint Type')
plt.show()