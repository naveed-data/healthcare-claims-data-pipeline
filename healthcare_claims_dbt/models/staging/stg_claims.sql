SELECT
    claim_id,
    patient_id,
    provider_id,
    claim_date,
    diagnosis_code,
    procedure_code,
    claim_amount,
    paid_amount,
    claim_status,
    payer_type
FROM public.fact_claims