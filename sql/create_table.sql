
CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id TEXT PRIMARY KEY,
    customer_unique_id TEXT,
    customer_zip_code_prefix INT,
    customer_city TEXT,
    customer_state TEXT
);


CREATE TABLE IF NOT EXISTS dim_products (
    product_id TEXT PRIMARY KEY,
    product_category_name TEXT,
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT
);



CREATE TABLE IF NOT EXISTS fact_orders (
    order_id TEXT,
    order_item_id INT,
    customer_id TEXT,
    product_id TEXT,
    order_purchase_timestamp TIMESTAMP,
    price NUMERIC,
    freight_value NUMERIC,

    PRIMARY KEY (order_id, order_item_id),

    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_products(product_id)
);


