from collections import namedtuple
from colorama import Fore, Style
from prettytable import PrettyTable
from models import EatType
from models import Unchange
from httpman import get_food

def menu():
    print(Fore.RED + "*" * 10 + Fore.RED + "欢迎光临今晚吃啥" + "*" * 10)
    print(Fore.BLACK + "1:固定餐食")
    print(Fore.BLACK + "2:外卖点餐")
    print(Fore.BLACK + "3:随缘吃点")
    print(Fore.BLACK + "q:出门吃肉")
    choice = input(Fore.BLUE + "请输入想做的编号：")
    switchs = {EatType.UNCHANGE.value: unchanged, EatType.WAIMAI.value: waimai}
    res, choice = check_choice(choice)
    if res:
        switchs[choice]()
    else:
        print(Fore.RED + "瞎几把输!")
        exit()


def check_choice(arg):
    """
    检查choice
    :param arg:
    :return:
    """
    if arg is not None and arg in [
            EatType.UNCHANGE.value,
            EatType.WAIMAI.value,
            EatType.RANGE.value,
            'q']:
        if arg == 'q':
            print(Fore.BLUE + "出门吃肉 拜拜")
            exit()
        return True, arg
    else:
        return False, None


def unchanged():
    res, uns = Unchange.query()
    x = PrettyTable(['id', 'eatName', 'money', 'updateTime', 'count'])
    if res:
        for i in uns:
            x.add_row([i.uid, i.eatName, i.money, i.updateTime, i.count])
        print(x)


def waimai():
    r = get_food()
    t = PrettyTable(['ID','名称','售价','原价','店铺','地址','联系方式'])
    t.padding_width = 1
    t.align['名称'] = 'l'
    t.align['店铺'] = 'l'
    t.align['地址'] = 'l'
    items = r.get('items')
    index = 1
    for item in items:
        shopName = item.get('restaurant').get('name', '')
        address = item.get('restaurant').get('address', '')
        mobile = item.get('restaurant').get('phone', '')
        supports = item.get('restaurant').get('supports')
        Food = namedtuple('Food', ['id','name', 'original_price', 'price'])
        foods = item.get('foods')
        for temp in foods:
            f = Food(index,temp.get('name'), temp.get('original_price'), temp.get('price'))
            t.add_row([f.id,f.name,f.price,f.original_price,shopName,address,mobile])
            index+=1
    print(Style.RESET_ALL)
    print(Fore.CYAN)
    print(t)
    print(Style.RESET_ALL)

if __name__ == '__main__':
    menu()
