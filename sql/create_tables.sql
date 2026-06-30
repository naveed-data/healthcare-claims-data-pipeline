CREATE TABLE IF NOT EXISTS dim_patients (
    patient_id VARCHAR(20) PRIMARY KEY,
    patient_name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    state VARCHAR(10),
    enrollment_date DATE
);

CREATE TABLE IF NOT EXISTS dim_providers (
    provider_id VARCHAR(20) PRIMARY KEY,
    provider_name VARCHAR(150),
    specialty VARCHAR(100),
    state VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS fact_claims (
    claim_id VARCHAR(20) PRIMARY KEY,
    patient_id VARCHAR(20),
    provider_id VARCHAR(20),
    claim_date DATE,
    diagnosis_code VARCHAR(20),
    procedure_code VARCHAR(20),
    claim_amount DECIMAL(12,2),
    paid_amount DECIMAL(12,2),
    claim_status VARCHAR(30),
    payer_type VARCHAR(50),
    age INT,
    gender VARCHAR(20),
    state_patient VARCHAR(10),
    provider_name VARCHAR(150),
    specialty VARCHAR(100),
    state_provider VARCHAR(10)
);