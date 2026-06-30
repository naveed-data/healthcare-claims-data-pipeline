CREATE INDEX IF NOT EXISTS idx_fact_claims_patient_id
ON fact_claims(patient_id);

CREATE INDEX IF NOT EXISTS idx_fact_claims_provider_id
ON fact_claims(provider_id);

CREATE INDEX IF NOT EXISTS idx_fact_claims_claim_date
ON fact_claims(claim_date);

CREATE INDEX IF NOT EXISTS idx_fact_claims_status
ON fact_claims(claim_status);

CREATE INDEX IF NOT EXISTS idx_fact_claims_payer_type
ON fact_claims(payer_type);