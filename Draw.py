from IMPORT import *

#-----------Normal setup
__location__=os.path.dirname(__file__)
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': PARA.api_key ,
    'secret': PARA.secret ,
})
##-----------Normal setup

#-----------Function
def Draw():
    #Draw chart and Ema line on the sheet 

    updated_col=F.updated_columns()

    for i in updated_col:
        length=len(sheet.read_value_spreadsheets(PARA.sheet_id,f"{i}!A:A"))
        if length>71:
            sheet.delete_rows_columns(PARA.sheet_id,PARA.sheet_code[i],1,2)
        ema_val=list(pd.read_csv(os.path.join(__location__,f'Indicator/Ema_{i}.csv'),index_col=0)[i].values)
        
        while True:
            try:
                price=exchange.fetch_ohlcv(PARA.symbol,i,limit=1)[0][1:]
                break
            except:
                sleep(0.5)
        price.extend(ema_val)
        price=F.convert_number(price)

        sheet.append_value_spreadsheets(PARA.sheet_id,f'{i}!A1:ZZ1',[price])


    print(updated_col)
def main():
    check=pd.read_csv(os.path.join(__location__,'Indicator/Ema_1m.csv'),index_col=0) 
    while True:
        while True:
            try:
                new=pd.read_csv(os.path.join(__location__,'Indicator/Ema_1m.csv'),index_col=0)
                break
            except:
                sleep(0.5)

        if not check.equals(new):
            Draw()
            check=new
        sleep(0.5)
 

#-----------Function

if __name__=='__main__':
    main()
