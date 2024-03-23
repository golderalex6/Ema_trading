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
#-----------Parameter

#-----------Normal setup
api_key=os.getenv('api_key')
secret=os.getenv('secret')
sheet_id='1Wp4cpdJpK3LKhI9Cf0_iRxJMzZ08YbdGaOlukZzgZLE'
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': api_key,
    'secret': secret,
})
exchange.set_sandbox_mode(True)
#-----------Normal setup

#-----------Function
def convert(timeframe):
    #convert timeframe to second
    time={
        'm':60,
        'h':3600,
        'd':86400
    }
    try:
        index=int(timeframe[:-1])
        return index*time[timeframe[-1]]
    except:
        print('Wrong timeframe format !!')

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