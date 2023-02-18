import requests as req
import json
import datetime
import time

base_url= 'https://www.binance.com/bapi/earn/v1/friendly/pos/union'
params = {'status':'ALL','asset':'axs'}
log_data=[]


def get_staking_data():
    proj=get_status()
    email_data=[]
    for i in proj:
        if i['available']:
            email_data.append(i)
        log_data.append(i)
    return email_data, log_data


def get_status():
    response = req.get(base_url,params=params)
    rr=json.loads(response.content)
    data=[]
    if len(rr['data'])>0:
        for asset in rr['data']:
            if len(asset['projects']) > 0:
                for proj in asset['projects']:
                    data.append({'asset': proj['asset']+' '+ proj['duration'],
                                          'available': not proj['sellOut'] ,
                                          'time':str(datetime.datetime.now().strftime("%H:%M:%S  , %d-%b-%Y "))})
    return data