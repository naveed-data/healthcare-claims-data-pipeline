from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, round
from pathlib import Path

PROCESSED_PATH = "data/processed"
SPARK_OUTPUT_PATH = "data/spark_output"

Path(SPARK_OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

spark = SparkSession.builder \
    .appName("HealthcareClaimsETL") \
    .getOrCreate()

patients = spark.read.option("header", True).option("inferSchema", True).csv(f"{PROCESSED_PATH}/patients.csv")
providers = spark.read.option("header", True).option("inferSchema", True).csv(f"{PROCESSED_PATH}/providers.csv")
claims = spark.read.option("header", True).option("inferSchema", True).csv(f"{PROCESSED_PATH}/claims.csv")

claims_clean = claims.dropDuplicates(["claim_id"]) \
    .dropna(subset=["claim_id", "patient_id", "provider_id"]) \
    .withColumn("claim_date", to_date(col("claim_date"))) \
    .filter(col("claim_amount") > 0) \
    .filter(col("paid_amount") <= col("claim_amount"))

fact_claims = claims_clean \
    .join(patients, "patient_id", "left") \
    .join(providers, "provider_id", "left")

fact_claims.write.mode("overwrite").option("header", True).csv(f"{SPARK_OUTPUT_PATH}/fact_claims")

patients.write.mode("overwrite").option("header", True).csv(f"{SPARK_OUTPUT_PATH}/dim_patients")
providers.write.mode("overwrite").option("header", True).csv(f"{SPARK_OUTPUT_PATH}/dim_providers")

print("PySpark ETL completed successfully.")
print(f"Fact claims count: {fact_claims.count()}")

spark.stop()