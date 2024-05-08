from IMPORT import *
__location__=os.path.dirname(__file__)
def send_error(err_str):
    url='https://send.api.mailtrap.io/api/send'
    data={
            'from':{'email':'mailtrap@demomailtrap.com','name':'TranHongLoan'},
            'to':[{'email':'golderalex6@gmail.com'}],#pass your email here
            'subject':'Warning!!',
            'text':err_str,
        }
    header={
            'Authorization': 'Bearer 2950014c5781cfac4e6897364262f3df' ,
            'Content-Type':'application/json'
            }
    s=requests.post(url,data=json.dumps(data),headers=header)
    with open(os.path.join(__location__,'ERROR.log'),'a+') as f:
        f.write(err_str+'\n\n')
    return s

if __name__=='__main__':
    send_error('testing')
