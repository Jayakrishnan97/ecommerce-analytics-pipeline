import boto3
import logging
from botocore.exceptions import ClientError
import os

s3_client = boto3.client('s3')

response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])


def upload_file(filename, bucket, object = None):
    if object is None:
        object = os.path.basename(filename)
    
    try:
        response = s3_client.upload_file(filename, bucket, object)
    except ClientError as e:
        logging(e)
        return False

    print("loaded succesfully")

bucket = "ecommerce-analytics-jayakrishnan2"
#dim_customers
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/cleaned/dim_customers.csv"
object = "clean/customers/dim_customers.csv"
print(upload_file(filename, bucket, object))


#dim_products
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/cleaned/dim_products.csv"
object = "clean/products/dim_products.csv"
print(upload_file(filename, bucket, object))

#fact_orders
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/cleaned/fact_orders.csv"
object = "clean/fact_orders/fact_orders.csv"
print(upload_file(filename, bucket, object))