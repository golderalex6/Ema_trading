import sqlite3 as sql
import os
__location__=os.path.dirname(__file__ )
conn=sql.connect(os.path.join(__location__,'Main.db'))
cursor=conn.cursor()

sql_str='''
select * from Open_order 
'''

cursor.execute(sql_str)
conn.commit()
print(cursor.fetchall())
