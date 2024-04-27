import sqlite3
import os
__location__=os.path.dirname(__file__ )
col=['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d']

u=''

#for Ema
# for i in col:
#     u+=f'create table Ema_{i}(\n'
#     u+='Date text not null,\n'
#     u+='Timestamp int primary key,\n'
#     for v in range(1,101):
#         if v==100:
#             u+=f'Ema_{v} real not null \n'
#         else:
#             u+=f'Ema_{v} real not null,\n'
#     u+=');\n\n'

#for Price
# for i in col:
#     u+=f'''
# create table Price_{i} (
# Timestamp int primary key,
# Open real not null,
# High real not null,
# Low real not null,
# Close real not null,
# Volume real not null,
# Date text not null
# );
# '''

# for trigger Ema
#for i in col:
#    u+=f'''
#create trigger check_len_Ema_{i}
#before insert 
#on Ema_{i}
#begin
#    delete from Ema_{i} where Timestamp in (select Timestamp from Ema_{i} order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
#end;\n
#'''

#for trigger Price
#for i in col:
#    u+=f'''
#create trigger check_len_Price_{i}
#before insert 
#on Price_{i}
#begin
#    delete from Price_{i} where Timestamp in (select Timestamp from Price_{i} order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
#end;\n
#'''


with open(os.path.join(__location__,'RAW.txt'),'w+') as f:
    f.write(u)
