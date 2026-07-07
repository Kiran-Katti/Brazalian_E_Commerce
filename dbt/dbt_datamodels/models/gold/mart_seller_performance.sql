WITH cte_seller_kpi AS (
	SELECT 
		oi.seller_id,
		count(oi.product_id) AS units_sold,
		round(sum(oi.price::numeric),2) AS total_revenue,
		count(DISTINCT oi.order_id) AS order_count
	FROM {{ref("stg_order_items")}} oi
	GROUP BY 1
),
cte_seller_avg_review AS (
	SELECT 
		oi.seller_id,
		round(avg(orv.review_score::numeric),2) AS avg_review_score
	FROM (SELECT DISTINCT seller_id, order_id FROM {{ref("stg_order_items")}}) oi
	JOIN {{ref("stg_order_reviews")}} orv
		ON oi.order_id = orv.order_id
	GROUP BY 1
),
cte_final AS (
SELECT 
	csk.seller_id AS seller_id,
	csk.units_sold AS units_sold, 
	csk.total_revenue AS total_revenue, 
	csk.order_count AS order_count, 
	csr.avg_review_score AS avg_review_score
FROM cte_seller_kpi csk
LEFT JOIN cte_seller_avg_review csr
	 ON csk.seller_id = csr.seller_id
)
SELECT
	seller_id,
	units_sold,
	total_revenue,
	order_count,
	avg_review_score
FROM cte_final