from random import *

c = randrange(1, 101)

for i in range(1, 6):
    p = int(input())
    if p not in range(1, 101):
        print('1부터 100까지의 숫자를 입력하세요')
        break
    if p < c:
        print('업')
    elif p == c:
        print('성공')
        break
    else:
        print('다운')

if p != c:
    print('실패')





