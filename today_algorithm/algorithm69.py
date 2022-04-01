# 백준 15650번 N과 M (2)
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())

n_list = [i for i in range(1, n+1)]

print(n_list)

result = list(combinations(n_list, m))

print(result)

for i in range(len(result)):
    print(f'{result[i][0]} {result[i][1]}')
