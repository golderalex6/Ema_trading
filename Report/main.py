from pathlib import Path
import sys
root=str(Path(__file__).parents[1])
sys.path.append(root+'/Trading/')
import plotext as plt
from IMPORT import *

def total_profit(tf):
    #calculate some general data
    data=DB.query_db(f"select sum([Win percent]),sum([Win USDT]) from History where Timeframe='{tf}'")
    if data[0]==(None,None):
        roi=0
        pnl=0
    else:
        roi=data[0][0]
        pnl=data[0][1]
    print(data)
    return f"ROI:{roi:2f}%\n PnL:{pnl:2f}$"

def growth_chart(tf):
    #get data for growing chart
    data=np.array(DB.query_db(f"select Date,[Win USDT] from History where Timeframe='{tf}'"))
    if len(data)==0:
        return [[],[]]
    date=data[:,0]
    trade=np.array(data[:,1],dtype='float')
    cumulative=[trade[0]]
    for i in range(1,len(trade)):
        cumulative.append(cumulative[-1]+trade[i])

    return [data[:,0],cumulative]

def main(tf):
    start=dt.datetime.now()
    #draw chart and summarize table 
    while True:
        plt.subplots(2,1)
        plt.subplot(1,1)
        x,y=growth_chart(tf)
        plt.plot(x,y,marker='fhd')
        plt.title('Growth chart')
        plt.theme('matrix')

        plt.subplot(2,1)
        text=F.time_delta(start)
        text+=total_profit(tf)
        plt.indicator(text,'Summarize')
        plt.show()
        F.round_time(0)

if __name__=='__main__':
    check_input=len(sys.argv)
    if check_input==1:
        tf=input('Select your timeframe:')
    else:
        tf=sys.argv[1]
    while tf not in PARA.col:
        tf=input('Please choose again:')
    try:
        main(tf)
    except Exception as e:
        error_str='Error from Report/main.py:'+str(e)
        ERROR.send_error(error_str)
        raise
