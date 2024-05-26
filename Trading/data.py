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
                Ema(close,date,timestamp,tf)

                #Database
                DB.insert_db('Price',price)
                print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'),tf)

async def auto_reconnect(r,sec=60):
    #destroy all asyncio task to disconnect to binance websocket 
    n=dt.datetime.now().timestamp()
    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    await asyncio.sleep(gap+r)
    for i in asyncio.all_tasks():
        i.cancel()

async def main():
    #create a try catch to after disconnect and connect again
    while True:
        try:
            await asyncio.gather(calculate_and_distribute(),auto_reconnect(20,7200))
        except:
            print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S')+': Reconnect to binance websocket')
            continue
#-----------Function

if __name__=="__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        error_str='Error from Trading/data.py :'+ str(e)
        ERROR.send_error(error_str)
        raise
