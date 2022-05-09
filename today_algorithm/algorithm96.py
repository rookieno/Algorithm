# 백준 18870번 좌표 압축

# 시간초과
# import sys

# input = sys.stdin.readline

# n = int(input())

# graph = list(map(int, input().split()))

# answer = []

# for i in graph:
#     cnt = 0
#     for j in graph:
#         if i > j:
#             cnt += 1
#     answer.append(cnt)

# print(' '.join(map(str,answer)))

# 시간 초과
# list.index(target) 시간복잗도 O(N)
# n = int(input())

# graph = list(map(int, input().split()))

# sorted_graph = sorted(list(set(graph)))

# for idx, i in enumerate(graph):
#     graph[idx] = sorted_graph.index(i)

# print(' '.join(map(str, graph))

# 인덱싱 낮은 시간복잡도로 하는법 딕셔너리 이용 시간복잡도 O
n = int(input())

graph = list(map(int, input().split()))

sorted_graph = sorted(list(set(graph)))

dic = {}

for i in range(len(sorted_graph)):
    dic[sorted_graph[i]] = i

for i in graph:
    print(dic[i], end=' ')

    





