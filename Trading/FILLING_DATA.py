from IMPORT import *

#-----------Function
def filling_data():
    #filling the missing data
    k=np.array([2/(i+1) for i in range(1,101)])
    for tf in PARA.col:
        nearest_tf = int(dt.datetime.now().timestamp()/PARA.tf_to_sec[tf])*PARA.tf_to_sec[tf]*1000-PARA.tf_to_sec[tf]*1000
        start_time=nearest_tf-200*PARA.tf_to_sec[tf]*1000

        data=get_history_bars(HYPER.symbol,tf,start_time,nearest_tf)
        price_val=data.values.tolist()
        close_price=data['Close'].values
        timestamp=data['Timestamp'].values date=data['Date'].values

        for i in range(len(close_price)):
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
