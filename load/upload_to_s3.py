import boto3
import logging
from botocore.exceptions import ClientError
import os



#checking & validating name of bucket
s3_client = boto3.client('s3')

response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])


def upload_file(filename, bucket, object_Name=None):

    if object_Name is None:
        object_Name = os.path.basename(filename)

    try:
        response = s3_client.upload_file(filename, bucket, object_Name)
    except ClientError as e:
        logging(e)
        return False

    return object_Name +" successfully uploaded"

bucket = "ecommerce-analytics-jayakrishnan2"
#customers
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce/customers.csv"
object_Name = "raw/customers/customers.csv"

print(upload_file(filename, bucket, object_Name))

#geolocation
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce/geolocation.csv"
object_Name = "raw/geolocation/geolocation.csv"


print(upload_file(filename, bucket, object_Name))

#order_items
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce/order_items.csv"
object_Name = "raw/order_items/order_items.csv"

print(upload_file(filename, bucket, object_Name))

#order_payments
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce/order_payments.csv"
object_Name = "raw/order_payments/order_payments.csv"

print(upload_file(filename, bucket, object_Name))

#order_reviews
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce/order_reviews.csv"
object_Name = "raw/order_reviews/order_reviews.csv"

print(upload_file(filename, bucket, object_Name))


#orders
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce/orders.csv"
object_Name = "raw/orders/orders.csv"

print(upload_file(filename, bucket, object_Name))


#product_category_name_translation
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce/product_category_name_translation.csv"
object_Name = "raw/product_category_name_translation/product_category_name_translation.csv"

print(upload_file(filename, bucket, object_Name))


#products
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce/products.csv"
object_Name = "raw/products/products.csv"

print(upload_file(filename, bucket, object_Name))


#sellers
filename = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce/sellers.csv"
object_Name = "raw/sellers/sellers.csv"

print(upload_file(filename, bucket, object_Name))
