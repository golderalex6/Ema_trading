from IMPORT import *
__location__=os.path.dirname(__file__)
def send_error(err_str):
    url='https://send.api.mailtrap.io/api/send'
    data={
            'from':{'email':'mailtrap@demomailtrap.com','name':''},# Your name here
            'to':[{'email':''}],#pass your email here
            'subject':'Warning!!',
            'text':err_str,
        }
    header={
            'Authorization': 'Bearer ' , #Your Bearer
            'Content-Type':'application/json'
            }
    s=requests.post(url,data=json.dumps(data),headers=header)
    return s

if __name__=='__main__':
    send_error('testing')
