import configparser
from sql_queries_template import create_tables, drop_tables
from redshift_connection import create_redshift_connection

def drop_all_tables(cur, conn):
    for drop_table in drop_tables:
        cur.execute(drop_table)
        conn.commit()

def create_tables(cur, conn):
    for create_table in create_tables:
        cur.execute(create_table)
        conn.commit()


config = configparser.ConfigParser()

conn = create_redshift_connection()

if conn is not None:
    cur  = conn.cursor()
    drop_all_tables(cur, conn)
    create_tables(cur, conn)
    cur.close()
    conn.close()
else:
    print("erro de conexção")
