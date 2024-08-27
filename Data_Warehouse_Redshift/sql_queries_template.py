
#Dropping table if exists

olist_geolocation_table_drop = "DROP TABLE IF EXISTS olist_geolocation;"
olist_sellers_table_drop = "DROP TABLE IF EXISTS olist_sellers;"
olist_products_table_drop = "DROP TABLE IF EXISTS olist_products;"
olist_customers_table_drop = "DROP TABLE IF EXISTS olist_customers;"
olist_orders_table_drop = "DROP TABLE IF EXISTS olist_orders;"
olist_order_payments_table_drop = "DROP TABLE IF EXISTS olist_order_payments;"
olist_order_reviews_table_drop = "DROP TABLE IF EXISTS olist_order_reviews;"
olist_order_items_table_drop = "DROP TABLE IF EXISTS olist_order_items;"


olist_geolocation_table = ("""
CREATE TABLE IF NOT EXISTS olist_geolocation
(
    geolocation_zip_code_prefix VARCHAR(5) PRIMARY KEY,
    geolocation_lat DECIMAL(2,18),
    geolocation_lng DECIMAL(3,18),
    geolocation_city VARCHAR(64),
    geolocation_state VARCHAR(2)
);
""")

olist_sellers_table = ("""
CREATE TABLE IF NOT EXISTS olist_sellers
(
   seller_id VARCHAR(32) PRIMARY KEY,
   seller_zip_code_prefix VARCHAR(5),
   seller_city VARCHAR(64),
   seller_state VARCHAR(2),
   FOREIGN KEY (seller_zip_code_prefix) REFERENCES olist_geolocation(geolocation_zip_code_prefix)                                                                
);
""")

olist_products_table = ("""
CREATE TABLE IF NOT EXISTS olist_products
(
    product_id VARCHAR(32) PRIMARY KEY,
    product_category_name VARCHAR(32),
    product_name_lenght INTEGER,
    product_description_lenght INTEGER,
    product_photos_qty INTEGER,
    product_weight_g FLOAT,
    product_length_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT                                     
);
""")

olist_customers_table = ("""
CREATE TABLE IF NOT EXISTS olist_customers
(
   customer_unique_id VARCHAR(32) PRIMARY KEY,
   customer_id VARCHAR(32),
   customer_zip_code_prefix VARCHAR(5),
   customer_city VARCHAR(64),
   customer_state VARCHAR(2),
   FOREIGN KEY (customer_id) REFERENCES olist_orders(customer_id)
   FOREIGN KEY (customer_zip_code_prefix) REFERENCES olist_geolocation(geolocation_zip_code_prefix)   
);
""")

olist_orders_table = ("""
CREATE TABLE IF NOT EXISTS olist_orders
(
   order_id VARCHAR(32) PRIMARY KEY,
   customer_id VARCHAR(32),
   order_status VARCHAR(15),
   order_purchase_timestamp TIMESTAMP,
   order_approved_at DATETIME,
   order_delivered_carrier_date DATETIME,
   order_delivered_customer_date DATETIME,
   order_estimated_delivery_date DATETIME,
   FOREIGN KEY (customer_id) REFERENCES olist_customers(customer_id)
);
""")

olist_order_payments_table = ("""
CREATE TABLE IF NOT EXISTS olist_order_payments
(
    order_id VARCHAR(32),
    payment_sequential INTEGER,
    payment_type VARCHAR(18),
    payment_installments INTEGER,
    payment_value DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES olist_orders(order_id)
);
""")

olist_order_reviews_table = ("""
CREATE TABLE IF NOT EXISTS olist_order_reviews
(
   review_id VARCHAR(32) PRIMARY KEY,
   order_id VARCHAR(32),
   review_score INT,
   review_comment_title TEXT,
   review_comment_message TEXT,
   review_creation_date DATETIME,
   review_answer_timestamp TIMESTAMP,
   FOREIGN KEY (order_id) REFERENCES olist_orders(order_id)
);
""")

olist_order_items_table = ("""
CREATE TABLE IF NOT EXISTS olist_order_items
(
    order_item_id VARCHAR(32) PRIMARY KEY,
    order_id VARCHAR(32),
    product_id VARCHAR(32),
    seller_id VARCHAR(32),
    shipping_limit_date DATETIME,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES olist_orders(order_id),
    FOREIGN KEY (product_id) REFERENCES olist_products(product_id),
    FOREIGN KEY (seller_id) REFERENCES olist_sellers(seller_id)
);
""")

create_tables = [olist_order_items_table, olist_sellers_table, olist_products_table, olist_customers_table, olist_orders_table, olist_order_payments_table, olist_order_reviews_table, olist_order_items_table]
drop_tables = [olist_geolocation_table_drop, olist_sellers_table_drop, olist_products_table_drop, olist_customers_table_drop, olist_orders_table_drop, olist_order_payments_table_drop, olist_order_reviews_table_drop, olist_order_items_table_drop]

