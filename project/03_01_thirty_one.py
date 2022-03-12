from random import *

call = 0
count = randint(0, 1)

while call < 31:
    count += 1
    if count % 2 == 1:
        p = int(input('몇 개 부를까 :'))
        while p not in range(1, 4):
            print('1 ~ 3사이의 숫자를 입력!')
            p = int(input('몇 개 부를까 :'))

        for i in range(p):
            call += 1
            print('나 : {0}'.format(call))
            if call == 31:
                print('컴퓨터 승')
                break
    elif count % 2 == 0:
        c = randrange(1, 4)
        for i in range(c):
            call += 1
            print('컴퓨터 : {0}'.format(call))
            if call == 31:
                print('플레이어 승')
                break