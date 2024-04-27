import sqlite3 as sql
import os
__location__=os.path.dirname(__file__ )
db_path=os.path.join(__location__,'Main.db')

#remove before run DDL code
if os.path.exists(db_path):
    os.remove(db_path)

conn=sql.connect(os.path.join(__location__,'Main.db'))
cursor=conn.cursor()

sql_str='''create table Ema_1m(
Date text not null,
Timestamp int primary key,
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

create table Ema_3m(
Date text not null,
Timestamp int primary key,
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

create table Ema_5m(
Date text not null,
Timestamp int primary key,
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

create table Ema_15m(
Date text not null,
Timestamp int primary key,
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

create table Ema_30m(
Date text not null,
Timestamp int primary key,
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

create table Ema_1h(
Date text not null,
Timestamp int primary key,
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

create table Ema_2h(
Date text not null,
Timestamp int primary key,
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

create table Ema_4h(
Date text not null,
Timestamp int primary key,
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

create table Ema_6h(
Date text not null,
Timestamp int primary key,
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

create table Ema_8h(
Date text not null,
Timestamp int primary key,
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

create table Ema_12h(
Date text not null,
Timestamp int primary key,
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

create table Ema_1d(
Date text not null,
Timestamp int primary key,
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

create table Price_1m (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_3m (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_5m (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_15m (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_30m (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_1h (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_2h (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_4h (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_6h (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_8h (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_12h (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create table Price_1d (
Timestamp int primary key,
Open real not null,
High real not null,
Low real not null,
Close real not null,
Volume real not null,
Date text not null
);

create trigger check_len_Ema_1m
before insert 
on Ema_1m
begin
    delete from Ema_1m where Timestamp in (select Timestamp from Ema_1m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_3m
before insert 
on Ema_3m
begin
    delete from Ema_3m where Timestamp in (select Timestamp from Ema_3m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_5m
before insert 
on Ema_5m
begin
    delete from Ema_5m where Timestamp in (select Timestamp from Ema_5m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_15m
before insert 
on Ema_15m
begin
    delete from Ema_15m where Timestamp in (select Timestamp from Ema_15m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_30m
before insert 
on Ema_30m
begin
    delete from Ema_30m where Timestamp in (select Timestamp from Ema_30m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_1h
before insert 
on Ema_1h
begin
    delete from Ema_1h where Timestamp in (select Timestamp from Ema_1h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_2h
before insert 
on Ema_2h
begin
    delete from Ema_2h where Timestamp in (select Timestamp from Ema_2h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_4h
before insert 
on Ema_4h
begin
    delete from Ema_4h where Timestamp in (select Timestamp from Ema_4h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_6h
before insert 
on Ema_6h
begin
    delete from Ema_6h where Timestamp in (select Timestamp from Ema_6h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_8h
before insert 
on Ema_8h
begin
    delete from Ema_8h where Timestamp in (select Timestamp from Ema_8h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_12h
before insert 
on Ema_12h
begin
    delete from Ema_12h where Timestamp in (select Timestamp from Ema_12h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Ema_1d
before insert 
on Ema_1d
begin
    delete from Ema_1d where Timestamp in (select Timestamp from Ema_1d order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_1m
before insert 
on Price_1m
begin
    delete from Price_1m where Timestamp in (select Timestamp from Price_1m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_3m
before insert 
on Price_3m
begin
    delete from Price_3m where Timestamp in (select Timestamp from Price_3m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_5m
before insert 
on Price_5m
begin
    delete from Price_5m where Timestamp in (select Timestamp from Price_5m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_15m
before insert 
on Price_15m
begin
    delete from Price_15m where Timestamp in (select Timestamp from Price_15m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_30m
before insert 
on Price_30m
begin
    delete from Price_30m where Timestamp in (select Timestamp from Price_30m order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_1h
before insert 
on Price_1h
begin
    delete from Price_1h where Timestamp in (select Timestamp from Price_1h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_2h
before insert 
on Price_2h
begin
    delete from Price_2h where Timestamp in (select Timestamp from Price_2h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_4h
before insert 
on Price_4h
begin
    delete from Price_4h where Timestamp in (select Timestamp from Price_4h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_6h
before insert 
on Price_6h
begin
    delete from Price_6h where Timestamp in (select Timestamp from Price_6h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_8h
before insert 
on Price_8h
begin
    delete from Price_8h where Timestamp in (select Timestamp from Price_8h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_12h
before insert 
on Price_12h
begin
    delete from Price_12h where Timestamp in (select Timestamp from Price_12h order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;


create trigger check_len_Price_1d
before insert 
on Price_1d
begin
    delete from Price_1d where Timestamp in (select Timestamp from Price_1d order by Timestamp limit 1) and (select count(*) from Timestamp)>=70;
end;

create table History(
Date text primary key,
[Order type] text not null,
Amount real not null,
Open real not null,
Close real not null,
[Win percent] real not null,
[Win USDT] real not null);

create table Open_order(
[Order type] text not null,
Amount real not null,
[Open price] real not null
)

'''

cursor.executescript(sql_str)
conn.commit()
