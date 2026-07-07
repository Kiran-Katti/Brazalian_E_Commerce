# Brazilian E-Commerce Data Engineering Project

## Project objective
This project builds a simple end-to-end data pipeline for Brazilian e-commerce data from Olist. It ingests raw CSV files, loads them into PostgreSQL, transforms them with dbt, and produces analytics-ready data marts for a portfolio showcase.

## Architecture diagram
```text
Raw CSV files -> Python extraction/load scripts -> PostgreSQL bronze tables -> dbt staging/silver models -> dbt gold marts
```

## Folder structure
- Raw_Data/: source CSV files
- src/: Python scripts for extraction and loading
- sql/: PostgreSQL table creation scripts
- dbt/dbt_datamodels/: dbt project, staging models, and gold marts
- docs/: architecture and data notes

## Tech stack
- Python and pandas
- PostgreSQL
- dbt Core
- SQL

## Installation instructions
1. Create and activate a Python environment.
2. Install dependencies: pip install -r Requirements.txt
3. Ensure PostgreSQL is installed and running.
4. Create the required tables using sql/create_table.sql.
5. If needed, install dbt and the PostgreSQL adapter for your environment.

## How to run the pipeline
1. Place the CSV files in Raw_Data/.
2. Update the loader entry points in src/main.py as needed.
3. Run the Python loading workflow from src/.
4. Run dbt commands from the dbt/dbt_datamodels folder, for example: dbt run

## Sample output
The pipeline produces curated data marts such as:
- mart_payment_review
- mart_products_performance
- mart_seller_performance
- mart_shippingdays_product

## Future improvements
- Add orchestration and scheduling
- Implement incremental loading
- Add automated tests and data quality checks
- Containerize the pipeline for easier deployment
