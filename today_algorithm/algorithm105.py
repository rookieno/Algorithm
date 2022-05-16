# 백준 14425번 문자열집합

# 리스트 O(n) 시간 4676ms
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


# 딕셔너리 O(1) 시간 1104ms
n, m = map(int, input().split())

s = {}
cnt = 0

for _ in range(n):
    answer = input()
    s[answer] = True

for _ in range(m):
    word = input()
    if word in s.keys():
        cnt += 1

print(cnt)