import os
import sys

sys.path.append("/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline")


from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

from transform.transform import transformed_data
from load.load_to_postgres import load_sql




def transform_task():
    transformed_data()


def load_task():
    load_sql()


with DAG(
    dag_id = "ecommerce_pipeline_s3",
    start_date = datetime(2024,1,1),
    schedule = "@daily",
    catchup=False
) as dag:
    
    transform = PythonOperator(
        task_id = "transform_data",
        python_callable = transform_task
    )

    load = PythonOperator(
        task_id = "load_to_postgres",
        python_callable = load_task
    )

    transform >> load