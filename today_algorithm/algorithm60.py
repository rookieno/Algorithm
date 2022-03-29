# 백준 11050번 이항계수
from itertools import combinations

a, b = map(int,input().split())

a = range(a)

answer = list(combinations(a,b))

print(len(answer))