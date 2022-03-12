import random
from random import *

# 2 6 10 14 18 22 26 30 을 컴퓨터가 말하면 된다
# 즉 4n+2 를 컴퓨터가 말해야 한다!
# 플레이어가 먼저 4n+2의 숫자를 차지하면 실수하지 않는 이상 지지않음.
# 예외처리 : 플레이어가 4n+2를 차지하면 컴퓨터는 다시 랜덤으로 1~3횟수 출력

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


def ai_c_call(now_call):
    if now_call % 4 == 0:
        com_call = 2
    elif now_call % 4 == 1:
        com_call = 1
    elif now_call % 4 == 3:
        com_call = 3
    else:
        com_call = randrange(1, 4)

    return com_call


call = 0
count = randint(0, 1)

while call < 31:
    count += 1
    if count % 2 == 1:
        p = int(input('몇 개 부를까 :'))
        while p not in range(1, 4) or call + p > 31:
            print('1 ~ 3사이의 숫자를 입력!')
            p = int(input('몇 개 부를까 :'))
        call = p_call(p, call)

    elif count % 2 == 0:
        c = ai_c_call(call)
        call = c_call(c, call)






