import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

CLEAN_PATH = Path("data/clean")

DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "healthcare_claims"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

tables = {
    "dim_patients": "dim_patients.csv",
    "dim_providers": "dim_providers.csv",
    "fact_claims": "fact_claims.csv"
}


def main():
    for table_name, file_name in tables.items():
        file_path = CLEAN_PATH / file_name
        df = pd.read_csv(file_path)

        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Loaded {len(df)} rows into {table_name}")

    print("Data loaded into PostgreSQL successfully.")


if __name__ == "__main__":
    main()