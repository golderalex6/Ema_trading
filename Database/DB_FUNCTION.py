import sqlite3 as sql
from pathlib import Path
#-----------Database connection
conn=sql.connect(str(Path(__file__).parent)+'/Main.db')
cursor=conn.cursor()
#-----------Database connection

def insert_db(table,para,multitable=False,multivalues=False):
    #multitable if user have mutiple table to insert and multivalues is for if user have mulple values to insert
    if multitable :
        for i in range(len(table)): 
            p_len=','.join(['?']*len(para[i]))
            if multivalues:
                p_len=','.join(['?']*len(para[i][0]))
                cursor.executemany(f'insert into {table[i]} values ({p_len})',para[i])
            else:
                cursor.execute(f'insert into {table[i]} values ({p_len})',para[i])
    else:

        p_len=','.join(['?']*len(para))
        if multivalues:
            p_len=','.join(['?']*len(para[0]))
            cursor.executemany(f"insert into {table} values ({p_len})",para)
        else:
            cursor.execute(f"insert into {table} values ({p_len})",para)
    conn.commit()
def query_db(query_str):
    #using normal sqlite query syntax to get datat
    cursor.execute(query_str)
    dat=cursor.fetchall()
    return dat

def delete_db(table,condition):
    #use table name and some condition to delete from table 
    cursor.execute(f'delete from {table} where {condition}')
    conn.commit()
if __name__=='__main__':
    print(query_db('select * from Open_order'))
