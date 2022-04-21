# 백준 7568번 덩치
from pyrsistent import b


n = int(input())

answer = []

big = []

for i in range(n):
    x, y = map(int, input().split())
    big.append((x,y))

print(big)