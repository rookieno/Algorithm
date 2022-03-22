# 프로그래머스 디스크 컨트롤러
# from collections import deque

# def solution(jobs):
#     answer = 0
#     time = 0
#     run = 0
#     jobs.sort()
#     deq = deque(jobs)
#     while True:
#         time += 1
#         if deq[0][0] == time:
#             run = deq[0][1]
#             run -= 1
#             if run == 0:
#                 deq.popleft()

#     return answer

import heapq

def solution(jobs):
    answer = 0
    
    return answer

a = [[0, 3], [1, 9], [2, 6]]
print(solution(a))