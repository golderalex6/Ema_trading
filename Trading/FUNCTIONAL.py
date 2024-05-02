from IMPORT import *

def handle_ohlvc(raw,timeframe):
    #convert raw data crawled from binance to dataframe pandas for easy process

    df=pd.DataFrame(raw,columns=['Timestamp','Open','High','Low','Close','Volume'])
    df['Date']=df['Timestamp'].map(lambda x:dt.datetime.strftime(dt.datetime.fromtimestamp(x/1000),'%Y/%m/%d %H:%M:%S'))
    df['Timestamp']=df['Timestamp']/1000
    df['Timeframe']=timeframe
    df=df[['Date','Timestamp','Timeframe','Open','High','Low','Close','Volume']]
    return df

def updated_columns():
    #Return the columns that need to update at that time

    now_min=int(dt.datetime.now().timestamp()/60)
    updated_col=[]
    for i in PARA.col:
        if (now_min-PARA.standard_min)%PARA.tf_to_min[i]==0:
            updated_col.append(i)
    
    return updated_col

def convert_number(data:list):
    return list(map(lambda x:str(x).replace('.',','),data))

def cross_over(fast,slow):
    #check if the fast ema is cross over the slow one

    if fast[0]<=slow[0] and fast[1]>slow[1]:
        return True
    return False

def cross_under(fast,slow):
    #check if the fast ema is cross under the slow one

    if fast[0]>=slow[0] and fast[1]<slow[1]:
        return True
    return False

def round_time(r,sec=60):
    #wait to the nearest time frame

    n=dt.datetime.now().timestamp()
    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    sleep(gap+r)


