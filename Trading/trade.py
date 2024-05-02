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
def round_down_nth(d,n):
    return floor(d*10**(n))/10**n

def trading_log(timestamp:int,order_type:str,amount:float,open:float,close:float,timeframe:str):
    #write trading history for future query
    
    date_str=dt.datetime.strftime(dt.datetime.fromtimestamp(timestamp),'%Y/%m/%d %H:%M:%S')
    fee=0.002
    total_fee=fee*(amount+amount*close/open)

    win_per=(-1,1)[order_type=='SELL']*(open-close)/open
    win_usd=amount*win_per-total_fee
    history_log=[date_str,timestamp,timeframe,order_type,total_fee,amount,open,close,win_per,win_usd]
    DB.insert_db('History',history_log)

def Trade(tf)->None:
    #run the trading application
    old_ema=DB.query_db(f"select * from Ema where Timeframe='{tf}' order by Timestamp desc limit 1")
    while True:
        new_ema=DB.query_db(f"select * from Ema where Timeframe='{tf}' order by Timestamp desc limit 1")
        if old_ema!=new_ema and len(old_ema)>0:
            fast_old,slow_old=old_ema[0][HYPER.ema_fast+2],old_ema[0][HYPER.ema_slow+2]
            fast_new,slow_new=new_ema[0][HYPER.ema_fast+2],new_ema[0][HYPER.ema_slow+2]
            fast,slow=[fast_old,fast_new],[slow_old,slow_new]
            # print(fast,slow)
            now=dt.datetime.now().timestamp()
            open_order=DB.query_db('select * from Open_order')
            #reduce number of requests created
            if F.cross_over(fast,slow) or F.cross_under(fast,slow):
                order_books=exchange.fetch_order_book(HYPER.symbol,limit=5)

            if F.cross_over(fast,slow):
                #close the sell order and create a new buy order

                print(dt.datetime.strftime(dt.datetime.fromtimestamp(now),'%Y/%m/%d %H:%M:%S'),'Buy')
                if open_order:
                    latest_quant=open_order[0][1]
                    open_price=open_order[0][2]
                    #PLACE MARKET BUY ORDER WITH QUANTITY ABOVE 
                    DB.delete_db('Open_order',"[Order type]='SELL'")
                    close_price=float(order_books['asks'][0][0]) 
                    trading_log(now,'SELL',latest_quant,open_price,close_price,tf)

                quantity=round_down_nth(HYPER.balance/float(order_books['asks'][0][0]),3)
                #PLACE MARKET BUY ORDER WITH QUANTITY ABOVE
                open_price=float(order_books['asks'][0][0])
                DB.insert_db('Open_order',['BUY',quantity,open_price])

            if F.cross_under(fast,slow):
                #close the buy order and create a new sell order

                print(dt.datetime.strftime(dt.datetime.fromtimestamp(now),'%Y/%m/%d %H:%M:%S'),'Sell')
                if open_order:
                    latest_quant=open_order[0][1]
                    open_price=open_order[0][2]
                    #PLACE MARKET SELL ORDER WITH QUANTITY ABOVE 
                    DB.delete_db('Open_order',"[Order type]='BUY'") 
                    close_price=float(order_books['bids'][0][0])
                    trading_log(now,'BUY',latest_quant,open_price,close_price,tf)

                quantity=round_down_nth(HYPER.balance/float(order_books['bids'][0][0]),3)
                #PLACE MARKET SELL ORDER WITH QUANTITY ABOVE
                open_price=float(order_books['bids'][0][0])
                DB.insert_db('Open_order',['SELL',quantity,open_price])
        else:
            sleep(0.5)
        old_ema=new_ema 

def main():
    #Error handling
    check_input=len(sys.argv)
    if check_input==1:
        tf=input('Select your timeframe:')
    else:
        tf=sys.argv[1]
    while tf not in PARA.col:
        tf=input('Please choose again:')
    try:
        Trade(tf)
    except Exception as e:
        error_str='Error from Trading/trade.py:'+str(e)
        ERROR.send_error(error_str)
        raise
#-----------Function
if __name__=='__main__':
    main()
