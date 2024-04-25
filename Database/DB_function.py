import sqlite3 as sql
from pathlib import Path
#-----------Database connection
conn=sql.connect(str(Path(__file__).parent)+'/Main.db')
cursor=conn.cursor()
#-----------Database connection

def insert_db(table,para,multi=False):
    if multi:
        for i in range(len(table)): 
            p_len=','.join(['?']*len(para[i]))
            cursor.execute(f'insert into {table[i]} values ({p_len})',para[i])
    else:
        p_len=','.joing(['?']*len(para))
        cursor.execute(f"insert into {table} values ({p_len})",para)
    conn.commit()

def query_db(query_str):
    cursor.execute(query_str)
    dat=cursor.fetchall()
    return dat


