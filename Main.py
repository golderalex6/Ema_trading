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
col_index_start=np.array(['B2','C2','D2','E2','F2','G2','H2','I2','J2','K2','L2','M2'])
col_index_end=np.array(['B103','C103','D103','E103','F103','G103','H103','I103','J103','K103','L103','M103'])
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

    last=np.array(sheet.read_value_spreadsheets(sheet_id,'Ema_val!B3:M3')[0],dtype='int')
    now=np.array([dt.datetime.now().timestamp()]*12)
    time=np.array(list(tf_to_sec.values()))
    filter=(now-last)/time>1
    
    return [np.array(list(tf_to_sec.keys()))[filter],[col_index_start[filter][0],col_index_end[filter][-1]]]

def update_delay_time():
    #update the new value for Ema after the gap time

    delay_timeframe,delay_index=calculate_delay_time()
    price=[]
    date=[]
    timestamp=[]
    for i in delay_timeframe:
        get=handle_ohlvc(exchange.fetch_ohlcv(symbol,i,limit=2))
        price.append(get[type].values[0])
        date.append(get['Date'].values[0])
        timestamp.append(int(get['Timestamp'].values[0]))
    data=[price for i in range(100)]
    data.insert(0,timestamp)
    data.insert(0,date)

    write=sheet.write_value_spreadsheets(sheet_id,f'Ema_val!{delay_index[0]}:{delay_index[1]}',data)
    return write

def Ema(tf,new_price):
    rate=np.array([1.        , 0.66666667, 0.5       , 0.4       ,0.33333333,
       0.28571429, 0.25      , 0.22222222, 0.2       , 0.18181818,
       0.16666667, 0.15384615, 0.14285714, 0.13333333, 0.125     ,
       0.11764706, 0.11111111, 0.10526316, 0.1       , 0.0952381 ,
       0.09090909, 0.08695652, 0.08333333, 0.08      , 0.07692308,
       0.07407407, 0.07142857, 0.06896552, 0.06666667, 0.06451613,
       0.0625    , 0.06060606, 0.05882353, 0.05714286, 0.05555556,
       0.05405405, 0.05263158, 0.05128205, 0.05      , 0.04878049,
       0.04761905, 0.04651163, 0.04545455, 0.04444444, 0.04347826,
       0.04255319, 0.04166667, 0.04081633, 0.04      , 0.03921569,
       0.03846154, 0.03773585, 0.03703704, 0.03636364, 0.03571429,
       0.03508772, 0.03448276, 0.03389831, 0.03333333, 0.03278689,
       0.03225806, 0.03174603, 0.03125   , 0.03076923, 0.03030303,
       0.02985075, 0.02941176, 0.02898551, 0.02857143, 0.02816901,
       0.02777778, 0.02739726, 0.02702703, 0.02666667, 0.02631579,
       0.02597403, 0.02564103, 0.02531646, 0.025     , 0.02469136,
       0.02439024, 0.02409639, 0.02380952, 0.02352941, 0.02325581,
       0.02298851, 0.02272727, 0.02247191, 0.02222222, 0.02197802,
       0.02173913, 0.02150538, 0.0212766 , 0.02105263, 0.02083333,
       0.02061856, 0.02040816, 0.02020202, 0.02      , 0.01980198])
    


def round_time(tf):
    #wait to the nearest time frame

    sec=tf_to_sec[tf]
    standard_time=dt.datetime(2024,1,1,7,0).timestamp()
    while True:
        n=dt.datetime.now()
        if (int(n.timestamp())-standard_time)%sec==0:
            return

def main()->None:
    first_procedure=False
    while True:
        if not first_procedure:
            update_delay_time()
            round_time(timeframe)
            first_procedure=True
        
        sleep(tf_to_sec[timeframe])

#-----------Function

if __name__=='__main__':
    main()