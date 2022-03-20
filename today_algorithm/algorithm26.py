# 프로그래머스 프린터

def solution(priorities, location):
    answer = 0
    index_list = [] # 인덱스를 포함한 배열
    for index, val in enumerate(priorities):
        index_list.append([index,val])
    
    while len(priorities) != 0:
        max_num = max(priorities) # 제일 높은 숫자 매번 초기화
        pop = index_list.pop(0) # 첫번째 뽑기
        pop2 = priorities.pop(0)
        if max_num == pop[1]: # 첫번째 값이 제일 높은 숫자면
            answer += 1 # 빼주고 +1
            if pop[0] == location: # 뽑은 값의 인덱스가 location과 같으면 종료
                break
        else:
            index_list.append(pop) # 아닐시 제일 뒷쪽으로 append
            priorities.append(pop2)
    return answer


a = [2, 1, 3, 2]
b = 2
c = [1, 1, 9, 1, 1, 1]
d = 0
print(solution(a,b))
print(solution(c,d))