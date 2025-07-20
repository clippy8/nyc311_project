import pandas as pd

def test_data_columns():
    df = pd.read_csv("data/311_Manhattan.csv")
    assert "Created Date" in df.columns
    assert "Complaint Type" in df.columns

def test_data_format():
    df = pd.read_csv("data/311_Manhattan.csv")
    pd.to_datetime(df["Created Date"], errors="raise")  # will fail if format invalid
