# 백준 2798번 블랙잭
from itertools import combinations

n ,m = map(int, input().split())

cards = list(map(int, input().split()))

pick = list(combinations(cards, 3))

result = []

answer = 0

for i in pick:
    result.append(sum(i))

for i in result:
    if i <= m and m-i < m-answer:
        if answer == 0:
            answer = i
        answer = i

print(answer)
