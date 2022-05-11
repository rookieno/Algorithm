# 백준 2477번 참외밭

n = int(input())

dic = {}

for i in range(6):
    a, b = map(int, input().split())
    if len(dic[a]) == 0:
        dic[a] = b
    else:
        dic[a] = dic[a],b

print(dic)