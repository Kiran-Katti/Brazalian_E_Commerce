WITH cte_final AS (
	SELECT 
		DISTINCT order_id,
		order_purchase_timestamp::date AS order_purchase_timestamp,	
		NULLIF(order_delivered_customer_date, 'NaN')::date AS order_delivered_customer_date
	FROM {{source("bronze", "orders")}}
)
SELECT 
	order_id,
	order_purchase_timestamp,
	order_delivered_customer_date
FROM cte_final