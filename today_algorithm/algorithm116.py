# 백준 25305번 커트라인
n, k = map(int, input().split())

score = list(map(int, input().split()))

score.sort()

print(score[-k])