SELECT
    provider_id,
    COUNT(*) AS total_claims,
    SUM(claim_amount) AS total_billed_amount,
    SUM(paid_amount) AS total_paid_amount,
    ROUND(AVG(claim_amount)::NUMERIC, 2) AS avg_claim_amount
FROM {{ ref('stg_claims') }}
GROUP BY provider_id