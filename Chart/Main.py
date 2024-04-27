from pathlib import Path
import sys
root=str(Path(__file__).parents[1])
sys.path.append(root+'/Trading/')
import plotext as plt
from IMPORT import *
#-----------Function
def round_time():
    #wait to the nearest time frame
    DELAY=10
    sec=60
    n=dt.datetime.now().timestamp()

    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    sleep(gap+DELAY)

def Draw(tf):
    while True:            
        price=DB.query_db(f'select * from Price_{tf}')
        ema_fast=DB.query_db(f'select Ema_{PARA.ema_fast} from Ema_{tf}')
        ema_slow=DB.query_db(f'select Ema_{PARA.ema_slow} from Ema_{tf}')
        ema_fast=list(map(lambda x:x[0],ema_fast))
        ema_slow=list(map(lambda x:x[0],ema_slow))
        day=list(map(lambda x:x[-1],price))
        candle=pd.DataFrame(list(map(lambda x:x[1:-2],price)),columns=['Open','High','Low','Close']).to_dict(orient='list')
        plt.plot(day,ema_fast,color='orange',marker='fhd')
        plt.plot(day,ema_slow,color='purple',marker='fhd')
        plt.candlestick(day,candle )
        plt.theme('matrix')
        plt.title(tf)
        plt.show()

        round_time()
        plt.clear_figure()

def Main():
    tf=input('Please select your timeframe:')
    while tf not in PARA.col:
        tf=input('Please try again:')
    try:
        Draw(tf)
    except Exception as e:
        error_str='Error from Chart :'+ str(e)
        ERROR.send_error(error_str)
        raise 
#-----------Function

if __name__=='__main__':
    Main()
