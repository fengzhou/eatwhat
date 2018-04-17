import sqlite3
from datetime import datetime
from models import Unchange

conn = sqlite3.connect(r'./db/eatwhat.db')
cursor = conn.cursor()
# sql = '''create table unchanges(
#         id int,
#         eatName VARCHAR ,
#         money FLOAT ,
#         updateTime DATETIME
#       )'''
#
#
# sql = '''insert into unchanges(id,eatName,money,updateTime) values(:id,:eatName,:money,:updateTime)'''
# cursor.execute(sql,{'id':1,'eatName':'test','money':12.88,'updateTime':datetime.now()})
#
# conn.commit()
#
#
# cursor.close()
# conn.close()


sql = '''select * from unchanges'''

results = cursor.execute(sql)

unchange_model = ('id','eatName','money','updateTime','count')

def inc(t):
    unchange_model = ('id','eatName','money','updateTime','count')
    t = dict(zip(unchange_model,t))
    return Unchange(t.get('id'),t.get('eatName'),t.get('money'),t.get('updateTime'),t.get('count'))


if __name__ == '__main__':
    us = [inc(i) for i in results]
    print(us)
