from pathlib import Path
import sys
root=str(Path(__file__).parents[1])
sys.path.append(root+'/Trading/')
import plotext as plt
from IMPORT import *

def total_profit():
    data=DB.query_db('select sum([Win percent]),sum([Win USDT]) from History')
    if len(data)==0:
        roi=0
        pnl=0
    else:
        roi=data[0][0]
        pnl=data[0][1]
    return f"ROI:{roi:2f}%\n PnL:{pnl:2f}$"

def growth_chart():
    data=np.array(DB.query_db('select Date,[Win USDT] from History'))
    if len(data)==0:
        return [[],[]]
    date=data[:,0]
    trade=np.array(data[:,1],dtype='float')
    cumulative=[trade[0]]
    for i in range(1,len(trade)):
        cumulative.append(cumulative[-1]+trade[i])

    return [data[:,0],cumulative]

def main():
    while True:
        plt.subplots(2,1)
        plt.subplot(1,1)
        x,y=growth_chart()
        plt.plot(x,y,marker='fhd')
        plt.title('Grouth chart')
        plt.theme('matrix')

        plt.subplot(2,1)
        text=total_profit()
        plt.indicator(text,'Summarize')
        plt.show()
        F.round_time(0,3600)

if __name__=='__main__':
    main()
