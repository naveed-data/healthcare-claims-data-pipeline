CREATE OR REPLACE VIEW vw_monthly_claims_summary AS
SELECT
    DATE_TRUNC('month', claim_date) AS claim_month,
    COUNT(*) AS total_claims,
    SUM(claim_amount) AS total_claim_amount,
    SUM(paid_amount) AS total_paid_amount,
    ROUND(AVG(claim_amount), 2) AS avg_claim_amount
FROM fact_claims
GROUP BY 1;

CREATE OR REPLACE VIEW vw_payer_denial_rate AS
SELECT
    payer_type,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) AS denied_claims,
    ROUND(
        100.0 * SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS denial_rate
FROM fact_claims
GROUP BY payer_type;

CREATE OR REPLACE VIEW vw_provider_performance AS
SELECT
    provider_id,
    provider_name,
    specialty,
    COUNT(*) AS total_claims,
    SUM(claim_amount) AS total_billed_amount,
    SUM(paid_amount) AS total_paid_amount,
    ROUND(AVG(claim_amount), 2) AS avg_claim_amount
FROM fact_claims
GROUP BY provider_id, provider_name, specialty;