from IMPORT import *

#-----------Normal setup
__location__=os.path.dirname(__file__)
client = UMFutures(base_url=PARA.base_url)
##-----------Normal setup

#-----------Function
def updated_columns():
    #Return the columns that need to update at that time

    now_min=int(dt.datetime.now().timestamp()/60)
    updated_col=[]
    for i in PARA.col:
        if (now_min-PARA.standard_min)%PARA.tf_to_min[i]==0:
            updated_col.append(i)
    
    return updated_col

def Draw():
    #Draw chart and Ema line on the sheet 

    updated_col=updated_columns()

    for i in updated_col:
        length=len(sheet.read_value_spreadsheets(PARA.sheet_id,f"{i}!A:A"))
        if length>71:
            sheet.delete_rows_columns(PARA.sheet_id,PARA.sheet_code[i],1,2)
        ema_val=list(pd.read_csv(os.path.join(__location__,f'Indicator/Ema_{i}.csv'),index_col=0)[i].values)
        price=client.continuous_klines(pair=PARA.symbol,contractType='PERPETUAL',interval=i,limit=1)[0][:6]
        price.extend(ema_val)
        
        sheet.append_value_spreadsheets(PARA.sheet_id,'1m!A1:ZZ1',[price])


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
