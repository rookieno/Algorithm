# 프로그래머스 폰켓몬
from itertools import combinations

def solution(nums):
    answer = 0
    pick = len(nums)//2
    num_list = list(set(nums))
    
    if pick > len(num_list):
        answer += len(num_list)
    else:
        answer += pick

    return answer

a = [3,1,2,3]
print(solution(a))