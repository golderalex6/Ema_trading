from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from IMPORT import *
from Indicator import Ema
#-----------Database connection
conn=sql.connect(os.path.join(str(Path(__file__).parents[2]),'Database/Main.db'))
cursor=conn.cursor()
#-----------Database connection

#-----------Normal setup
__location__=os.path.dirname(__file__)
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': PARA.api_key ,
    'secret': PARA.secret ,
})
#-----------Normal setup

#-----------Function
def round_time():
    #wait to the nearest time frame

    sec=60
    n=dt.datetime.now().timestamp()

    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    sleep(gap)

def insert_db(table,para,multi=False):
    if multi:
        for i in range(len(table)): 
            p_len=','.join(['?']*len(para[i]))
            cursor.execute(f'insert into {table[i]} values ({p_len})',para[i])
    else:
        p_len=','.joing(['?']*len(para))
        cursor.execute(f"insert into {table} values ({p_len})",para)
    conn.commit()
        
def calculate_and_distribute():

    update_col=F.updated_columns()
    for i in update_col: 
        while True:
            cursor.execute(f'select Timestamp from Price_{i} order by Timestamp desc limit 1')
            latest=cursor.fetchall()[0][0]
            try:
                get=F.handle_ohlvc([exchange.fetch_ohlcv(PARA.symbol,i,limit=2)[0]])
                if latest==get['Timestamp'].values[0]:
                    raise
                break
            except:
                sleep(0.5)
        price=get.values[0]
        
        #Ema
        cursor.execute(f'select * from Ema_{i} order by Timestamp desc limit 1')
        old_ema=cursor.fetchall()
        if len(old_ema)==0:
            old_ema=[price[4]]*100
        else:
            old_ema=old_ema[0][2:]
        new_ema=Ema(price[4],old_ema,price[0],price[-1])
        #Ema

        #Trading
        try:
            print()
        except Exception as e:
            error_str=str(e)
            ERROR.send_error(error_str)
            raise
        #Trading
        
        #Database
        insert_db([f'Price_{i}',f'Ema_{i}'],[price,new_ema],True)
        #Database

    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))
    print('Updated timeframe :',update_col)

def Main():
    while True:
        round_time()
        calculate_and_distribute()
        #-----------Function

if __name__=="__main__":
    Main()
