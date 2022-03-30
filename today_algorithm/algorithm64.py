# 백준 1021번 회전하는 큐
from collections import deque
import sys

n, m = map(int, input().split())

que = deque(range(1,n+1))

a = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in a:
    while True:
        if i == que[0]:
            que.popleft()
            break
        else:
            if que.index(i) < len(que)/2:
                while i != que[0]:
                    que.append(que.popleft())
                    cnt += 1
            else:
                while i != que[0]:
                    que.appendleft(que.pop())
                    cnt += 1
print(cnt)