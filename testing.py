from IMPORT import *
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': PARA.api_key ,
    'secret': PARA.secret,
})

print(exchange.fetch_ohlcv(PARA.symbol,'1m',limit=2))
