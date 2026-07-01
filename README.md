# Healthcare Claims Data Engineering Pipeline

End-to-end healthcare claims analytics pipeline built with Python, PySpark, PostgreSQL, dbt, Airflow, Docker, and SQL.

## Project Overview

This project demonstrates a production-style data engineering workflow for healthcare claims analytics. It generates realistic patient, provider, and claims data, ingests and cleans the data, transforms it using PySpark, loads it into PostgreSQL, builds dbt models and tests, orchestrates the pipeline with Airflow, and exports dashboard-ready analytics datasets.

## Architecture

Raw Healthcare Data  
→ Python Ingestion  
→ PySpark ETL  
→ PostgreSQL Warehouse  
→ dbt Staging & Mart Models  
→ dbt Tests  
→ Airflow Orchestration  
→ Dashboard Exports

## Tech Stack

Python, Pandas, PySpark, PostgreSQL, dbt, Airflow, Docker, SQL, Git, GitHub

## Key Features

- Generated 5,000+ healthcare claims records with patient and provider data
- Built Python ingestion and validation workflows
- Developed PySpark ETL pipeline for cleaning and transformation
- Loaded cleaned data into PostgreSQL using psycopg2
- Created dbt staging and mart models for healthcare analytics
- Added dbt tests for uniqueness and not-null validation
- Orchestrated the full pipeline using Apache Airflow
- Exported dashboard-ready CSV files for reporting

## dbt Models

- stg_claims
- stg_patients
- stg_providers
- mart_monthly_claims
- mart_payer_denial_rate
- mart_provider_performance

## Business Insights

This project supports analysis of:

- Monthly claims trends
- Claim denial rates by payer
- Provider performance
- Total billed amount
- Total paid amount
- Average claim amount

## How to Run

```bash
python scripts/generate_sample_data.py
python scripts/ingest_data.py
python spark/claims_etl_spark.py
python scripts/load_to_postgres.py
cd healthcare_claims_dbt
dbt run
dbt test
cd ..
python scripts/export_dashboard_data.py
```
