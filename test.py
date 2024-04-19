from IMPORT import *
import hashlib
import hmac
import json
option_type='CALL'
exercised_coin='USDT'
invest_coint='BTC'
end_point='https://api.binance.com'
timestamp=int(dt.datetime.now().timestamp()*1000)
#n=int(dt.datetime.now().timestamp()*1000)
#a=requests.get(f"https://api.binance.com/sapi/v1/dci/product/list?optionType={option_type}&exercisedCoin={exercised_coin}&investCoin={invest_coint}&timestamp={n}")

SECRET=PARA.secret 
def hashing(query_string):
    return hmac.new(SECRET.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
headers={'X-MBX-APIKEY': PARA.api_key }
query_string=f'optionType={option_type}&exercisedCoin={exercised_coin}&investCoin={invest_coint}&timestamp={timestamp}'
signature=hashing(query_string )
url=end_point+'/sapi/v1/dci/product/list?'+query_string+f'&signature={signature}'
a=requests.get(url,headers=headers)
m=open('test.txt','w+')
m.write(json.dumps(a.json()))
