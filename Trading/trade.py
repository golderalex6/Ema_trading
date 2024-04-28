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

def trading_log(date:str,order_type:str,amount:float,open:float,close:float):
    #write trading history for future query
    
    fee=0.002
    total_fee=fee*(amount+amount*close/open)

    win_per=(-1,1)[order_type=='SELL']*(open-close)/open
    win_usd=amount*win_per-total_fee
    history_log=[date,order_type,total_fee,amount,open,close,win_per,win_usd]
    DB.insert_db('History',history_log)

def Trade()->None:
    #run the trading application
    tf=input('Select your timeframe:')
    while tf not in PARA.col:
        tf=input('Please choose again:')
    old_ema=DB.query_db(f'select * from Ema_{tf} order by Timestamp desc limit 1')
    while True:
        new_ema=DB.query_db(f'select * from Ema_{tf} order by Timestamp desc limit 1')
        if old_ema!=new_ema and len(old_ema)>0:
            fast_old,slow_old=old_ema[0][PARA.ema_fast+1],old_ema[0][PARA.ema_slow+1]
            fast_new,slow_new=new_ema[0][PARA.ema_fast+1],new_ema[0][PARA.ema_slow+1]
            fast,slow=[fast_old,fast_new],[slow_old,slow_new]
            
            now=dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S')
            open_order=DB.query_db('select * from Open_order')
            #reduce number of requests created
            if F.cross_over(fast,slow) or F.cross_under(fast,slow):
                order_books=exchange.fetch_order_book(PARA.symbol,limit=5)

            if F.cross_over(fast,slow):
                #close the sell order and create a new buy order

                print(now,'Buy')
                if open_order:
                    latest_quant=open_order[0][1]
                    open_price=open_order[0][2]
                    #PLACE MARKET BUY ORDER WITH QUANTITY ABOVE 
                    DB.delete_db('Open_order',"[Order type]='SELL'")
                    close_price=float(order_books['asks'][0][0]) 
                    trading_log(now,'SELL',latest_quant,open_price,close_price)

                quantity=round_down_nth(PARA.balance/float(order_books['asks'][0][0]),3)
                #PLACE MARKET BUY ORDER WITH QUANTITY ABOVE
                open_price=float(order_books['asks'][0][0])
                DB.insert_db('Open_order',['BUY',quantity,open_price])

            if F.cross_under(fast,slow):
                #close the buy order and create a new sell order

                print(now,'Sell')
                if open_order:
                    latest_quant=open_order[0][1]
                    open_price=open_order[0][2]
                    #PLACE MARKET SELL ORDER WITH QUANTITY ABOVE 
                    DB.delete_db('Open_order',"[Order type]='BUY'") 
                    close_price=float(order_books['bids'][0][0])
                    trading_log(now,'BUY',latest_quant,open_price,close_price)

                quantity=round_down_nth(PARA.balance/float(order_books['bids'][0][0]),3)
                #PLACE MARKET SELL ORDER WITH QUANTITY ABOVE
                open_price=float(order_books['bids'][0][0])
                DB.insert_db('Open_order',['SELL',quantity,open_price])
        else:
            sleep(0.5)
        old_ema=new_ema 

def Main():
    #Error handling
    try:
        Trade()
    except Exception as e:
        error_str='Error from trade.py '+str(e)
        ERROR.send_error(error_str)
        raise
#-----------Function
if __name__=='__main__':
    Main()
