SELECT 
	DISTINCT order_id,
	payment_type,
	payment_value
FROM {{source("bronze", "order_payments")}}