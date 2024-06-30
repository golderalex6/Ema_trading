from pathlib import Path 
import sys
sys.path.append(str(Path(__file__).parent)+'/Trading')
from IMPORT import *
root=os.path.dirname(__file__)

error=''
#check for parameter

#Check 2 Ema line
if not(100>=HYPER.ema_fast>=1) and not (100>=HYPER.ema_slow>=1):
    error='ERROR'
#Check for valid timeframe 
for tf in HYPER.timeframe:
    if tf not in PARA.col:
        error='ERROR'
if HYPER.ema_fast>=HYPER.ema_slow:
    error='ERROR'

#check for valid symbol
test=requests.get(f"https://data-api.binance.vision/api/v3/klines?symbol={HYPER.symbol}&interval=1m").json()
if 'code' in test:
    error='ERROR'

#create screen setup for each timeframe on HYPERPARAMETER
screen_setup=[f'screen -t Data python3 {root}/Trading/data.py']
for tf in HYPER.timeframe:
    screen_setup.append(f'screen -t Trade-{tf} python3 {root}/Trading/trade.py {tf}')
    screen_setup.append(f'screen -t Chart-{tf} python3 {root}/Chart/main.py {tf}')
    screen_setup.append(f'screen -t Report-{tf} python3 {root}/Report/main.py {tf}')

#write to .trade_setup 
with open(os.path.join(root,'.trade_setup'),'w+') as f:
    f.write('\n'.join(screen_setup))

print(error)
