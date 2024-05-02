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
def get_and_compare_data(tf):
    #get the new data and make sure not get the duplicate data
    latest=DB.query_db(f"select Timestamp from Price where Timeframe='{tf}' order by Timestamp desc limit 1")
    while True:
        try:
            get=F.handle_ohlvc([exchange.fetch_ohlcv(HYPER.symbol,tf,limit=2)[0]],tf)
            if len(latest)!=0:
                if latest[0][0]==get['Timestamp'].values[0]:raise
            break
        except:
            sleep(0.5)
    return get.values[0]


def calculate_and_distribute():

    update_col=F.updated_columns()
    for tf in update_col:

        price=get_and_compare_data(tf)
        #Ema
        old_ema=DB.query_db(f"select * from Ema where Timeframe='{tf}' order by Timestamp desc limit 1")
        old_ema=[price[6]]*100 if len(old_ema)==0 else old_ema[0][3:]
        new_ema=Ema(price[6],old_ema,price[1],price[0],tf)
        #Database
        DB.insert_db([f'Price',f'Ema'],[price,new_ema],True)

    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))
    print('Updated timeframe :',update_col)

def Main():
    #Error handling
    while True:
        F.round_time(0)
        try:
            calculate_and_distribute()
        except Exception as e:
            error_str='Error from Trading/data.py :'+ str(e)
            ERROR.send_error(error_str)
            raise
#-----------Function

if __name__=="__main__":
    Main()
