WITH cte_shippingdays_review AS (
	SELECT
		round(avg(tot_ship_days),2) AS avg_shipment_days,
		ord_rev.review_score AS review_score
	FROM (
		SELECT
			order_id,
			(order_delivered_customer_date::date - order_purchase_timestamp::date) AS tot_ship_days
		FROM silver.stg_orders
		WHERE order_delivered_customer_date IS NOT null
	) cln_ord
	JOIN silver.stg_order_reviews ord_rev
		 ON cln_ord.order_id = ord_rev.order_id
	GROUP BY 2
	ORDER BY review_score ASC
)
SELECT
	avg_shipment_days,
	review_score
FROM cte_shippingdays_review
	
