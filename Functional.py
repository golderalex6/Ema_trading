from IMPORT import *

def handle_ohlvc(raw):
    #convert raw data crawled from binance to dataframe pandas for easy process

    df=pd.DataFrame(raw,columns=['Timestamp','Open','High','Low','Close','Volume'])
    df['Date']=df['Timestamp'].map(lambda x:dt.datetime.strftime(dt.datetime.fromtimestamp(x/1000),'%Y/%m/%d %H:%M:%S'))

    return df

def updated_columns():
    #Return the columns that need to update at that time

    now_min=int(dt.datetime.now().timestamp()/60)
    updated_col=[]
    for i in PARA.col:
        if (now_min-PARA.standard_min)%PARA.tf_to_min[i]==0:
            updated_col.append(i)
    
    return updated_col

