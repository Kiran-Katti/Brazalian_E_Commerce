from load import load
from pathlib import Path
from extract.extract import get_rows


PROJECT_ROOT: Path = Path(__file__).parents[1]


file_paths: dict[str, str | Path] = {
   "cust_data" : PROJECT_ROOT.joinpath("Raw_Data", "olist_customers_dataset.csv"),
   "geoloc_data" : PROJECT_ROOT.joinpath("Raw_Data", "olist_geolocation_dataset.csv"),
   "order_items_data" : PROJECT_ROOT.joinpath("Raw_Data", "olist_order_items_dataset.csv"),
   "order_pay_data" : PROJECT_ROOT.joinpath("Raw_Data", "olist_order_payments_dataset.csv"),
   "order_rev_data" : PROJECT_ROOT.joinpath("Raw_Data", "olist_order_reviews_dataset.csv"),
   "order_data" : PROJECT_ROOT.joinpath("Raw_Data", "olist_orders_dataset.csv"),
   "product_data" : PROJECT_ROOT.joinpath("Raw_Data", "olist_products_dataset.csv"),
   "seller_data" : PROJECT_ROOT.joinpath("Raw_Data", "olist_sellers_dataset.csv"),
   "product_cat_name_trans" : PROJECT_ROOT.joinpath("Raw_Data", "product_category_name_translation.csv")
}

def main() -> None:

   # get_rows(file_paths["cust_data"], load.load_customers_data)
   # get_rows(file_paths["geoloc_data"], load.load_geolocation_data)
   # get_rows(file_paths["order_items_data"], load.load_order_items_data)
   # get_rows(file_paths["order_pay_data"], load.load_order_payments_data)
   # get_rows(file_paths["order_rev_data"], load.load_order_reviews_data)
   # get_rows(file_paths["order_data"], load.load_orders_data)
   # get_rows(file_paths["product_cat_name_trans"], load.load_product_cat_trans_data)
   # get_rows(file_paths["product_data"], load.load_products_data)
   # get_rows(file_paths["seller_data"], load.load_sellers_data)
   pass


if __name__ == "__main__":
   main()