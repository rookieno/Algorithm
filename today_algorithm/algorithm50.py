# 프로그래머스 폰켓몬
from itertools import combinations

def solution(nums):
    answer = []
    pick = list(combinations(nums, 2))
    for i in pick:
        if sum(i) not in answer:
            print(sum(i))
            answer.append(sum(i))
    print(answer)
    return len(answer)

a = [3,1,2,3]
print(solution(a))