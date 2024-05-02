from pathlib import Path 
import sys
sys.path.append(str(Path(__file__).parent)+'/Trading')
from IMPORT import *
root=os.path.dirname(__file__)

screen_setup=[f'screen -t Data python3 {root}/Trading/data.py']

#create screen setup for each timeframe on HYPERPARAMETER
for tf in HYPER.timeframe:
    screen_setup.append(f'screen -t Trade-{tf} python3 {root}/Trading/trade.py {tf}')
    screen_setup.append(f'screen -t Chart-{tf} python3 {root}/Chart/main.py {tf}')
    screen_setup.append(f'screen -t Report-{tf} python3 {root}/Report/main.py {tf}')

#write to .trade_setup 
with open(os.path.join(root,'.trade_setup'),'w+') as f:
    f.write('\n'.join(screen_setup))
