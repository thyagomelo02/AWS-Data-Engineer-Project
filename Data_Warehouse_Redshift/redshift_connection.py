import psycopg2
import logging

logging.basicConfig(level=logging.INFO)

def create_redshift_connection():
    try:
        conn = psycopg2.connect(
            dbname='db_olist1',
            user='olist',
            password='Olist2024',
            host='olist-redshiftcluter.cme8c8uumlvh.us-east-1.redshift.amazonaws.com',
            port='5439'
        )
        print("AQUIIII")
        logging.info("Connection successful")
        return conn
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        return None
    
#ParameterKey=MasterUsername,ParameterValue=olist ParameterKey=MasterUserPassword,ParameterValue=Olist2024 ParameterKey=DatabaseName,ParameterValue=db_olist1 ParameterKey=ClusterType,ParameterValue=single-node ParameterKey=NumberOfNodes,ParameterValue=1 ParameterKey=S3BucketName,ParameterValue=bucket-olist-cleaned-zone ParameterKey=VpcCidr,ParameterValue=10.0.0.0/16 ParameterKey=SubnetCidr1,ParameterValue=10.0.1.0/24 ParameterKey=SubnetCidr2,ParameterValue=10.0.2.0/24 --capabilities CAPABILITY_NAMED_IAM --region us-east-1