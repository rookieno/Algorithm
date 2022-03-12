import random
from random import *


def p_call(num, called):
    for i in range(num):
        called += 1
        print('나 : {0}'.format(called))

        if called == 31:
            print('컴퓨터 승')
            break
    return called


def c_call(num, called):
    for i in range(num):
        called += 1
        print('컴퓨터 : {0}'.format(called))

        if called == 31:
            print('플레이어 승')
            break
    return called


call = 0
count = randint(0, 1)

while call < 31:
    count += 1
    if count % 2 == 1:
        p = int(input('몇 개 부를까 :'))
        while p not in range(1, 4):
            print('1 ~ 3사이의 숫자를 입력!')
            p = int(input('몇 개 부를까 :'))
        call = p_call(p, call)

    elif count % 2 == 0:
        c = randrange(1, 4)
        call = c_call(c, call)






