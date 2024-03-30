from IMPORT import *

#-----------Normal setup
__location__=os.path.dirname(__file__)
client = UMFutures(PARA.api_key,PARA.secret,base_url=PARA.base_url)
client.change_leverage(PARA.symbol,1)
#-----------Normal setup

#-----------Function
def round_down_nth(d,n):
    return floor(d*10**(n))/10**n
def handle_ohlvc(raw):
    #convert raw data crawled from binance to dataframe pandas for easy process

    df=pd.DataFrame(raw,columns=['Timestamp','Open','High','Low','Close','Volume'])
    df['Date']=df['Timestamp'].map(lambda x:dt.datetime.strftime(dt.datetime.fromtimestamp(x/1000),'%Y/%m/%d %H:%M:%S'))

    return df

def round_time(tf):
    #wait to the nearest time frame

    sec=PARA.tf_to_sec[tf]
    standard_time=dt.datetime(2024,1,1,7,0).timestamp()
    n=dt.datetime.now().timestamp()

    if (int(n)-standard_time)%sec==0:
        print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))
        return
    gap=ceil((n-standard_time)/sec)*sec-(n-standard_time)
    sleep(gap)
    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))

def cross_over(fast,slow):
    #check if the fast ema is cross over the slow one

    if fast[0]<=slow[0] and fast[1]>slow[1]:
        return True
    else:
        return False

def cross_under(fast,slow):
    #check if the fast ema is cross under the slow one

    if fast[0]>=slow[0] and fast[1]<slow[1]:
        return True
    else:
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

    sheet.append_value_spreadsheets(PARA.sheet_id,'Trading_log!A1:H1',[history_log])

def main()->None:
    #run the trading application
    check=pd.read_csv(os.path.join(__location__,f'Indicator/Ema_{PARA.timeframe}.csv'),index_col=0)

    while True:
        new=pd.read_csv(os.path.join(__location__,f'Indicator/Ema_{PARA.timeframe}.csv'),index_col=0)

        if not check.equals(new):
            
            #Get the Ema value
            fast_old,slow_old=check.loc[[f'Ema_{PARA.ema_fast}',f'Ema_{PARA.ema_slow}']].values
            fast_new,slow_new=new.loc[[f'Ema_{PARA.ema_fast}',f'Ema_{PARA.ema_slow}']].values
            fast,slow=[fast_old,fast_new],[slow_old,slow_new]
            
            now=dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S')
            
            open_position=False
            latest_quant=None
            order_books=client.depth(PARA.symbol,limit=5)
            open_price=None
            close_price=None

            if cross_over(fast,slow):
                #close the sell order and create a new buy order

                print(now,'Buy')
                if open_position:
                    client.new_order(symbol=PARA.symbol,side='BUY',type='MARKET',quantity=latest_quant)
                    close_price=float(order_books['asks'][0][0])
                    trading_log(now,'SELL',latest_quant,open_price,close_price)

                quantity=round_down_nth(PARA.balance/float(order_books['asks'][0][0]),3)
                client.new_order(symbol=PARA.symbol,side='BUY',type='MARKET',quantity=quantity)
                open_position=True
                latest_quant=quantity
                open_price=float(order_books['asks'][0][0])

            if cross_under(fast,slow):
                #close the buy order and create a new sell order

                print(now,'Sell')
                if open_position:
                    client.new_order(symbol=PARA.symbol,side='SELL',type='MARKET',quantity=latest_quant)
                    close_price=float(order_books['bids'][0][0])
                    trading_log(now,'BUY',latest_quant,open_price,close_price)

                quantity=round_down_nth(PARA.balance/float(order_books['bids'][0][0]),3)
                client.new_order(symbol=PARA.symbol,side='SELL',type='MARKET',quantity=quantity)
                open_position=True
                latest_quant=quantity
                open_price=float(order_books['bids'][0][0])

            check=new
        sleep(0.5)
        
#-----------Function

if __name__=='__main__':
    main()
