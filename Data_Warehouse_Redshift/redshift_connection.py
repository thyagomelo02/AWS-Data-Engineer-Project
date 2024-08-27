import psycopg2
import logging

logging.basicConfig(level=logging.INFO)

def create_redshift_connection():
    try:
        conn = psycopg2.connect(
            dbname='db_olist1',
            user='olist',
            password='Olist2024',
            host='Cluster ARN',
            port='5439'
        )
        print("AQUIIII")
        logging.info("Connection successful")
        return conn
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        return None
    
