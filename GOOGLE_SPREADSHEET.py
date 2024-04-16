import json
import requests
import subprocess
import pandas as pd
import os

def get_auth_url(scope):
    with open('Credential.json','r+') as f:
        credential=json.loads(f.read())
        client_id=credential['client_id']
        redirect_uri=credential['redirect_uri']
    
    url_auth=f'https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}&access_type=offline'
    return url_auth

def check_expired(access_token:str):
    try:
        check=requests.post(f'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}').json()
        if 'error' in check:
            return False
        else:
            return (False,True)[check['expires_in']!=0]
    except:
        return False

def regenerate_access_token():
    
    with open('Credential.json','r+') as f:
        credential=json.loads(f.read())
        client_id=credential['client_id']
        client_secret=credential['client_secret']
        refresh_token=credential['refresh_token']
        authorize_code=credential['authorize_code']
        redirect_uri=credential['redirect_uri']

    if refresh_token=='':
        url_access_token=f'https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={authorize_code}&grant_type=authorization_code&redirect_uri={redirect_uri}'
    else:
        url_access_token=f'https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&refresh_token={refresh_token}&grant_type=refresh_token'    
    
    token=requests.post(url_access_token,headers={'Host':'oauth2.googleapis.com','Content-Type':'application/x-www-form-urlencoded'}).json()

    return token['access_token']

def read_value_spreadsheets(spreadsheet_id:str,ranges:str,majorDimension='ROWS'):
    
    access_token=regenerate_access_token()
    get=requests.get(f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchGet?access_token={access_token}&ranges={ranges}&majorDimension={majorDimension}').json()
    return get['valueRanges'][0]['values']
    
def write_value_spreadsheets(spreadsheet_id:str,ranges:str,values:list):
    
    val={'range':ranges,'values':values}
    data={
            'valueInputOption':"USER_ENTERED",
            'data':val
    }

    access_token=regenerate_access_token()
    change=requests.post(f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchUpdate?access_token={access_token}',data=json.dumps(data)).text
    return change

def clear_value_spreadsheets(spreadsheet_id:str,range:str):
    
    access_token=regenerate_access_token()

    clear=requests.post(f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}:clear?access_token={access_token}').text
    return clear

def append_value_spreadsheets(spreadsheet_id:str,range:str,values:list,insert_option='INSERT_ROWS'):
    
    val={'range':range,'values':values}

    access_token=regenerate_access_token()
    
    append=requests.post(f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}:append?access_token={access_token}&valueInputOption=USER_ENTERED&insertDataOption={insert_option}',data=json.dumps(val)).text
    return append

def delete_rows_columns(spreadsheet_id:str,sheet_code:int,fr:int,t:int,dimension='ROWS'):
    
    config={
      "deleteDimension": {
        "range": {
          "sheetId": sheet_code ,
          "dimension": dimension ,
          "startIndex": fr,
          "endIndex": t
        }
      }
    }

    val={"requests":[config]}

    access_token=regenerate_access_token()
    m=requests.post(f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}:batchUpdate?access_token={access_token}',data=json.dumps(val))
    return m.json()
if __name__ =='__main__':
    scope='https://www.googleapis.com/auth/spreadsheets'
    sheet_id='1Wp4cpdJpK3LKhI9Cf0_iRxJMzZ08YbdGaOlukZzgZLE'
    m=['122,6745']*3
    print(append_value_spreadsheets(sheet_id,'testing!A1:ZZ1',[m]))
