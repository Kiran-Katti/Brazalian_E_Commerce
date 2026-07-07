WITH cte_shippingdays_product AS (
SELECT
	ord_prd.product_category_name AS product_category_name,
	round(avg(tot_ship_days),2) AS avg_shipment_days
FROM (
	SELECT
		order_id,
		(order_delivered_customer_date::date - order_purchase_timestamp::date) AS tot_ship_days
	FROM {{ref("stg_orders")}}
) cln_ord
JOIN (
	SELECT 
		ord_itm.order_id,
		prd.product_category_name
	FROM {{ref("stg_order_items")}} ord_itm
	JOIN {{ref("stg_products")}} prd 
		ON ord_itm.product_id = prd.product_id 
) ord_prd 
	ON cln_ord.order_id = ord_prd.order_id
GROUP BY 1
)
SELECT 
	product_category_name,
	avg_shipment_days
FROM cte_shippingdays_product