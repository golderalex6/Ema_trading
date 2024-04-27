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
            print(f'insert into {table[i]} values ({p_len})')
            cursor.execute(f'insert into {table[i]} values ({p_len})',para[i])
    else:
        p_len=','.join(['?']*len(para))
        cursor.execute(f"insert into {table} values ({p_len})",para)
    conn.commit()

def query_db(query_str):
    cursor.execute(query_str)
    dat=cursor.fetchall()
    return dat

def delete_db(table,condition):
    cursor.execute(f'delete from {table} where {condition}')
    conn.commit()
