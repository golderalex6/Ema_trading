from IMPORT import *
import random

def get_data(i,delta,tf):
    #using Sin function and random noise to fake data
    m=sin(i)*20
    timestamp=dt.datetime.now().timestamp()
    o,h,l,c,v=[m,m+random.randrange(0,5),m-random.randrange(0,5),sin(i+delta)*20,0.1]
    datetime=dt.datetime.strftime(dt.datetime.fromtimestamp(timestamp),'%Y/%m/%d %H:%M:%S')
    return [datetime ,timestamp,tf,o,h,l,c,v]

def calculate_and_distribute(i,delta):
    #fake data but only work on 1m timeframe
    tf='1m'
    price=get_data(i,delta,tf)
    #Ema
    old_ema=DB.query_db(f"select * from Ema where Timeframe='{tf}' order by Timestamp desc limit 1")
    old_ema=[price[6]]*100 if len(old_ema)==0 else old_ema[0][3:]
    new_ema=Ema(price[6],old_ema,price[1],price[0],tf)
    #Database
    DB.insert_db([f'Price',f'Ema'],[price,new_ema],True)

    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))

def Main():
    i,delta=0,0.05
    while True:
        F.round_time(0,5)
        calculate_and_distribute(i,delta )
        i+=delta

if __name__=='__main__':
    Main()
