import psycopg2
import pandas as pd
import plotly.express as px

conn = psycopg2.connect("dbname=dvdrental user=postgres password=2215")
cur = conn.cursor()

sql = ("""


SELECT customer_id, sum(amount)
FROM payment
GROUP BY customer_id
ORDER BY customer_id



""")
    
df = pd.read_sql_query(sql, conn)
conn = None
fig = px.scatter(df, x='customer_id', y='sum')
fig.show()
