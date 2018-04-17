from enum import Enum
from datetime import datetime
import sqlite3


class EatType(Enum):
    UNCHANGE = "1"  # 固定类型的
    WAIMAI = "2"  # 外卖类型的
    RANGE = "3"  # 随机类型的


def get_connect():
    try:
        return sqlite3.connect(r'./db/eatwhat.db')
    except Exception as e:
        print(e)
        return None


class DBase(object):

    conn = get_connect()
    cursor = conn.cursor()

    @classmethod
    def clear_connect(cls):
        if cls.cursor:
            cls.cursor.close()
        if cls.conn:
            cls.conn.close()


class Unchange(DBase):
    def __init__(
            self,
            uid,
            eatName,
            money=0.00,
            updateTime=datetime.now(),
            count=0):
        self.uid = uid,
        self.eatName = eatName
        self.money = money
        self.updateTime = updateTime
        self.sql = None
        self.count = count

    def __repr__(self):
        return 'Unchange id:{0},eatName:{1},money:{2},updateTime:{3}'.format(
            self.uid, self.eatName, self.money, self.updateTime)

    def update(self):
        pass

    def insert(self):
        try:
            self.sql = '''insert into unchanges(id,eatName,money,updateTime,count) values(:id,:eatName,:money,:updateTime,:count)'''
            self.cursor.execute(self.sql,
                                {'id': self.uid,
                                 'eatName': self.eatName,
                                 'money': self.money,
                                 'updateTime': self.updateTime,
                                 'count': self.count})
            self.conn.commit()
            return True, None
        except Exception as e:
            return False, e
        finally:
            self.clear_connect()

    @classmethod
    def query(cls):
        try:
            sql = '''select id,eatName,money,updateTime,count from unchanges'''
            results = cls.cursor.execute(sql)
            res = [cls.__inc(i) for i in results]
            return True, res
        except Exception as e:
            return False, e
        finally:
            cls.clear_connect()

    def delete(self):
        pass

    @classmethod
    def __inc(cls, t):
        unchange_model = ('uid', 'eatName', 'money', 'updateTime', 'count')
        temp = dict(zip(unchange_model, t))
        tt = Unchange(
            temp.get('uid'),
            temp.get('eatName'),
            temp.get('money'),
            temp.get('updateTime'),
            temp.get('count'))
        tt.uid = temp.get('uid')
        return tt


class Shop(object):
    def __init__(self, shopName, address, mobile):
        self.shopName = shopName
        self.address = address
        self.mobile = mobile


class Food(Shop):
    def __init__(
            self,
            shopName,
            address,
            mobile,
            foodName,
            originalPrice,
            price,
            imagetext,
            activities=[],
            supports=[]):
        # originalPrice 原价 price 折扣价  imagetext：折扣 activities 优惠 supports 食品保障
        super(Food, self).__init__(shopName, address, mobile)
        self.foodName = foodName
        self.originalPrice = originalPrice
        self.price = price
        self.imagetext = imagetext
        self.activities = activities
        self.supports = supports
    pass


if __name__ == '__main__':
    res, uns = Unchange.query()
    for i in uns:
        print(i)
