from IMPORT import * 

def send_error(err_str):
    url='https://send.api.mailtrap.io/api/send'
    data={
            'from':{'email':'mailtrap@demomailtrap.com','name':'TranHongLoan'},
            'to':[{'email':'golderalex6@gmail.com'}],
            'subject':'Warning!!',
            'text':'Something wrong with our Trading',
            'category':'Warning test'
        }
    header={
            'Authorization': 'Bearer 2950014c5781cfac4e6897364262f3df' ,
            'Content-Type':'application/json'
            }
    s=requests.post(url,data=json.dumps(data),headers=header)
    return s

if __name__=='__main__':
    try:
        2/0
    except:
        print('error')
        raise
