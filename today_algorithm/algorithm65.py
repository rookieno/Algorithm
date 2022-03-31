# 백준 18258본 큐2
from collections import deque
import sys
n = int(input())

que = deque([])

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        que.append(order[-1])
    elif order[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print('-1')
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if que:
            print('0')
        else:
            print('1')
    elif order[0] == 'front':
        if que:
            print(que[0])
        else:
            print('-1')
    elif order[0] == 'back':
        if que:
            print(que[-1])
        else:
            print('-1')
