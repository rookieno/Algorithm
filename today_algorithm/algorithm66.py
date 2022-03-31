# 백준 1260번 DFS와 BFS
from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().split())

# graph = [[] for _ in range(n+!)]
# for i in range(m):
#     a ,b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     graph[a].sort()
#     graph[b].sort()

# def DFS(adjacent_graph, start_node):
#     stack = [start_node]
#     visited = []
#     while stack:
#         current_node = stack.pop()
#         visited.append(current_node) # start_node
#         for adjacent_node in adjacent_graph[current_node]:
#             if adjacent_node not in visited:
#                 stack.append(adjacent_node)
#     return visited

# print(graph) [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a ,b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

#print(graph) [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]]

def DFS(adjacent_graph, start_node):
    visited += [start_node]
    for i in range(len(adjacent_graph[start_node])):
        if adjacent_graph[start_node][i] == 1 and i not in visited:
            DFS(i, visited)
    return visited


    
print(DFS(graph, v))