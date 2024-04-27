
from time import sleep
import plotext as plt
import random
import pandas as pd
import datetime as dt
import numpy as np
df=pd.read_csv('Chart/BTCUSDC-5m-2024-04-01.csv',index_col=0).iloc[:,:4]
bot,distance=0,70
df.columns=['Open','High','Low','Close']

def convert(timestamp:int):
    day=dt.datetime.fromtimestamp(int(timestamp/1000))
    day_str=dt.datetime.strftime(day,'%Y/%m/%d %H:%M:%S')
    return day_str
date=list(map(lambda x:convert(x),df.index))

while True:
    dat=df.iloc[bot:bot+distance].to_dict(orient='list')
    day=date[bot:bot+distance]
    # plt.candlestick(day,dat)
    plt.plot(day,[500*np.sin(i)+20000 for i in range(len(day))],color='orange')
    plt.theme('matrix')
    plt.grid(True,True)
    plt.title('5m')
    plt.show()
    bot+=1
    sleep(2)
    plt.clear_figure()


