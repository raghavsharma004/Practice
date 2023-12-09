# -*- coding: utf-8 -*-
"""
Spyder Editor
print ("hello")
This is a temporary script file
"""
import psycopg2

conn = psycopg2.connect(
    host="postgres-1.crxwlc1o3uct.us-east-1.rds.amazonaws.com",
    port=5432,
    user="postgres",
    password="pa55w0rd"
    
    )

conn.autocommit=True

db_create_query = """insert into newdb.emp(name) values('rag')"""

cursor = conn.cursor()

cursor.execute(db_create_query)

conn.close()



