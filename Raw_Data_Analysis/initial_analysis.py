import pandas as pd

file_path: dict[str, str] = {
   "cust_data" : r"..\Raw_Data\olist_customers_dataset.csv",
   "geoloc_data" : r"..\Raw_Data\olist_geolocation_dataset.csv",
   "order_items_data" : r"..\Raw_Data\olist_order_items_dataset.csv",
   "order_pay_data" : r"..\Raw_Data\olist_order_payments_dataset.csv",
   "order_rev_data" : r"..\Raw_Data\olist_order_reviews_dataset.csv",
   "order_data" : r"..\Raw_Data\olist_orders_dataset.csv",
   "product_data" : r"..\Raw_Data\olist_products_dataset.csv",
   "seller_data" : r"..\Raw_Data\olist_sellers_dataset.csv",
   "product_cat_name_trans" : r"..\Raw_Data\product_category_name_translation.csv"
}

df_cust_data: pd.DataFrame = pd.read_csv(file_path["cust_data"])
df_geoloc_data: pd.DataFrame = pd.read_csv(file_path["geoloc_data"])
df_order_items_data: pd.DataFrame = pd.read_csv(file_path["order_items_data"])
df_order_pay_data: pd.DataFrame = pd.read_csv(file_path["order_pay_data"])
df_order_rev_data: pd.DataFrame = pd.read_csv(file_path["order_rev_data"])
df_order_data: pd.DataFrame = pd.read_csv(file_path["order_data"])
df_product_data: pd.DataFrame = pd.read_csv(file_path["product_data"])
df_seller_data: pd.DataFrame = pd.read_csv(file_path["seller_data"])
df_product_cat_name_trans: pd.DataFrame = pd.read_csv(file_path["product_cat_name_trans"])

# print("File Name: cust_data", df_cust_data.info(), "\n")
# print("File Name: geoloc_data", df_geoloc_data.info(), "\n")
# print("File Name: order_items_data", df_order_items_data.info(), "\n")
# print("File Name: order_pay_data", df_order_pay_data.info(), "\n")
# print("File Name: order_rev_data", df_order_rev_data.info(), "\n")
# print("File Name: order_data", df_order_data.info(), "\n")
# print("File Name: product_data", df_product_data.info(), "\n")
# print("File Name: seller_data", df_seller_data.info(), "\n")
# print("File Name: product_cat_name_trans", df_product_cat_name_trans.info(), "\n")

print(df_order_data.head().iloc[0])
# print(len(df_cust_data["customer_unique_id"][0]))