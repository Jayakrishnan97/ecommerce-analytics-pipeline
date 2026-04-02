from sqlalchemy import create_engine
from config.config import DB_CONFIG
import pandas as pd
import logging

def get_engine():
    return create_engine(f'postgresql://{DB_CONFIG["user"]}:{DB_CONFIG["password"]}@{DB_CONFIG["host"]}:{DB_CONFIG["port"]}/{DB_CONFIG["db_name"]}')

base_path = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/cleaned"


def load_sql():
    engine = get_engine()

    dim_products = pd.read_csv(f"{base_path}/dim_products.csv")
    dim_customers = pd.read_csv(f"{base_path}/dim_customers.csv")
    fact_orders = pd.read_csv(f"{base_path}/fact_orders.csv")

    logging.info("Loading dim_products...")
    
    dim_products.to_sql(
        name="dim_products",
        con=engine,
        if_exists = "append",
        index = False
    )
    
    
    logging.info("Loading dim_customers...")
    dim_customers.to_sql(
        name="dim_customers",
        con = engine,
        if_exists = "append",
        index = False
    )
    
    logging.info("Loading fact_orders...")
    fact_orders.to_sql(
        name="fact_orders",
        con = engine,
        if_exists = "append",
        index = False
    )

    
    logging.info("Data loaded successfully")

