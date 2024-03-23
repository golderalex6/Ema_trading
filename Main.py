import ccxt
import pandas as pd
import numpy as np
import GOOGLE_SPREADSHEET as sheet
from time import sleep
import datetime as dt
from dotenv import load_dotenv
import os
load_dotenv()

#-----------Parameter
ema_fast=7
ema_slow=70
symbol='ETHUSDT'
timeframe='15m'
type='close'
#-----------Parameter

#-----------Normal setup
api_key=os.getenv('api_key')
secret=os.getenv('secret')
sheet_id='1Wp4cpdJpK3LKhI9Cf0_iRxJMzZ08YbdGaOlukZzgZLE'
timeframe={
    '1m':60,
    '3m':180,
    '5m':300,
    '15m':900,
    '30m':1800,
    '1h':3600,
    '2h':7200,
    '4h':14400,
    '6h':21600,
    '8h':28800,
    '12h':43200,
    '1d':86400
}
col_index=np.array(['B3','C3','D3','E3','F3','G3','H3','I3','J3','K3','L3','M3'])
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': api_key,
    'secret': secret,
})
exchange.set_sandbox_mode(True)
#-----------Normal setup

#-----------Function
def handle_ohlvc(raw):
    df=pd.DataFrame(raw,columns=['Timestamp','Open','High','Low','Close','Volume'])
    df['Date']=df['Timestamp'].map(lambda x:dt.datetime.fromtimestamp(x/1000))

    return df

def calculate_delay_time():
    #check time gap from the last turn off untill now

    last=np.array(sheet.read_value_spreadsheets(sheet_id,'Ema_val!B3:M3')[0],dtype='int64')
    now=np.array([dt.datetime.now().timestamp()]*12)
    time=np.array(list(timeframe.values()))
    filter=(now-last)/time>1

    return [np.array(list(timeframe.keys()))[filter],col_index[filter]]

def update_delay_time():
    #update the new value for Ema after the gap time

    delay_timeframe,delay_index=calculate_delay_time()
    price=handle_ohlvc(exchange.fetch_ohlcv(symbol,timeframe,limit=1))[type]
    
def round_time():
    #wait to the nearest time frame

    standard_time=dt.datetime(2024,1,1,7,0).timestamp()
    while True:
        n=dt.datetime.now()
        if (int(n.timestamp())-standard_time)%60==0:
            print(n,n.timestamp())
            return

def main()->None:
    pass
#-----------Function

if __name__=='__main__':
    main()