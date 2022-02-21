# def solution(citations):
#     answer = 0
#     for i in range(len(citations)):
#         if citations[i] > citations[i+1]:
#             answer = citations[i]
#     print(answer)
#     return answer


# def solution(citations):
#     citations.sort(reverse=True)
#     for i in range(1, len(citations)):
#         if len(citations) == citations[i]:

#     return

# def solution(citations):
#     citations.sort()
#     for i,j in enumerate(citations):
#         if j == len(citations[i:]):
#             result = len(citations[i:])
#             break
#     return result


# h-index = 1번이상 인용 1개 나머지 논문이 1개이하, 2번이상 2개 나머지논문이 2개이하, 3번이상 3개 나머지 논문이 3개이하.... 
# 인용된횟수 = 인용된 논문 수,  나머지논문 =< 인용된횟수

def solution(citations):
    citations.sort() # 0,1,3,5,6
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i: # 인용된 횟수 , 나머지논문수
          return len(citations)-i  
    return 0


print(solution([3, 0, 6, 1, 5]))
