import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from load.load_to_postgres import load_sql
from transform.transform import transformed_data



def main():
    dim_products, dim_customers, fact_orders = transformed_data()
    load_sql(dim_products, dim_customers, fact_orders)

if __name__== "__main__":
    main()