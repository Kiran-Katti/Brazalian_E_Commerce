----------------------------------------------------------------------------
-- Raw table schema

<class 'pandas.DataFrame'>
RangeIndex: 99441 entries, 0 to 99440
Data columns (total 5 columns):
 #   Column                    Non-Null Count  Dtype
---  ------                    --------------  -----
 0   customer_id               99441 non-null  str
 1   customer_unique_id        99441 non-null  str
 2   customer_zip_code_prefix  99441 non-null  int64
 3   customer_city             99441 non-null  str
 4   customer_state            99441 non-null  str
dtypes: int64(1), str(4)
memory usage: 3.8 MB
File Name: cust_data None
----------------------------------------------------------------------------
----------------------------------------------------------------------------
<class 'pandas.DataFrame'>
RangeIndex: 1000163 entries, 0 to 1000162
Data columns (total 5 columns):
 #   Column                       Non-Null Count    Dtype
---  ------                       --------------    -----
 0   geolocation_zip_code_prefix  1000163 non-null  int64
 1   geolocation_lat              1000163 non-null  float64
 2   geolocation_lng              1000163 non-null  float64
 3   geolocation_city             1000163 non-null  str
 4   geolocation_state            1000163 non-null  str
dtypes: float64(2), int64(1), str(2)
memory usage: 38.2 MB
File Name: geoloc_data None
----------------------------------------------------------------------------
----------------------------------------------------------------------------
<class 'pandas.DataFrame'>
RangeIndex: 112650 entries, 0 to 112649
Data columns (total 7 columns):
 #   Column               Non-Null Count   Dtype
---  ------               --------------   -----
 0   order_id             112650 non-null  str
 1   order_item_id        112650 non-null  int64
 2   product_id           112650 non-null  str
 3   seller_id            112650 non-null  str
 4   shipping_limit_date  112650 non-null  str
 5   price                112650 non-null  float64
 6   freight_value        112650 non-null  float64
dtypes: float64(2), int64(1), str(4)
memory usage: 6.0 MB
File Name: order_items_data None
----------------------------------------------------------------------------
----------------------------------------------------------------------------
<class 'pandas.DataFrame'>
RangeIndex: 103886 entries, 0 to 103885
Data columns (total 5 columns):
 #   Column                Non-Null Count   Dtype
---  ------                --------------   -----
 0   order_id              103886 non-null  str
 1   payment_sequential    103886 non-null  int64
 2   payment_type          103886 non-null  str
 3   payment_installments  103886 non-null  int64
 4   payment_value         103886 non-null  float64
dtypes: float64(1), int64(2), str(2)
memory usage: 4.0 MB
File Name: order_pay_data None
----------------------------------------------------------------------------
----------------------------------------------------------------------------
<class 'pandas.DataFrame'>
RangeIndex: 99224 entries, 0 to 99223
Data columns (total 7 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   review_id                99224 non-null  str
 1   order_id                 99224 non-null  str
 2   review_score             99224 non-null  int64
 3   review_comment_title     11568 non-null  str
 4   review_comment_message   40977 non-null  str
 5   review_creation_date     99224 non-null  str
 6   review_answer_timestamp  99224 non-null  str
dtypes: int64(1), str(6)
memory usage: 5.3 MB
File Name: order_rev_data None
----------------------------------------------------------------------------
----------------------------------------------------------------------------
<class 'pandas.DataFrame'>
RangeIndex: 99441 entries, 0 to 99440
Data columns (total 8 columns):
 #   Column                         Non-Null Count  Dtype
---  ------                         --------------  -----
 0   order_id                       99441 non-null  str
 1   customer_id                    99441 non-null  str
 2   order_status                   99441 non-null  str
 3   order_purchase_timestamp       99441 non-null  str
 4   order_approved_at              99281 non-null  str
 5   order_delivered_carrier_date   97658 non-null  str
 6   order_delivered_customer_date  96476 non-null  str
 7   order_estimated_delivery_date  99441 non-null  str
dtypes: str(8)
memory usage: 6.1 MB
File Name: order_data None
----------------------------------------------------------------------------
----------------------------------------------------------------------------
<class 'pandas.DataFrame'>
RangeIndex: 32951 entries, 0 to 32950
Data columns (total 9 columns):
 #   Column                      Non-Null Count  Dtype
---  ------                      --------------  -----
 0   product_id                  32951 non-null  str
 1   product_category_name       32341 non-null  str
 2   product_name_lenght         32341 non-null  float64
 3   product_description_lenght  32341 non-null  float64
 4   product_photos_qty          32341 non-null  float64
 5   product_weight_g            32949 non-null  float64
 6   product_length_cm           32949 non-null  float64
 7   product_height_cm           32949 non-null  float64
 8   product_width_cm            32949 non-null  float64
dtypes: float64(7), str(2)
memory usage: 2.3 MB
File Name: product_data None
----------------------------------------------------------------------------
----------------------------------------------------------------------------
<class 'pandas.DataFrame'>
RangeIndex: 3095 entries, 0 to 3094
Data columns (total 4 columns):
 #   Column                  Non-Null Count  Dtype
---  ------                  --------------  -----
 0   seller_id               3095 non-null   str
 1   seller_zip_code_prefix  3095 non-null   int64
 2   seller_city             3095 non-null   str
 3   seller_state            3095 non-null   str
dtypes: int64(1), str(3)
memory usage: 96.8 KB
File Name: seller_data None
----------------------------------------------------------------------------
----------------------------------------------------------------------------
<class 'pandas.DataFrame'>
RangeIndex: 71 entries, 0 to 70
Data columns (total 2 columns):
 #   Column                         Non-Null Count  Dtype
---  ------                         --------------  -----
 0   product_category_name          71 non-null     str
 1   product_category_name_english  71 non-null     str
dtypes: str(2)
memory usage: 1.2 KB
File Name: product_cat_name_trans None
----------------------------------------------------------------------------
----------------------------------------------------------------------------
-- Raw table relation

| Parent Table             | Child Table        | Join Column                | Cardinality          |
| ------------------------ | ------------------ | -------------------------- | -------------------- |
| `customer_data`          | `order_data`       | `customer_id`              | **1 : Many**         |
| `order_data`             | `order_items_data` | `order_id`                 | **1 : Many**         |
| `order_data`             | `order_pay_data`   | `order_id`                 | **1 : Many**         |
| `order_data`             | `order_rev_data`   | `order_id`                 | **1 : One** (mostly) |
| `product_data`           | `order_items_data` | `product_id`               | **1 : Many**         |
| `seller_data`            | `order_items_data` | `seller_id`                | **1 : Many**         |
| `product_cat_name_trans` | `product_data`     | `product_category_name`    | **1 : Many**         |
| `geoloc_data`            | `customer_data`    | `customer_zip_code_prefix` | **Many : Many***     |
| `geoloc_data`            | `seller_data`      | `seller_zip_code_prefix`   | **Many : Many***     |
----------------------------------------------------------------------------