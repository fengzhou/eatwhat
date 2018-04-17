from colorama import Fore, Style
from prettytable import PrettyTable
from models import EatType
from models import Unchange

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
    print(Style.RESET_ALL + choice)


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


def waimai(arg):
    ele_sid = ''

    pass


if __name__ == '__main__':
    menu()
