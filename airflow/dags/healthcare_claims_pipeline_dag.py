from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_PATH = "/Users/naveedshaik/Desktop/healthcare-claims-data-pipeline"

default_args = {
    "owner": "naveed",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="healthcare_claims_pipeline",
    default_args=default_args,
    description="End-to-end healthcare claims data pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["healthcare", "data-engineering", "dbt", "spark"],
) as dag:

    generate_sample_data = BashOperator(
        task_id="generate_sample_data",
        bash_command=f"cd {PROJECT_PATH} && python scripts/generate_sample_data.py",
    )

    ingest_data = BashOperator(
        task_id="ingest_data",
        bash_command=f"cd {PROJECT_PATH} && python scripts/ingest_data.py",
    )

    run_spark_etl = BashOperator(
        task_id="run_spark_etl",
        bash_command=f"cd {PROJECT_PATH} && python spark/claims_etl_spark.py",
    )

    load_to_postgres = BashOperator(
        task_id="load_to_postgres",
        bash_command=f"cd {PROJECT_PATH} && python scripts/load_to_postgres.py",
    )

    run_dbt_models = BashOperator(
        task_id="run_dbt_models",
        bash_command=f"cd {PROJECT_PATH}/healthcare_claims_dbt && dbt run",
    )

    run_dbt_tests = BashOperator(
        task_id="run_dbt_tests",
        bash_command=f"cd {PROJECT_PATH}/healthcare_claims_dbt && dbt test",
    )

    generate_sample_data >> ingest_data >> run_spark_etl >> load_to_postgres >> run_dbt_models >> run_dbt_tests