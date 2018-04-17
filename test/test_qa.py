#!/usr/bin/python3
import requests


def clear():
    url = 'http://10.9.187.138:7001/dev/com.youzan.beauty.goods.biz.promoter.mock.PromotionMockServiceImpl/1.0.0/runJobOnServer?json={"jobName":"clear","opType":"current"}&no_session=1'
    r = requests.get(url)
    print(r.text)

if __name__ == '__main__':
    pass
