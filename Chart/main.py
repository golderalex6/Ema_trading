from pathlib import Path
import sys
root=str(Path(__file__).parents[1])
sys.path.append(root+'/Trading/')
import plotext as plt
from IMPORT import *
#-----------Function
def Draw(tf):
    while True:            
        #Get and handle data
        price=DB.query_db(f"select * from Price where Timeframe='{tf}'")
        ema_fast=DB.query_db(f"select Ema_{HYPER.ema_fast} from Ema where Timeframe='{tf}'")
        ema_slow=DB.query_db(f"select Ema_{HYPER.ema_slow} from Ema where Timeframe='{tf}'")
        ema_fast=list(map(lambda x:x[0],ema_fast))
        ema_slow=list(map(lambda x:x[0],ema_slow))
        day=list(map(lambda x:x[0],price))
        plt.date_form('Y/m/d H:M:S')
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

        F.round_time(1,5)
        plt.clear_figure()
#-----------Function
def Main():
    check_len=len(sys.argv)
    if check_len==1:
        tf=input('Please select your timeframe:')
    else:
        tf=sys.argv[1]

    while tf not in PARA.col:
        tf=input('Please try again:')
    try:
        Draw(tf)
    except Exception as e:
        error_str='Error from Chart/main.py :'+ str(e)
        ERROR.send_error(error_str)
        raise 
#-----------Function

if __name__=='__main__':
    Main()
