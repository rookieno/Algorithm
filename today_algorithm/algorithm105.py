# 백준 14425번 문자열집합

n, m = map(int, input().split())

s = []

cnt = 0

for _ in range(n):
    s.append(input())

for _ in range(m):
    word = input()

    if word in s:
        cnt += 1

print(cnt)