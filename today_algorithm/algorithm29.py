# 프로그래머스 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            answer += 1
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            result = a + (b*2)
            heapq.heappush(scoville,result)
        except:
            return -1
    return answer

a = [1, 2, 3, 9, 10, 12]
b = 7
print(solution(a,b))