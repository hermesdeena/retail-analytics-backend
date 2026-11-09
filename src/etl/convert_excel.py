"""
Convert the raw UCI Online Retail Excel file into a CSV file.

Run once from the project root:
    python src/etl/convert_excel.py
"""

from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
EXCLE_PATH = RAW_DIR / "Online Retail.xlsx"
CSV_PATH = RAW_DIR / "online_retail_raw.csv"


print(f"Reading {EXCLE_PATH} file takes 1-2 seconds...")
df = pd.read_excel(EXCLE_PATH,
                   dtype={"InvoiceNo": str,
                          "StockCode": str,
                          "CustomerId": str})

df.to_csv(CSV_PATH, index=False)

print(f"Saved {len(df):,} rows and {len(df.columns)} columns to {CSV_PATH}")

print("Columns:", list(df.columns))

print(df.head(3).to_string())
