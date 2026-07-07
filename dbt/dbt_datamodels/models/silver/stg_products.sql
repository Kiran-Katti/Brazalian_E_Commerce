WITH cte_final AS (
	SELECT 
		DISTINCT product_id,
		CASE 
			WHEN product_category_name = 'NaN' THEN 'Unknown'
			ELSE product_category_name
		END AS product_category_name
	FROM {{source("bronze", "products")}}
)
SELECT  
	product_id,
	product_category_name
FROM cte_final