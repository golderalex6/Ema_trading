from IMPORT import * 
#-----------Function
async def calculate_and_distribute():
    #get the uri of all columns
    uri='wss://fstream.binance.com/stream?streams='
    uri+='/'.join(list(map(lambda x:f'{HYPER.symbol.lower()}@kline_{x}',PARA.col)))
    async with websockets.connect(uri) as ws:
        while True:
            #get the kline and check if the kline is done or not
            raw=json.loads(await ws.recv())
            dat=raw['data']['k']
            done=dat['x']
            if done:
                #distribute to dabase
                date,timestamp,tf=dt.datetime.strftime(dt.datetime.fromtimestamp(dat['t']/1000),'%Y/%m/%d %H:%M:%S'),dat['t'],dat['i']
                open,high,low,close,volume=dat['o'],dat['h'],dat['l'],dat['c'],dat['v']
                price=[date,timestamp,tf,open,high,low,close,volume]

                #Ema
                old_ema=DB.query_db(f"select * from Ema where Timeframe='{tf}' order by Timestamp desc limit 1")
                old_ema=[close]*100 if len(old_ema)==0 else old_ema[0][3:]
                new_ema=Ema(close,old_ema,date,timestamp,tf)

                #Database
                DB.insert_db(['Price','Ema'],[price,new_ema],True)
                print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'),tf)

def Main():
    #Error handling
    try:
        asyncio.run(calculate_and_distribute())
    except Exception as e:
        error_str='Error from Trading/data.py :'+ str(e)
        ERROR.send_error(error_str)
        raise
#-----------Function

if __name__=="__main__":
    Main()
