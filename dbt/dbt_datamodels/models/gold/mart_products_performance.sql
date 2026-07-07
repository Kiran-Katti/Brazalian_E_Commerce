WITH cte_products_performance AS (
	SELECT
		oi.product_id AS product_id,
		p.product_category_name AS product_category_name,
		count(oi.order_id) AS no_of_orders,
		round(sum(oi.price::numeric + oi.freight_value::numeric), 2) AS net_product_revenue
	FROM {{ref("stg_order_items")}} oi
	JOIN {{ref("stg_products")}} p
		ON oi.product_id = p.product_id
	GROUP BY 1,2
)
SELECT 
	product_id,
	product_category_name,
	no_of_orders,
	net_product_revenue
FROM cte_products_performance