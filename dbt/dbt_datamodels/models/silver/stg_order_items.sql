SELECT
	DISTINCT order_id,
	product_id,
	seller_id,
	price,
	freight_value
FROM bronze.order_items