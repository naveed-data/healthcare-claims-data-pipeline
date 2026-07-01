import psycopg2
from pathlib import Path

CLEAN_PATH = Path("data/clean")

DB_CONFIG = {
    "dbname": "healthcare_claims",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432",
}

tables = {
    "dim_patients": "dim_patients.csv",
    "dim_providers": "dim_providers.csv",
    "fact_claims": "fact_claims.csv",
}


def load_csv_to_postgres(table_name, file_name):
    file_path = CLEAN_PATH / file_name

    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")

    with open(file_path, "r") as f:
        header = f.readline().strip().split(",")

    columns = ", ".join([f'"{col}" TEXT' for col in header])
    cursor.execute(f'CREATE TABLE {table_name} ({columns});')

    with open(file_path, "r") as f:
        cursor.copy_expert(
            f"COPY {table_name} FROM STDIN WITH CSV HEADER",
            f
        )

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Loaded {file_name} into {table_name}")


def main():
    for table_name, file_name in tables.items():
        load_csv_to_postgres(table_name, file_name)

    print("Data loaded into PostgreSQL successfully.")


if __name__ == "__main__":
    main()