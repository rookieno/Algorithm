# 프로그래머스 소수 만들기
from itertools import combinations

def solution(nums):
    answer = 0
    sum_list = list(combinations(nums,3))
    
    for i in sum_list:
        if prime_num(sum(i)):
            answer += 1

    return answer

def prime_num(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

a = [1,2,3,4]
print(solution(a))