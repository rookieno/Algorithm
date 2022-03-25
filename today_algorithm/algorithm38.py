# 백준 11651번 좌표 정렬하기2
n = int(input())

list = []

for i in range(n):
    x, y = map(int,input().split())
    list.append((x,y))

list = sorted(list, key=lambda x:(x[1],x[0]))

for i in list:
    print(f'{i[0]} {i[1]}')