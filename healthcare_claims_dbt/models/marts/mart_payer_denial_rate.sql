SELECT
    payer_type,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) AS denied_claims,
    ROUND(
        100.0 * SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS denial_rate
FROM {{ ref('stg_claims') }}
GROUP BY payer_type