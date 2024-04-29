from IMPORT import *

#-----------Function
def Ema(price:float,old_ema:list,timestamp,date):
    #Calculate the Ema values

    new_values=np.array([price]*100,dtype='float')
    old_values=np.array(old_ema,dtype='float')
    k=np.array([2/(i+1) for i in range(1,101)])

    new_ema=(np.multiply(new_values,k)+np.multiply(old_values,1-k)).tolist()
    new_ema.insert(0,timestamp)
    new_ema.insert(0,date)
    return new_ema
#-----------Function

if __name__=="__main__":
    old_ema=[]
    old_ema.extend([0]*49)
    old_ema.append(63636.607)
    old_ema.extend([0]*50)
    price=63257.43
    m=Ema(price,old_ema,0,0)
    print(m[51])
