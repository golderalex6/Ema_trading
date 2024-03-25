import ccxt
import pandas as pd
import numpy as np
import GOOGLE_SPREADSHEET as sheet
from time import sleep
import datetime as dt
from dotenv import load_dotenv
import os
load_dotenv()
from math import *

#-----------Parameter
ema_fast=7
ema_slow=70
symbol='ETHUSDT'
timeframe='1m'
type='Close'
balance=100
#-----------Parameter

#-----------Normal setup
__location__=os.path.dirname(__file__)
api_key=os.getenv('api_key_test')
secret=os.getenv('secret_test')
sheet_id='1Wp4cpdJpK3LKhI9Cf0_iRxJMzZ08YbdGaOlukZzgZLE'

tf_to_sec={
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
col=np.array(['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d'])

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
    #convert raw data crawled from binance to dataframe pandas for easy process

    df=pd.DataFrame(raw,columns=['Timestamp','Open','High','Low','Close','Volume'])
    df['Date']=df['Timestamp'].map(lambda x:dt.datetime.strftime(dt.datetime.fromtimestamp(x/1000),'%Y/%m/%d %H:%M:%S'))

    return df

def round_time(tf):
    #wait to the nearest time frame

    sec=tf_to_sec[tf]
    standard_time=dt.datetime(2024,1,1,7,0).timestamp()
    n=dt.datetime.now().timestamp()

    if (int(n)-standard_time)%sec==0:
        print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))
        return
    gap=ceil((n-standard_time)/sec)*sec-(n-standard_time)
    sleep(gap)
    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))

def cross_over(fast,slow):
    #check if the fast ema is cross over the slow one

    if fast[0]<=slow[0] and fast[1]>slow[1]:
        return True
    else:
        return False

def cross_under(fast,slow):
    #check if the fast ema is cross under the slow one

    if fast[0]>=slow[0] and fast[1]<slow[1]:
        return True
    else:
        return False

def trading_log():
    #write
    pass


def main()->None:
    #run the trading application
    check=pd.read_csv(os.path.join(__location__,'Indicator\\Ema.csv'),index_col=0)

    while True:
        new=pd.read_csv(os.path.join(__location__,'Indicator\\Ema.csv'),index_col=0)

        if not check.equals(new):

            fast_old,slow_old=check.loc[[f'Ema_{ema_fast}',f'Ema_{ema_slow}'],timeframe].values
            fast_new,slow_new=new.loc[[f'Ema_{ema_fast}',f'Ema_{ema_slow}'],timeframe].values
            fast,slow=[fast_old,fast_new],[slow_old,slow_new]
            
            now=dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S')
            traded=False

            if cross_over(fast,slow):
                print(now,'Buy')
                traded=True
            if cross_under(fast,slow):
                print(now,'Sell')
                traded=True
            if traded==False:
                print(now,fast,slow)
            check=new
        else:
            print('No update')
        sleep(0.5)
        
#-----------Function

if __name__=='__main__':
    main()