import ccxt
import pandas as pd
import numpy as np
import GOOGLE_SPREADSHEET
from time import sleep
import datetime as dt
from dotenv import load_dotenv
import os
load_dotenv()

#-----------Parameter
ema_fast=7
ema_slow=70
symbol='ETHUSDT'
timeframe='15m'
#-----------Parameter

#-----------Normal setup
api_key=os.getenv('api_key')
secret=os.getenv('secret')
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': api_key,
    'secret': secret,
})
exchange.set_sandbox_mode(True)
#-----------Normal setup

#-----------Function
def main()->None:
    pass
#-----------Function

if __name__=='__main__':
    main()