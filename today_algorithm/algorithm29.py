# 프로그래머스 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트를 힙으로
    while scoville[0] < K: # 효율성을 위해 0번째 = 제일 작은수
        try:
            answer += 1
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            result = a + (b*2)
            heapq.heappush(scoville,result)
        except: # 예외
            return -1
    return answer

a = [1, 2, 3, 9, 10, 12]
b = 7
print(solution(a,b))