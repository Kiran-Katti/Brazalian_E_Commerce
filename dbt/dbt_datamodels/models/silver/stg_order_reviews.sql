SELECT 
	distinct order_id,
	review_score
FROM {{source("bronze", "order_reviews")}}