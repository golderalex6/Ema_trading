from IMPORT import * 
#-----------Normal setup
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': PARA.api_key ,
    'secret': PARA.secret ,
})
#-----------Normal setup

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

        Ema=[]
        first_val=[date[0],timestamp[0]]
        first_val.extend([close_price[0]]*100)
        Ema.append(first_val)

        for i in range(1,len(close_price)):
            old_ema=Ema[-1][2:]
            new_ema=(np.multiply(k,close_price[i])+np.multiply((1-k),old_ema)).tolist()
            new_ema.insert(0,timestamp[i])
            new_ema.insert(0,date[i])
            Ema.append(new_ema)

        DB.insert_db([f'Price_{tf}',f'Ema_{tf}'],[price_val,Ema],True,True)
    print('Filled done !!,start draw and trade')

def round_time(r):
    #wait to the nearest time frame

    sec=60
    n=dt.datetime.now().timestamp()
    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    sleep(gap+r)

def get_and_compare_data(tf):
    #get the new data and make sure not get the duplicate data
    latest=DB.query_db(f'select Timestamp from Price_{tf} order by Timestamp desc limit 1')
    while True:
        try:
            get=F.handle_ohlvc([exchange.fetch_ohlcv(PARA.symbol,tf,limit=2)[0]])
            if len(latest)!=0:
                if latest[0][0]==get['Timestamp'].values[0]:raise
            break
        except:
            sleep(0.5)
    return get.values[0]


def calculate_and_distribute():

    update_col=F.updated_columns()
    for i in update_col: 

        price=get_and_compare_data(i)
        #Ema
        old_ema=DB.query_db(f'select * from Ema_{i} order by Timestamp desc limit 1')
        old_ema=[price[4]]*100 if len(old_ema)==0 else old_ema[0][2:]
        new_ema=Ema(price[4],old_ema,price[0],price[-1])
        #Database
        DB.insert_db([f'Price_{i}',f'Ema_{i}'],[price,new_ema],True)

    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))
    print('Updated timeframe :',update_col)

def Main():
    #Error handling
    round_time(10)
    filling_data()
    while True:
        round_time(0)
        try:
            calculate_and_distribute()
        except Exception as e:
            error_str='Error from Data.py '+ str(e)
            ERROR.send_error(error_str)
            raise
#-----------Function

if __name__=="__main__":
    Main()
