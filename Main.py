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
    history_log=F.convert_number(history_log)

    sheet.append_value_spreadsheets(PARA.sheet_id,'Trading_log!A1:H1',[history_log])

def main()->None:
    #run the trading application
    check=pd.read_csv(os.path.join(__location__,f'Indicator/Ema_{PARA.timeframe}.csv'),index_col=0)
    
    open_position=False
    latest_quant=None
    open_price=None
    close_price=None
    
    while True:
        while True:
            try:
                new=pd.read_csv(os.path.join(__location__,f'Indicator/Ema_{PARA.timeframe}.csv'),index_col=0)
                break
            except:
                sleep(0.5)

        if not check.equals(new):
            
            #Get the Ema value
            fast_old,slow_old=check.loc[[f'Ema_{PARA.ema_fast}',f'Ema_{PARA.ema_slow}']].values
            fast_new,slow_new=new.loc[[f'Ema_{PARA.ema_fast}',f'Ema_{PARA.ema_slow}']].values
            fast,slow=[fast_old,fast_new],[slow_old,slow_new]
            
            now=dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S')
                        
            order_books=exchange.fetch_order_book(PARA.symbol,limit=5)

            if cross_over(fast,slow):
                #close the sell order and create a new buy order

                print(now,'Buy')
                if open_position:
                    #PLACE BUY ORDER HERE 
                    close_price=float(order_books['asks'][0][0]) 
                    trading_log(now,'SELL',latest_quant,open_price,close_price)

                quantity=round_down_nth(PARA.balance/float(order_books['asks'][0][0]),3)
                #PLACE BUY ORDER HERE
                open_position=True
                latest_quant=quantity
                open_price=float(order_books['asks'][0][0])

            if cross_under(fast,slow):
                #close the buy order and create a new sell order

                print(now,'Sell')
                if open_position:
                    #PLACE SELL ORDER HERE 
                    close_price=float(order_books['bids'][0][0])
                    trading_log(now,'BUY',latest_quant,open_price,close_price)

                quantity=round_down_nth(PARA.balance/float(order_books['bids'][0][0]),3)
                #PLACE SELL ORDER HERE
                open_position=True
                latest_quant=quantity
                open_price=float(order_books['bids'][0][0])

            check=new
        sleep(0.5)
        
#-----------Function
if __name__=='__main__':
    main()
