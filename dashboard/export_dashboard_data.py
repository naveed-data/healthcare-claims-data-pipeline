import pandas as pd
import psycopg2
from pathlib import Path

OUTPUT_PATH = Path("dashboard/exports")
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

DB_CONFIG = {
    "dbname": "healthcare_claims",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432",
}

queries = {
    "monthly_claims_summary": "SELECT * FROM mart_monthly_claims;",
    "payer_denial_rate": "SELECT * FROM mart_payer_denial_rate;",
    "provider_performance": "SELECT * FROM mart_provider_performance;",
}


def main():
    conn = psycopg2.connect(**DB_CONFIG)

    for file_name, query in queries.items():
        df = pd.read_sql(query, conn)
        output_file = OUTPUT_PATH / f"{file_name}.csv"
        df.to_csv(output_file, index=False)
        print(f"Exported: {output_file}")

    conn.close()
    print("Dashboard data export completed successfully.")


if __name__ == "__main__":
    main()