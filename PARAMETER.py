from IMPORT import *
#-----------Main Parameter
ema_fast=7
ema_slow=70
symbol='BTCUSDT'
timeframe='1m'
type='Close'
balance=150
#-----------Main Parameter

#-----------Normal setup
api_key=os.getenv('key_future_test')
secret=os.getenv('secret_future_test')
sheet_id='1Wp4cpdJpK3LKhI9Cf0_iRxJMzZ08YbdGaOlukZzgZLE'

tf_to_sec={'1m':60,'3m':180,'5m':300,'15m':900,'30m':1800,'1h':3600,'2h':7200,'4h':14400,'6h':21600,'8h':28800,'12h':43200,'1d':86400}
tf_to_min={'1m':1,'3m':3,'5m':5,'15m':15,'30m':30,'1h':60,'2h':120,'4h':240,'6h':360,'8h':480,'12h':720,'1d':1440}
col=np.array(['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d'])
standard_sec=dt.datetime(2024,1,1,7,0).timestamp()
standard_min=int(standard_sec/60)
base_url='https://testnet.binancefuture.com' #CHANGE TO MAIN NET WHEN START TRADING

#-----------Normal setup