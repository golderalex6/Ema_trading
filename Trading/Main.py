from IMPORT import *

#-----------Normal setup
__location__=os.path.dirname(__file__)
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

def trading_log(date:str,order_type:str,amount:float,open:float,close:float):
    #write trading history for future query
    
    fee=0.002
    total_fee=fee*(amount+amount*close/open)

    win_per=None
    if order_type=='BUY':
        win_per=(close-open)/open
    else:
        win_per=(open-close)/close

    win_usd=amount*win_per-total_fee
    history_log=[date,order_type,total_fee,amount,open,close,win_per,win_usd]

def main(cursor:sqlite3.Cursor,old_ema,new_ema,timeframe)->None:
    #check if the timeframe passed is valid
    if timeframe!=PARA.timeframe:
        return

    #run the trading application
    
    fast_old,slow_old=old_ema[PARA.ema_fast+1],old_ema[PARA.ema_slow+1]
    fast_new,slow_new=new_ema[PARA.ema_fast+1],new_ema[PARA.ema_slow+1]
    fast,slow=[fast_old,fast_new],[slow_old,slow_new]
    
    now=dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S')
                
    order_books=exchange.fetch_order_book(PARA.symbol,limit=5)

    cursor.execute('select * from Open_order')
    open_order=(False,cursor.fetchall()[0])[len(cursor.fetchall())==0]

    if cross_over(fast,slow):
        #close the sell order and create a new buy order

        print(now,'Buy')
        if open_order:
            latest_quant=open_order[1]
            #PLACE MARKET BUY ORDER WITH QUANTITY ABOVE 
            close_price=float(order_books['asks'][0][0]) 
            trading_log(now,'SELL',latest_quant,open_price,close_price)

        quantity=round_down_nth(PARA.balance/float(order_books['asks'][0][0]),3)
        #PLACE MARKET BUY ORDER WITH QUANTITY ABOVE
        open_price=float(order_books['asks'][0][0])
        cursor.execute('insert into Open_order values (?,?,?)')

    if cross_under(fast,slow):
        #close the buy order and create a new sell order

        print(now,'Sell')
        if open_order:
            latest_quant=open_order[1]
            #PLACE MARKET SELL ORDER WITH QUANTITY ABOVE 
            close_price=float(order_books['bids'][0][0])
            trading_log(now,'BUY',latest_quant,open_price,close_price)

        quantity=round_down_nth(PARA.balance/float(order_books['bids'][0][0]),3)
        #PLACE MARKET SELL ORDER WITH QUANTITY ABOVE
        open_price=float(order_books['bids'][0][0])
    
#-----------Function
if __name__=='__main__':
    main()
