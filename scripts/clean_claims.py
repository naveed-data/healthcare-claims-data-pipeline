import pandas as pd
from pathlib import Path

PROCESSED_PATH = Path("data/processed")
CLEAN_PATH = Path("data/clean")
CLEAN_PATH.mkdir(parents=True, exist_ok=True)


def main():
    patients = pd.read_csv(PROCESSED_PATH / "patients.csv")
    providers = pd.read_csv(PROCESSED_PATH / "providers.csv")
    claims = pd.read_csv(PROCESSED_PATH / "claims.csv")

    claims = claims.drop_duplicates(subset=["claim_id"])
    claims = claims.dropna(subset=["claim_id", "patient_id", "provider_id"])
    claims["claim_date"] = pd.to_datetime(claims["claim_date"])
    claims["claim_amount"] = claims["claim_amount"].astype(float)
    claims["paid_amount"] = claims["paid_amount"].astype(float)

    claims = claims[claims["claim_amount"] > 0]
    claims = claims[claims["paid_amount"] <= claims["claim_amount"]]

    fact_claims = claims.merge(patients, on="patient_id", how="left")
    fact_claims = fact_claims.merge(providers, on="provider_id", how="left", suffixes=("_patient", "_provider"))

    fact_claims.to_csv(CLEAN_PATH / "fact_claims.csv", index=False)

    patients.to_csv(CLEAN_PATH / "dim_patients.csv", index=False)
    providers.to_csv(CLEAN_PATH / "dim_providers.csv", index=False)

    print("Cleaning completed successfully.")
    print(f"Clean claims records: {len(fact_claims)}")


if __name__ == "__main__":
    main()