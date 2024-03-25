import datetime as dt
import pandas as pd
import requests
import numpy as np
import os
import ccxt
from math import *
from time import sleep

#-----------Parameter
ema_fast=7
ema_slow=70
symbol='ETHUSDT'
timeframe='1m'
type='Close'
#-----------Parameter

#-----------Normal setup
__location__=os.path.dirname(__file__)
exchange=ccxt.binance()
col=np.array(['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d'])
#-----------Normal setup

#-----------Function
def handle_ohlvc(raw):
    #convert raw data crawled from binance to dataframe pandas for easy process

    df=pd.DataFrame(raw,columns=['Timestamp','Open','High','Low','Close','Volume'])
    df['Date']=df['Timestamp'].map(lambda x:dt.datetime.strftime(dt.datetime.fromtimestamp(x/1000),'%Y/%m/%d %H:%M:%S'))

    return df

def Ema():
    #Calculate the Ema values

    price=[]
    date=[]
    timestamp=[]
    index=['Date','Timestamp']
    index.extend([f'Ema_{i}' for i in range(1,101)])
        
    for i in col:
        get=handle_ohlvc(exchange.fetch_ohlcv(symbol,i,limit=2))
        price.append(get[type].values[0])
        date.append(get['Date'].values[0])
        timestamp.append(int(get['Timestamp'].values[0]))

    data=[price for i in range(100)]
    data.insert(0,timestamp)
    data.insert(0,date)

    new_values=np.array(data[2:])
    
    try:
        df=pd.read_csv(os.path.join(__location__,'Ema.csv'),index_col=0)
        k=np.array([[2/(i+1)] for i in range(1,101)])
        old_values=df.iloc[2:].to_numpy(dtype='float')

        new_ema=(np.multiply(new_values,k)+np.multiply(old_values,1-k)).tolist()
        new_ema.insert(0,timestamp)
        new_ema.insert(0,date)

        new_df=pd.DataFrame(new_ema,columns=col,index=index)
        new_df.to_csv(os.path.join(__location__,'Ema.csv'))
    except:
        
        df=pd.DataFrame(data,columns=col,index=index)
        df.to_csv(os.path.join(__location__,'Ema.csv'))

def round_time():
    #wait to the nearest time frame

    sec=60
    standard_time=dt.datetime(2024,1,1,7,0).timestamp()
    n=dt.datetime.now().timestamp()

    if (int(n)-standard_time)%sec==0:
        print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))
        return
    gap=ceil((n-standard_time)/sec)*sec-(n-standard_time)
    sleep(gap)
    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))

def Main():
    while True:
        Ema()
        round_time()
#-----------Function

if __name__=="__main__":
    Main()