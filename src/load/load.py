from .bulk_insert import bulk_insert


def load_customers_data(rows: list[tuple[str, str, int, str, str]]) -> None:

   query = """ 
               INSERT INTO bronze.customers (
                           customer_id,
                           customer_unique_id,
                           customer_zip_code_prefix,
                           customer_city,
                           customer_state
                        )
                        VALUES %s;
                        """
   bulk_insert(query, rows)
   print("Successfully ran load_customers_data")

def load_geolocation_data(rows: list[tuple[str, str, int, str, str]]) -> None:

   query = """
               INSERT INTO bronze.geolocation (
                  geolocation_zip_code_prefix,
                  geolocation_lat,
                  geolocation_lng,
                  geolocation_city,
                  geolocation_state
               )
               VALUES %s;
               """
   bulk_insert(query, rows)
   print("Successfully ran load_geolocation_data")

def load_order_items_data(rows: list[tuple[str, str, int, str, str]]) -> None:

   query = """
               INSERT INTO bronze.order_items (
                  order_id,
                  order_item_id,
                  product_id,
                  seller_id,
                  shipping_limit_date,
                  price,
                  freight_value
               )
               VALUES %s;
               """
   bulk_insert(query, rows)
   print("Successfully ran load_order_items_data")

def load_order_payments_data(rows: list[tuple[str, str, int, str, str]]) -> None:

   query = """
               INSERT INTO bronze.order_payments (
                  order_id,
                  payment_sequential,
                  payment_type,
                  payment_installments,
                  payment_value
               )
               VALUES %s;
               """
   bulk_insert(query, rows)
   print("Successfully ran load_order_payments_data")

def load_order_reviews_data(rows: list[tuple[str, str, int, str, str]]) -> None:

   query = """
               INSERT INTO bronze.order_reviews (
                  review_id,
                  order_id,
                  review_score,
                  review_comment_title,
                  review_comment_message,
                  review_creation_date,
                  review_answer_timestamp
               )
               VALUES %s;
               """
   bulk_insert(query, rows)
   print("Successfully ran load_order_reviews_data")

def load_orders_data(rows: list[tuple[str, str, int, str, str]]) -> None:

   query = """
               INSERT INTO bronze.orders (
                  order_id,
                  customer_id,
                  order_status,
                  order_purchase_timestamp,
                  order_approved_at,
                  order_delivered_carrier_date,
                  order_delivered_customer_date,
                  order_estimated_delivery_date
               )
               VALUES %s;
               """
   bulk_insert(query, rows)
   print("Successfully ran load_orders_data")

def load_product_cat_trans_data(rows: list[tuple[str, str, int, str, str]]) -> None:

   query = """
               INSERT INTO bronze.product_category_translation (
                  product_category_name,
                  product_category_name_english
               )
               VALUES %s;
               """
   bulk_insert(query, rows)
   print("Successfully ran load_product_cat_trans_data")

def load_products_data(rows: list[tuple[str, str, int, str, str]]) -> None:

   query = """
               INSERT INTO bronze.products (
                  product_id,
                  product_category_name,
                  product_name_lenght,
                  product_description_lenght,
                  product_photos_qty,
                  product_weight_g,
                  product_length_cm,
                  product_height_cm,
                  product_width_cm
               )
               VALUES %s;
               """
   bulk_insert(query, rows)
   print("Successfully ran load_products_data")

def load_sellers_data(rows: list[tuple[str, str, int, str, str]]) -> None:

   query = """
               INSERT INTO bronze.sellers (
                  seller_id,
                  seller_zip_code_prefix,
                  seller_city,
                  seller_state
               )
               VALUES %s;
               """
   bulk_insert(query, rows)
   print("Successfully ran load_sellers_data")