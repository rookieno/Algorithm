# 백준 11650번 좌표 정렬하기 2
n = int(input())

graph = []

for _ in range(n):
    x, y = map(int, input().split())
    graph.append((x,y))

graph = sorted(graph, key=lambda x:(x,x))

for i in graph:
    print(i[0], i[1])
