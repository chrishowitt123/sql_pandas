import psycopg2
import pandas as pd

conn = psycopg2.connect("dbname=dvdrental user=postgres password=2215")
cur = conn.cursor()

sql = ("""SELECT * from payment""")
    
df = pd.read_sql_query(sql, conn)
conn = None
df
