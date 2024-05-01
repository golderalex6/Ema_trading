from IMPORT import *
import random

def get_data(i,delta):
    m=sin(i)*20
    timestamp=dt.datetime.now().timestamp()
    o,h,l,c,v=[m,m+random.randrange(0,5),m-random.randrange(0,5),sin(i+delta)*20,0.1]
    datetime=dt.datetime.strftime(dt.datetime.fromtimestamp(timestamp),'%Y/%m/%d %H:%M:%S')
    return [timestamp,o,h,l,c,v,datetime]

def calculate_and_distribute(i,delta):
    tf='1m'
    price=get_data(i,delta)
    #Ema
    old_ema=DB.query_db(f'select * from Ema_{tf} order by Timestamp desc limit 1')
    old_ema=[price[4]]*100 if len(old_ema)==0 else old_ema[0][2:]
    new_ema=Ema(price[4],old_ema,price[0],price[-1])
    #Database
    DB.insert_db([f'Price_{tf}',f'Ema_{tf}'],[price,new_ema],True)

    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))
    # print('Updated timeframe :',update_col)

def Main():
    i,delta=0,0.05
    while True:
        F.round_time(0,5)
        calculate_and_distribute(i,delta )
        i+=delta

if __name__=='__main__':
    Main()
