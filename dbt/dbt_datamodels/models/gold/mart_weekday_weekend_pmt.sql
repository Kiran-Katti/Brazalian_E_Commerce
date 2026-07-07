WITH cte_weekday_weekend_pmt AS (
	SELECT
		ord_pmt.payment_value,
		CASE 
			WHEN extract(ISODOW FROM ord.order_purchase_timestamp) IN (6,7) THEN 'weekend'
			ELSE 'weekday'
		END	AS weekday_weekend
	FROM {{ref("stg_orders")}} ord
	JOIN {{ref("stg_order_payments")}} ord_pmt ON ord.order_id = ord_pmt.order_id
),
cte_final AS (
	SELECT
		weekday_weekend,
		round((sum(payment_value)::NUMERIC)/1000000, 2) AS net_pmt_mil,
		round((sum(payment_value)/(sum(sum(payment_value)) OVER()))::numeric * 100, 2) AS pmt_pct
	FROM cte_weekday_weekend_pmt
	GROUP BY weekday_weekend
)
SELECT
	weekday_weekend,
	net_pmt_mil,
	pmt_pct
FROM cte_final