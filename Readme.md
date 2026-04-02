📊 E-commerce Analytics Pipeline

🚀 Overview

This project builds an end-to-end data engineering pipeline that processes e-commerce data and loads it into a structured data warehouse using a star schema.

The pipeline is orchestrated using Apache Airflow and integrates AWS S3 for intermediate storage and PostgreSQL as the data warehouse.

🧱 Architecture

Raw Data → Transform (Pandas) → S3 → PostgreSQL (Star Schema)

🛠️ Tech Stack

Python
Pandas
Apache Airflow
AWS S3 (boto3)
PostgreSQL
SQLAlchemy

📊 Data Model

Fact Table
fact_orders — transactional order data
Dimension Tables
dim_customers — customer details
dim_products — product information

⚙️ Pipeline Workflow

Extract raw data
Transform and clean data using Pandas
Generate dimension and fact tables
Perform data quality checks
Upload cleaned data to S3
Load data into PostgreSQL
Schedule pipeline using Airflow

🔥 Key Features

Modular ETL design (separate transform & load layers)
Airflow DAG orchestration
Data quality validation
Logging and error handling
S3 integration for scalable storage
Idempotent pipeline (safe re-runs)

📂 Project Structure
E_commerce_Analytics_Pipeline/
│
├── dags/                 # Airflow DAGs
├── transform/            # Data transformation logic
├── load/                 # Load to Postgres & S3
├── config/               # DB configuration
├── sql/                  # Table creation scripts
├── main.py               # Local pipeline execution
├── README.md
└── .gitignore


🚀 How to Run
# run locally
python main.py

# run via Airflow
airflow standalone


🚀 Future Improvements

Incremental data loading
Partitioned data storage in S3
Integration with BI tools
Migration to cloud warehouse (Redshift / BigQuery)


📌 Author

Jaya Krishnan