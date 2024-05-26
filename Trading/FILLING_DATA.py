from IMPORT import *

#-----------Function
def get_history_bars(symbol, interval, start_time:int, end_time:int):

    url = f"https://data-api.binance.vision/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&endTime={end_time}&limit=1000"
    df=pd.DataFrame(requests.get(url).json())
    if (len(df.index)==0):
        return None

    df=df.iloc[:, 0:6]
    df.columns = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
    df['Date'] = [dt.datetime.strftime(dt.datetime.fromtimestamp(x/1000.0),'%Y/%m/%d %H:%M:%S') for x in df['Timestamp']]
    df['Open']=df['Open'].astype(float)
    df['High']=df['High'].astype(float)
    df['Low']=df['Low'].astype(float)
    df['Close']=df['Close'].astype(float)
    df['Volume']=df['Volume'].astype(float)
    df['Timestamp']=df['Timestamp']/1000
    df['Timeframe']=interval
    df=df[['Date','Timestamp','Timeframe','Open','High','Low','Close','Volume']]

    return df
def filling_data():
    #filling the missing data
    k=np.array([2/(i+1) for i in range(1,101)])
    for tf in PARA.col:
        nearest_tf = int(dt.datetime.now().timestamp()/PARA.tf_to_sec[tf])*PARA.tf_to_sec[tf]*1000-PARA.tf_to_sec[tf]*1000
        start_time=nearest_tf-200*PARA.tf_to_sec[tf]*1000

        data=get_history_bars('BTCUSDT',tf,start_time,nearest_tf)
        price_val=data.values.tolist()
        close_price=data['Close'].values
        timestamp=data['Timestamp'].values
        date=data['Date'].values

#         Ema=[]
#         first_val=[date[0],timestamp[0],tf]
#         first_val.extend([close_price[0]]*100)
#         Ema.append(first_val)

        for i in range(len(close_price)):
            # old_ema=Ema[-1][3:]
            # new_ema=(np.multiply(k,close_price[i])+np.multiply((1-k),old_ema)).tolist()
            # new_ema.insert(0,tf)
            # new_ema.insert(0,timestamp[i])
            # new_ema.insert(0,date[i])
            # Ema.append(new_ema)
            Ema(close_price[i],date[i],timestamp[i],tf)
        DB.insert_db('Price',price_val,False,True)
    print('Filled done !!,start draw and trade')

def round_time(r):
    #wait to the nearest time frame

    sec=60
    n=dt.datetime.now().timestamp()
    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    sleep(gap+r)
#-----------Function
if __name__=='__main__':
    round_time(10)
    filling_data()
