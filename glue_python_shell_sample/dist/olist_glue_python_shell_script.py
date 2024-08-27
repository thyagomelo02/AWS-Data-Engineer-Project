import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')

def read_csv_from_s3(source_bucket, file_key):
    response = s3.get_object(Bucket=source_bucket, Key=file_key)
    data = response['Body'].read().decode('utf-8')
    return pd.read_csv(StringIO(data))

def write_csv_to_s3(destination_bucket, file_key, df):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=destination_bucket, Key=file_key, Body=csv_buffer.getvalue())

def etl_with_glue(source_bucket, destination_bucket, source_files):
    for file_key in source_files:
        try:
            df = read_csv_from_s3(source_bucket, file_key)
            if file_key == '7 olist_products_dataset.csv':
                #print(df.isnull().any()) #Looking for empty rows and columns
                df_cleaned = etl_in_producst_data_set(df)
                # Write the transformation file on the s3 destination 
                destination_key = file_key 
                write_csv_to_s3(destination_bucket, destination_key, df_cleaned)
                print("ETL process completed.")
            else:
                destination_key = file_key 
                write_csv_to_s3(destination_bucket, destination_key, df)
                print("ETL process completed.")
        except Exception as e:
            print(f"Error processing {file_key}: {e}")

def etl_in_producst_data_set(df):
    #dropping all rows wich has the followings column with blank values - for this business role is really important having the product name
    df_cleaned = df.dropna(how='all', subset=['product_category_name'])
    return df_cleaned

#Setting sourcer and destination bucket also referencing the .csv files. 
source_bucket = 'bucket-olist-raw-zone'
destination_bucket = 'bucket-olist-cleaned-zone' 
#['1 olist_orders_dataset.csv','2 olist_customers_dataset.csv','3 olist_geolocation_dataset.csv','4 olist_order_items_dataset.csv','5 olist_order_payments_dataset.csv','6 olist_order_reviews_dataset.csv','7 olist_products_dataset.csv','8 olist_sellers_dataset']
source_files = ['test_try_except.csv', '1 olist_orders_dataset.csv','2 olist_customers_dataset.csv','3 olist_geolocation_dataset.csv','4 olist_order_items_dataset.csv','5 olist_order_payments_dataset.csv','6 olist_order_reviews_dataset.csv','7 olist_products_dataset.csv','8 olist_sellers_dataset.csv']

etl_with_glue(source_bucket,destination_bucket,source_files)
