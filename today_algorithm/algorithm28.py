# 프로그래머스 주식가격
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices):
        cnt = 0
        a = prices.popleft()
        for i in prices:
            if a <= i:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer

a = [1, 2, 3, 2, 3]	
print(solution(a))