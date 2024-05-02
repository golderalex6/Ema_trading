import sqlite3 as sql
import os
__location__=os.path.dirname(__file__ )
conn=sql.connect(os.path.join(__location__,'Main.db'))
cursor=conn.cursor()

col=['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d']

for tf in col:
    sql_str=f'''
    select sum([Win percent]) from History where Timeframe='{tf}'
    '''

    cursor.execute(sql_str)
    conn.commit()
    m=cursor.fetchall()
    print(m)
