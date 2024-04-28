from pathlib import Path
import sys
root=str(Path(__file__).parents[1])
sys.path.append(root+'/Trading/')
import plotext as plt
from IMPORT import *
df=pd.read_csv('Chart/BTCUSDC-5m-2024-04-01.csv',index_col=0).iloc[:,:4]
width=120
bot,distance=0,width
df.columns=['Open','High','Low','Close']

def convert(timestamp:int):
    day=dt.datetime.fromtimestamp(int(timestamp/1000))
    day_str=dt.datetime.strftime(day,'%Y/%m/%d %H:%M:%S')
    return day_str
date=list(map(lambda x:convert(x),df.index))

while True:
    # dat=df.iloc[bot:bot+distance].to_dict(orient='list')
    # day=date[bot:bot+distance]
    # plt.candlestick(day,dat)
    x1=np.linspace(bot,bot+10,width)
    x2=np.linspace(bot,bot+10,width)-1.75
    y1=np.sin(x1)
    y2=np.sin(x2)
    for i in range(y2.shape[0]-2):
        fast_old,fast_new=y1[i:i+2]
        slow_old,slow_new=y2[i:i+2]
        fast=y1[i:i+2]
        slow=y2[i:i+2]
        if F.cross_over(fast,slow):
            plt.text('B',x=x1[i],y=y1[i]-0.1,alignment='center',color='green',background='black')
        if F.cross_under(fast,slow):
            plt.text('S',x=x1[i],y=y1[i]+0.1,alignment='center',color='red',background='black')
    plt.plot(x1,y1,color='orange',marker='fhd',label='Ema:7')
    plt.plot(x1,y2,color='purple',marker='fhd',label='Ema:70')
    plt.theme('matrix')
    plt.grid(True,True)
    plt.title('5m')
    plt.show()
    bot+=0.1
    sleep(0.1)
    plt.clear_figure()


