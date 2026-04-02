import os
import pandas as pd



folder_path = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/raw/brazilian-ecommerce"

def transformed_data():
    folder = os.listdir(folder_path)


    file_location_list = {}

    #checking all the columns name

    for file in folder:
        if file.endswith(".csv"):
            filename = file.removesuffix(".csv")
            file_location_list[filename] = folder_path+'/'+file
            df = pd.read_csv(folder_path+"/"+file)
            print("filename: "+file)
            print(df.columns.to_list())


    #checking data name and its storage
    #only checking the data with requirement - customers, orders, order_items, products

    for key,value in file_location_list.items():
        if key == "customers":
            df_customers = pd.read_csv(value)

        if key == "orders":
            df_orders = pd.read_csv(value)
        
        if key == "order_items":
            df_order_items = pd.read_csv(value)
        
        if key == "products":
            df_products = pd.read_csv(value)
        print(f"{key}:{value}")
        print()




    #checking data info

    def check_dtype(path):
        dataframe = pd.read_csv(path)

        print(dataframe.dtypes)

        print()

        return dataframe.info()

    #checking
    for key,value in file_location_list.items():
        if key in ["customers", "orders", "order_items", "products"]:
            print(key)
            print(check_dtype(value))
            print("----------------end----------------")
            print()


    #changing data types

    #df_products
    df_products.rename(columns={"product_name_lenght":"product_name_length",
                                "product_description_lenght":"product_description_length"}, inplace=True)


    df_order_items["shipping_limit_date"] = pd.to_datetime(df_order_items["shipping_limit_date"])

    print(df_order_items["shipping_limit_date"].head())
    # df_orders


    orders_list_change = ["order_purchase_timestamp","order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date"]

    for i in orders_list_change:
        df_orders[i] = pd.to_datetime(df_orders[i])


    print(df_orders[["order_purchase_timestamp", 
                    "order_approved_at", "order_delivered_carrier_date", 
                    "order_delivered_customer_date", "order_estimated_delivery_date"]].dtypes)


    #null types

    print("----------------------start------------------------------")
    print(df_customers.isnull().sum())
    print("----------------------end--------------------------------")
    print()

    print("----------------------start------------------------------")
    print(df_orders.isnull().sum())
    print("----------------------end--------------------------------")
    print()

    print("----------------------start------------------------------")
    print(df_order_items.isnull().sum())
    print("----------------------end--------------------------------")
    print()

    print("----------------------start------------------------------")
    print(df_products.isnull().sum())
    print("----------------------end--------------------------------")
    print()




    #fill nulls
    df_products["product_category_name"] = df_products["product_category_name"].fillna("unknown")
    df_products["product_name_length"] = df_products["product_name_length"].fillna(0)
    df_products["product_description_length"] = df_products["product_description_length"].fillna(0)
    df_products["product_photos_qty"] = df_products["product_photos_qty"].fillna(0)
    df_products["product_weight_g"] = df_products["product_weight_g"].fillna(0) 
    df_products["product_length_cm"] = df_products["product_length_cm"].fillna(0)
    df_products["product_height_cm"] = df_products["product_height_cm"].fillna(0)
    df_products["product_width_cm"] = df_products["product_width_cm"].fillna(0)


    #final check for null

    print("----------------------start------------------------------")
    print(df_customers.isnull().sum())
    print("----------------------end--------------------------------")
    print()

    print("----------------------start------------------------------")
    print(df_orders.isnull().sum())
    print("----------------------end--------------------------------")
    print()

    print("----------------------start------------------------------")
    print(df_order_items.isnull().sum())
    print("----------------------end--------------------------------")
    print()

    print("----------------------start------------------------------")
    print(df_products.isnull().sum())
    print("----------------------end--------------------------------")
    print()

    #check for duplicates
    print(df_customers.duplicated().sum())
    print(df_orders.duplicated().sum())
    print(df_order_items.duplicated().sum())
    print(df_products.duplicated().sum())


    #creating dim_table products, customers

    dim_products = df_products[["product_id", "product_category_name", "product_name_length", "product_description_length", "product_photos_qty"]]
    dim_products = dim_products.drop_duplicates(subset="product_id")

    dim_customers = df_customers[["customer_id","customer_unique_id", "customer_zip_code_prefix","customer_city","customer_state"]]
    dim_customers = dim_customers.drop_duplicates(subset="customer_id")


    #creating fact table from orders, order_items table
    df_orders_dim = df_orders[["order_id", "customer_id", "order_purchase_timestamp"]]
    df_order_items_dim = df_order_items[["order_id", "order_item_id", "product_id", "price", "freight_value"]]

    fact_orders = pd.merge(df_orders_dim, df_order_items_dim, on = "order_id", how='inner')

    base_path = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/extract/cleaned"

    os.makedirs(base_path, exist_ok = True)

    dim_products.to_csv(f"{base_path}/dim_products.csv", index=False)
    dim_customers.to_csv(f"{base_path}/dim_customers.csv", index=False)
    fact_orders.to_csv(f"{base_path}/fact_orders.csv",index=False)
    
    return dim_products, dim_customers, fact_orders




