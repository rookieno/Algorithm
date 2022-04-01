# 백쥰 2630번 색종이 만들기
from re import L
import sys

n = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = []

def divide(x, y, n):
    taget = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if taget != paper[i][j]:
                divide(x,y,n//2)
                divide(x,y+n//2,n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2, n//2)
                return
    if taget == 0:
        result.append(0)
    else:
        result.append(1)


divide(0,0,n)
print(result.count(0))
print(result.count(1))
