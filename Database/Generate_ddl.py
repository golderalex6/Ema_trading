import sqlite3
import os
__location__=os.path.dirname(__file__ )
col=['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d']

u=''
for i in col:
    u+=f'create table Ema_{i}(\n'
    u+='Date text not null,\n'
    u+='Timestamp int primary key,\n'
    for v in range(1,101):
        if v==100:
            u+=f'Ema_{v} real not null \n'
        else:
            u+=f'Ema_{v} real not null,\n'
    u+=')\n\n'

with open(os.path.join(__location__,'raw.txt'),'w+') as f:
    f.write(u)
