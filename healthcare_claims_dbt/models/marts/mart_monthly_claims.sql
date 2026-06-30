SELECT
    DATE_TRUNC('month', claim_date) AS claim_month,
    COUNT(*) AS total_claims,
    SUM(claim_amount) AS total_claim_amount,
    SUM(paid_amount) AS total_paid_amount,
    ROUND(AVG(claim_amount)::NUMERIC, 2) AS avg_claim_amount
FROM {{ ref('stg_claims') }}
GROUP BY 1