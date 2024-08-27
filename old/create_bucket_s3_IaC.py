import json
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os

#configuration
bucket_name = 'bucket-olist'  
region_name = 'us-west-2' 
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Initializing S3 client
s3_client = boto3.client('s3', region_name=region_name)

def create_s3_bucket(bucket_name, region_name):
    try:
        if region_name == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region_name},
            )
        print(f'Bucket "{bucket_name}" has been created successful "{region_name}".')
    except ClientError as e:
        print(f'Creation Failure: {e}')

def set_bucket_policy(bucket_name):
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }
    policy_string = json.dumps(policy)
    try:
        s3_client.put_bucket_policy(
            Bucket=bucket_name,
            Policy=policy_string
        )
        print(f'Policy applied to the bucket"{bucket_name}".')
    except ClientError as e:
        print(f'Error when applying the policy: {e}')
    try:
        s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )
        print(f"Public access '{bucket_name}' ")
    except ClientError as e:
        print(f"Public access failure: {e}")

def delete_s3_bucket(bucket_name):
    s3_client = boto3.client('s3')
    # Delete all objects 
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f'Object {obj["Key"]} Deleted.')
        # Delete bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f'Bucket "{bucket_name}" deleted successful.')

    except ClientError as e:
        print(f'Delete Failure: {e}')

create_s3_bucket(bucket_name, region_name)
#set_bucket_policy(bucket_name)
#delete_s3_bucket(bucket_name)
