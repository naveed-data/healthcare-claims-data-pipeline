-- Monthly claims trend
SELECT DATE_TRUNC('month', claim_date) AS claim_month,
       COUNT(*) AS total_claims,
       SUM(claim_amount) AS total_claim_amount,
       SUM(paid_amount) AS total_paid_amount
FROM fact_claims
GROUP BY 1
ORDER BY 1;

-- Denial rate by payer
SELECT payer_type,
       COUNT(*) AS total_claims,
       SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) AS denied_claims,
       ROUND(100.0 * SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) / COUNT(*), 2) AS denial_rate
FROM fact_claims
GROUP BY payer_type
ORDER BY denial_rate DESC;

-- Provider performance
SELECT provider_name,
       specialty,
       COUNT(*) AS claim_volume,
       SUM(claim_amount) AS billed_amount,
       SUM(paid_amount) AS paid_amount
FROM fact_claims
GROUP BY provider_name, specialty
ORDER BY claim_volume DESC;