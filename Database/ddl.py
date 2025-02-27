import sqlite3 as sql
import os
__location__=os.path.dirname(__file__ )
db_path=os.path.join(__location__,'Main.db')

#remove before run DDL code
if os.path.exists(db_path):
    os.remove(db_path)

conn=sql.connect(db_path)
cursor=conn.cursor()

sql_str='''
create table Ema(
Date text not null,
Timestamp int,
Timeframe text not null,
Ema_1 real not null,
Ema_2 real not null,
Ema_3 real not null,
Ema_4 real not null,
Ema_5 real not null,
Ema_6 real not null,
Ema_7 real not null,
Ema_8 real not null,
Ema_9 real not null,
Ema_10 real not null,
Ema_11 real not null,
Ema_12 real not null,
Ema_13 real not null,
Ema_14 real not null,
Ema_15 real not null,
Ema_16 real not null,
Ema_17 real not null,
Ema_18 real not null,
Ema_19 real not null,
Ema_20 real not null,
Ema_21 real not null,
Ema_22 real not null,
Ema_23 real not null,
Ema_24 real not null,
Ema_25 real not null,
Ema_26 real not null,
Ema_27 real not null,
Ema_28 real not null,
Ema_29 real not null,
Ema_30 real not null,
Ema_31 real not null,
Ema_32 real not null,
Ema_33 real not null,
Ema_34 real not null,
Ema_35 real not null,
Ema_36 real not null,
Ema_37 real not null,
Ema_38 real not null,
Ema_39 real not null,
Ema_40 real not null,
Ema_41 real not null,
Ema_42 real not null,
Ema_43 real not null,
Ema_44 real not null,
Ema_45 real not null,
Ema_46 real not null,
Ema_47 real not null,
Ema_48 real not null,
Ema_49 real not null,
Ema_50 real not null,
Ema_51 real not null,
Ema_52 real not null,
Ema_53 real not null,
Ema_54 real not null,
Ema_55 real not null,
Ema_56 real not null,
Ema_57 real not null,
Ema_58 real not null,
Ema_59 real not null,
Ema_60 real not null,
Ema_61 real not null,
Ema_62 real not null,
Ema_63 real not null,
Ema_64 real not null,
Ema_65 real not null,
Ema_66 real not null,
Ema_67 real not null,
Ema_68 real not null,
Ema_69 real not null,
Ema_70 real not null,
Ema_71 real not null,
Ema_72 real not null,
Ema_73 real not null,
Ema_74 real not null,
Ema_75 real not null,
Ema_76 real not null,
Ema_77 real not null,
Ema_78 real not null,
Ema_79 real not null,
Ema_80 real not null,
Ema_81 real not null,
Ema_82 real not null,
Ema_83 real not null,
Ema_84 real not null,
Ema_85 real not null,
Ema_86 real not null,
Ema_87 real not null,
Ema_88 real not null,
Ema_89 real not null,
Ema_90 real not null,
Ema_91 real not null,
Ema_92 real not null,
Ema_93 real not null,
Ema_94 real not null,
Ema_95 real not null,
Ema_96 real not null,
Ema_97 real not null,
Ema_98 real not null,
Ema_99 real not null,
Ema_100 real not null 
);


create table Price(
Date text not null,
Timestamp int ,
Timeframe text not null,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null
);

create trigger check_length_ema
after insert
on Ema
begin
    delete from Ema where Timestamp in (select Timestamp from Ema where Timeframe=NEW.Timeframe order by Timestamp limit 1) and Timeframe=NEW.Timeframe and (select count(*) from Ema where Timeframe=NEW.Timeframe)>120;


end;

create trigger check_length_price
after insert
on Price
begin
    delete from Price where Timestamp in (select Timestamp from Price where Timeframe=NEW.Timeframe order by Timestamp limit 1) and Timeframe=NEW.Timeframe and (select count(*) from Price where Timeframe=NEW.Timeframe)>120;


end;

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


/*Open_order*/
create table Open_order(
[Order type] text not null,
Amount real not null,
[Open price] real not null
)

'''

cursor.executescript(sql_str)
conn.commit()
