#!urs/bin/bash

root=`pwd`
check=`python3 $root/.trade_setup.py`
if [ "$check" == "ERROR" ]
then
	echo 'Your hyperparameter is invalid !!'
	exit
else
	echo 'Your hyperparameter is valid !!'
	python3 $root/Database/ddl.py
	python3 $root/Trading/FILLING_DATA.py
	screen -d -R -S Trading_bot -c $root/.trade_setup
fi

