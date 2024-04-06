from IMPORT import *

#-----------Normal setup
__location__=os.path.dirname(__file__)
#-----------Normal setup

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
        pass 

    print(updated_columns)

def round_time():
    #wait to the nearest time frame

    sec=60
    n=dt.datetime.now().timestamp()

    gap=ceil((n-PARA.standard_sec)/sec)*sec-(n-PARA.standard_sec)
    sleep(gap)
    print(dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d %H:%M:%S'))

def main():
    
    round_time()
    Draw()

#-----------Function

if __name__=='__main__':
    main()
