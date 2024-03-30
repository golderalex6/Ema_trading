import sys
sys.path.append('D:\\Trading')
from IMPORT import *

__location__=os.path.dirname(__file__)
client=UMFutures(PARA.api_key,PARA.secret,base_url=PARA.base_url)

#-----------Function
def handle_ohlvc(raw):
    #convert raw data crawled from binance to dataframe pandas for easy process

    df=pd.DataFrame(raw,columns=['Timestamp','Open','High','Low','Close','Volume'])
    df['Date']=df['Timestamp'].map(lambda x:dt.datetime.strftime(dt.datetime.fromtimestamp(x/1000),'%Y/%m/%d %H:%M:%S'))

    return df

def Ema():
    #Calculate the Ema values

    
    index=['Date','Timestamp']
    index.extend([f'Ema_{i}' for i in range(1,101)])
    now_min=int(dt.datetime.now().timestamp()/60)
    updated_col=[]
    for i in PARA.col:
        price=[]
        date=[]
        timestamp=[]
        if (now_min-PARA.standard_min)%PARA.tf_to_min[i]==0:
            updated_col.append(i)
            get=handle_ohlvc([client.continuous_klines(pair=PARA.symbol,contractType='PERPETUAL',interval=i,limit=1)[0][:6]])
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

    print('Updated timeframe :',updated_col)

def round_time():
    #wait to the nearest time frame

    sec=60
    n=dt.datetime.now().timestamp()

    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    sleep(gap)
    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))

def Main():
    while True:
        round_time()
        Ema()
#-----------Function

if __name__=="__main__":
    Main()