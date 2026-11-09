# retail-analytics-backend

E-Commerce Revenue and Customer Analytics Backend API built on 541,909 real UK retail transactions (UCI Online Retail, CC BY 4.0).

## Status
Data profiling and Pandas ETL pipeline in progress.

## Tech Stack

- Python 3.12
- Pandas, NumPy
- PostgreSQL 16 (Neon Serverless) -- coming Week 2
- FastAPI, Pydantic v2, SQLAlchemy 2.0 -- coming Week 3
- Pytest -- coming Week 3

## Dataset

UCI Online Retail (#352), DOI: 10.24432/C5BW33, CC BY 4.0.
541,909 transaction rows, 8 columns, UK-based online gift retailer (Dec 2010 -- Dec 2011).

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
