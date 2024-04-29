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
def round_time():
    #wait to the nearest time frame

    sec=60
    n=dt.datetime.now().timestamp()

    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    sleep(gap)

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
    while True:
        round_time()
        try:
            calculate_and_distribute()
        except Exception as e:
            error_str='Error from Data.py '+ str(e)
            ERROR.send_error(error_str)
            raise
#-----------Function

if __name__=="__main__":
    Main()
