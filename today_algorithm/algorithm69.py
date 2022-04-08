# 백준 15650번 N과 M (2)
from itertools import combinations
import sys
import re

# n, m = map(int, sys.stdin.readline().split())

# n_list = [i for i in range(1, n+1)]

# result = list(combinations(n_list, m))

# for i in result:
#     a = list(map(int,re.findall(r'\d', str(i))))
#     for i in range(m):
#         print(f'{a[i]}',end=' ')

result = []

def DFS(start_node):
    if len(result) == m: # result = [1,2]
        print(' '.join(map(str,result))) # 1 2 출력
        return # 재귀 끝 아래 pop()
    for i in range(start_node, n+1):
        if i not in result:
            result.append(i) # 1 추가 result = [1] -> 2 추가 result = [1,2]
            DFS(i+1) # DFS(2) 시작 -> DFS(3) 시작
            result.pop()

DFS(1)

