import os
import boto3
from datetime import datetime

#configuration

local_folder_path = [DATA-SOURCE-LOCAL]
bucket_name = 'bucket-olist-raw-zone'  
aws_access_key_id = [AWS]
aws_secret_access_key = [AWS]
region_name = 'us-east-1' 

s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name = region_name
)

def upload_file_to_s3(folder_path, bucket_name):
    if folder_path:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.csv') or file_name.endswith('.xlsv'):
                local_file_path = os.path.join(folder_path, file_name)
                s3_client.upload_file(local_file_path, bucket_name, file_name)
                print(file_name)

upload_file_to_s3(local_folder_path, bucket_name)           
