import psycopg2
import pandas as pd
import plotly.express as px
import os

# target directory
os.chdir(r"C:\Users\chris\Desktop\covoid data")

# set up connection
conn = psycopg2.connect("dbname=dvdrental user=postgres password=2215")
cur = conn.cursor()

# reference to task
title = "Customer_Total_Spend"

# sql query
sql = ("""
SELECT customer_id, sum(amount) AS total_spend
FROM payment
GROUP BY customer_id
ORDER BY total_spend DESC
LIMIT 20
""")

# define png name object
png = f'{title}.png'

# create DataFrame object
df = pd.read_sql_query(sql, conn)
conn = None

# create plot and save
fig = px.scatter(df, x='customer_id', y='total_spend')
fig.write_image(png)

# create xlsx file
writer = pd.ExcelWriter('pandas_image.xlsx', engine='xlsxwriter')

# write df to xlsx
df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=2, startcol=1)

# define col length
col_len = len(df['total_spend']) + 1

# define workbook object
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# conditional format target values using f-sting to con_len
worksheet.conditional_format(f'B2:C{col_len}', {'type': '3_color_scale'})

# insert graph
worksheet.insert_image('D1', png)

# set col width
def Sorting(lst):
    lst.sort(key=len, reverse = True)
    return lst
      
cols_list = df.columns.values.tolist()
cols_ordered = Sorting(cols_list)
col_width = len(cols_ordered[0])

worksheet.set_column('A:B', col_width)

# save
writer.save()
