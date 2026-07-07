-- Architecture diagram

Data Source (CSV files from Kaggle)
      │ 
Save Raw Files Locally
      │
Validate & Basic Checks
      │
Load Raw Data to PostgreSQL
      │
Transform Data using dbt
      │
Data Mart Tables
      │
Optional Dashboard (PowerBI/Dash)