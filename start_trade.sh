#!urs/bin/bash

root=`pwd`
python3 $root/Database/ddl.py
python3 $root/Trading/FILLING_DATA.py
screen -d -R -S Trading_bot -c $root/.trade_setup
