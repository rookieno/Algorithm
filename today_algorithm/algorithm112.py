# 백준 9375번 패션왕 신해빈

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = {}
    answer = 1
    for _ in range(n):
        a, b = map(str, input().split())
        if b in clothes:
            clothes[b] += 1
        else:
            clothes[b] = 1

    for key, value in clothes.items():
        answer *= (value + 1)

    print(answer-1)


