import psycopg2
import pandas as pd
import xlsxwriter
import plotly.express as px
import os
os.chdir(r"C:\Users\chris\Desktop\covoid data")

# Set up connection
conn = psycopg2.connect("dbname=dvdrental user=postgres password=2215")
cur = conn.cursor()

# Reference to task
title = "Customer_Total_Spend"

sql = ("""

SELECT customer_id, sum(amount)
FROM payment
GROUP BY customer_id
ORDER BY customer_id

""")

png = f'{title}.png'
    
df = pd.read_sql_query(sql, conn)
conn = None
fig = px.scatter(df, x='customer_id', y='sum')
fig.write_image(png)

workbook = xlsxwriter.Workbook('images.xlsx')
worksheet = workbook.add_worksheet(name='Graph')
worksheet.insert_image('B5', png)
workbook.close()


with pd.ExcelWriter('images.xlsx', engine='openpyxl', mode='a') as writer: 
     df.to_excel(writer, sheet_name='Data', index=False)
