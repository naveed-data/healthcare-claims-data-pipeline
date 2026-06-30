import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker()
random.seed(42)
Faker.seed(42)

RAW_DATA_PATH = Path("data/raw")
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

NUM_PATIENTS = 1000
NUM_PROVIDERS = 100
NUM_CLAIMS = 5000

states = ["TX", "CA", "NY", "FL", "IL", "GA", "WA", "AZ"]
genders = ["Male", "Female"]
specialties = ["Cardiology", "Primary Care", "Orthopedics", "Dermatology", "Neurology"]
claim_statuses = ["Approved", "Denied", "Pending"]
payer_types = ["Medicare", "Medicaid", "Commercial", "Self-Pay"]


def generate_patients():
    patients = []
    for i in range(1, NUM_PATIENTS + 1):
        patients.append({
            "patient_id": f"P{i:05d}",
            "patient_name": fake.name(),
            "age": random.randint(18, 90),
            "gender": random.choice(genders),
            "state": random.choice(states),
            "enrollment_date": fake.date_between(start_date="-5y", end_date="today")
        })
    return pd.DataFrame(patients)


def generate_providers():
    providers = []
    for i in range(1, NUM_PROVIDERS + 1):
        providers.append({
            "provider_id": f"PR{i:04d}",
            "provider_name": fake.company(),
            "specialty": random.choice(specialties),
            "state": random.choice(states)
        })
    return pd.DataFrame(providers)


def generate_claims(patients, providers):
    claims = []
    for i in range(1, NUM_CLAIMS + 1):
        claim_amount = round(random.uniform(100, 15000), 2)
        status = random.choice(claim_statuses)

        if status == "Approved":
            paid_amount = round(claim_amount * random.uniform(0.6, 1.0), 2)
        elif status == "Denied":
            paid_amount = 0.00
        else:
            paid_amount = round(claim_amount * random.uniform(0.1, 0.5), 2)

        claims.append({
            "claim_id": f"C{i:06d}",
            "patient_id": random.choice(patients["patient_id"].tolist()),
            "provider_id": random.choice(providers["provider_id"].tolist()),
            "claim_date": fake.date_between(start_date="-2y", end_date="today"),
            "diagnosis_code": random.choice(["E11", "I10", "J45", "M54", "N18", "K21"]),
            "procedure_code": random.choice(["99213", "99214", "93000", "80053", "97110"]),
            "claim_amount": claim_amount,
            "paid_amount": paid_amount,
            "claim_status": status,
            "payer_type": random.choice(payer_types)
        })
    return pd.DataFrame(claims)


def main():
    patients = generate_patients()
    providers = generate_providers()
    claims = generate_claims(patients, providers)

    patients.to_csv(RAW_DATA_PATH / "patients.csv", index=False)
    providers.to_csv(RAW_DATA_PATH / "providers.csv", index=False)
    claims.to_csv(RAW_DATA_PATH / "claims.csv", index=False)

    print("Sample healthcare data generated successfully.")
    print(f"Patients: {len(patients)}")
    print(f"Providers: {len(providers)}")
    print(f"Claims: {len(claims)}")


if __name__ == "__main__":
    main()