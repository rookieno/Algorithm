# def solution(n, stages):
#     clear_stage = []
#     fail_per = []
#     answer = []
#     stages.sort()
#     denominator = len(stages)

#     for i in range(1,n+1):
#         a = stages.count(i)
#         clear_stage.append(a)
    
#     for i in clear_stage:
#         a = i / denominator 
#         denominator -= i
#         fail_per.append(a)

#     stage_fail_per = dict(zip(set(stages), fail_per))

#     result = sorted(stage_fail_per.items(), key=lambda x:x[1], reverse=True)
#     for i in result:
#         if i[0] > n:
#             answer.append(i[0]-1)
#         else:
#             answer.append(i[0])
    
#     return answer

# solution(4, [4,4,4,4,4])

def solution(n, stages):
    result = []
    answer = []
    denominator = len(stages) # 플레이어의 수
    
    for stage in range(1, n+1):
        if denominator != 0: # 도전한 플레이어의 수가 0이 아닐때
            result.append([stage, stages.count(stage)/denominator]) # 분자는 현재 스테이지에 있는 플에이어, 분모는 도전힌 플레이어, 결과로 실패율
            denominator -= stages.count(stage) # 다음 스테이지 넘어갈때 현재 스테이지에 있는 플레이어를 빼줌 (현재 스테이지를 클리어 못한사람)
        else:
            result.append([stage, 0]) # 스테이지를 클리어 하지 못한사람이 없을때, 도전한 플레이어가 0이하가될 때
    result.sort(key=lambda x:x[1],reverse=True) # 리스트에 실패율을 기준으로 내림차순 정렬
    
    for i in range(len(result)):
        a = result[i][0] # 스테이지만 뽕음
        answer.append(a)

    return print(answer)

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4,4,4,4,4])