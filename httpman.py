#!/usr/bin/python3
import requests
from collections import namedtuple

def get_food():
    url = 'https://mainsite-restapi.ele.me/pizza/v3/restaurants'
    ele_sid = 'gFN2KpblVQDbaqTpAJuffGAjgWFVWIZ2UA7w'
    user_id = 265117117
    payload = {}
    payload['offset'] = 0
    payload['limit'] = 10
    payload['latitude'] = 22.524003
    payload['longitude'] = 113.935394
    payload['extras'] = ['activities']
    payload['extra_filters'] = 'home'
    payload['keyword']=None
    payload['order_by'] = 6
    payload['terminal'] = 'weapp'
    payload['user_id'] = user_id
    headers = {'User-Agent':"Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 MicroMessenger/6.6.3 NetType/WIFI Language/zh_CN",
               'Cookie':'SID=gFN2KpblVQDbaqTpAJuffGAjgWFVWIZ2UA7w; USERID=26511711'}
    r = requests.get(url=url,params=payload,verify=False,headers=headers)
    return r.json()

if __name__ == '__main__':
    r = get_food()
    items = r.get('items')

    for item in items:
        shopName = item.get('restaurant').get('name','')
        address = item.get('restaurant').get('address','')
        mobile = item.get('restaurant').get('phone','')
        supports = item.get('restaurant').get('supports')
        Food = namedtuple('Food',['name','original_price','price'])
        foods = item.get('foods')
        for temp in foods:
            f = Food(temp.get('name'),temp.get('original_price'),temp.get('price'))
            print(f)
        print(shopName,address,mobile,supports)
        print('-'*20)
