from IMPORT import *
import random
import plotext as plt
def get_data(i,delta,tf):
    #using Sin function and random noise to fake data
    m=sin(i)*20
    timestamp=dt.datetime.now().timestamp()
    o,h,l,c,v=[m,m+random.randrange(0,5),m-random.randrange(0,5),sin(i+delta)*20,0.1]
    datetime=dt.datetime.strftime(dt.datetime.fromtimestamp(timestamp),'%Y/%m/%d %H:%M:%S')
    return [datetime ,timestamp,tf,o,h,l,c,v]

def calculate_and_distribute(i,delta):
    #fake data but only work on 1m timeframe
    tf='1h'
    price=get_data(i,delta,tf)
    #Ema
    old_ema=DB.query_db(f"select * from Ema where Timeframe='{tf}' order by Timestamp desc limit 1")
    old_ema=[price[6]]*100 if len(old_ema)==0 else old_ema[0][3:]
    new_ema=Ema(price[6],old_ema,price[1],price[0],tf)
    #Database
    DB.insert_db([f'Price',f'Ema'],[price,new_ema],True)
    #Get and handle data
    price=DB.query_db(f"select * from Price where Timeframe='{tf}'")
    ema_fast=DB.query_db(f"select Ema_{HYPER.ema_fast} from Ema where Timeframe='{tf}'")
    ema_slow=DB.query_db(f"select Ema_{HYPER.ema_slow} from Ema where Timeframe='{tf}'")
    ema_fast=list(map(lambda x:x[0],ema_fast))
    ema_slow=list(map(lambda x:x[0],ema_slow))
    day=list(map(lambda x:x[0],price))
    #Draw B/S order
    for i in range(len(ema_fast)-2):
        fast=ema_fast[i:i+2]
        slow=ema_slow[i:i+2]
        if F.cross_over(fast,slow):
            plt.text('B',x=day[i+2],y=price[i+2][3],alignment='center',background='black',color='green')
        if F.cross_under(fast,slow):
            plt.text('S',x=day[i+2],y=price[i+2][3],alignment='center',background='black',color='red')
    #Draw candle stick and setting the chart
    candle=pd.DataFrame(list(map(lambda x:x[3:-1],price)),columns=['Open','High','Low','Close']).to_dict(orient='list')
    plt.plot(day,ema_fast,color='orange',marker='fhd',label=f'Ema:{HYPER.ema_fast}')
    plt.plot(day,ema_slow,color='purple',marker='fhd',label=f'Ema:{HYPER.ema_slow}')
    plt.candlestick(day,candle )
    plt.theme('matrix')
    plt.grid(True,True)
    plt.title(tf)
    plt.show()

    plt.clear_figure()

def Main():
    i,delta=0,0.05
    while True:
        F.round_time(0,2)
        calculate_and_distribute(i,delta )
        i+=delta

if __name__=='__main__':
    Main()
