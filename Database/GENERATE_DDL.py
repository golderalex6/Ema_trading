import sqlite3
import os
__location__=os.path.dirname(__file__ )
col=['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d']

u=''

# for Ema
u+=f'create table Ema(\n'
u+='Date text not null,\n'
u+='Timestamp int primary key,\n'
u+='Timeframe text not null,'
for v in range(1,101):
    if v==100:
        u+=f'Ema_{v} real not null \n'
    else:
        u+=f'Ema_{v} real not null,\n'
u+=');\n\n'

# for Price
u+=f'''
create table Price(
Date text not null,
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);
'''

# for trigger Ema
u+=f'''
create trigger check_length_ema
after insert
on Ema
begin'''
for tf in col:
    u+=f'''
    delete from Ema where Timestamp in (select Timestamp from Ema where Timeframe='{tf}' order by Timestamp limit 1) and Timeframe='{tf}' and (select count(*) from Ema where Timeframe='{tf}')>120;\n
'''

u+='''\nend;\n'''

# for trigger Price
u+=f'''
create trigger check_length_price
after insert
on Price
begin'''
for tf in col:
    u+=f'''
    delete from Price where Timestamp in (select Timestamp from Price where Timeframe='{tf}' order by Timestamp limit 1) and Timeframe="{tf}" and (select count(*) from Price where Timeframe='{tf}')>120;\n
'''

u+='''\nend;\n'''

u+='''
/*History_table*/
create table History(
    Date text not null,
    Timestamp int not null,
    Timeframe text not null,
    [Order type] text not null,
    [Total fee] real not null,
    Amount real not null,
    Open real not null,
    Close real not null,
    [Win percent] real not null,
    [Win USDT] real not null
);

'''

u+='''
/*Open_order*/
create table Open_order(
[Order type] text not null,
Amount real not null,
[Open price] real not null
)

'''
with open(os.path.join(__location__,'RAW.txt'),'w+') as f:
    f.write(u)
