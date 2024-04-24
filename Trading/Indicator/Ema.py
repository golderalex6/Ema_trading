import sys
sys.path.append('/Working/Trading')
from IMPORT import *

__location__=os.path.dirname(__file__)
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': PARA.api_key ,
    'secret': PARA.secret ,
})

#-----------Function
def Ema():
    #Calculate the Ema values

    
    index=['Date','Timestamp']
    index.extend([f'Ema_{i}' for i in range(1,101)])
    
    update_col=F.updated_columns()
    for i in update_col:

        price=[]
        date=[]
        timestamp=[]
        while True:
            try:
                get=F.handle_ohlvc(exchange.fetch_ohlcv(PARA.symbol,i,limit=1))
                break
            except:
                sleep(0.5)
        price.append(get[PARA.type].values[0])
        date.append(get['Date'].values[0])
        timestamp.append(int(get['Timestamp'].values[0]))

        data=[price for i in range(100)]
        data.insert(0,timestamp)
        data.insert(0,date)

        new_values=np.array(data[2:],dtype='float')
        
        try:
            df=pd.read_csv(os.path.join(__location__,f'Ema_{i}.csv'),index_col=0)
            k=np.array([[2/(i+1)] for i in range(1,101)])
            old_values=df.iloc[2:].to_numpy(dtype='float')

            new_ema=(np.multiply(new_values,k)+np.multiply(old_values,1-k)).tolist()
            new_ema.insert(0,timestamp)
            new_ema.insert(0,date)

            new_df=pd.DataFrame(new_ema,columns=[i],index=index)
            new_df.to_csv(os.path.join(__location__,f'Ema_{i}.csv'))
        
        except:
            
            df=pd.DataFrame(data,columns=[i],index=index)
            df.to_csv(os.path.join(__location__,f'Ema_{i}.csv'))

    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))
    print('Updated timeframe :',update_col)

def round_time():
    #wait to the nearest time frame

    sec=60
    n=dt.datetime.now().timestamp()

    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    sleep(gap)
    
def Main():
    while True:
        round_time()
        Ema()
#-----------Function

if __name__=="__main__":
    Main()
