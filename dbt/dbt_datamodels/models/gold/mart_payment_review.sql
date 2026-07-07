WITH cte_payment_review AS (
   SELECT
      ord_pmt.order_id AS order_id,
      ord_pmt.payment_type AS payment_type,
      ord_rev.review_score AS review_score
   FROM {{ref("stg_order_payments")}} ord_pmt
   JOIN {{ref("stg_order_reviews")}} ord_rev
      ON ord_pmt.order_id  = ord_rev.order_id 
)
SELECT 
	order_id,
	payment_type,
	review_score
FROM cte_payment_review