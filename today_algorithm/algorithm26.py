# 프로그래머스 프린터

def solution(priorities, location):
    answer = 0
    index_list = []
    for index, val in enumerate(priorities):
        index_list.append([index,val])
    
    while len(priorities) != 0:
        max_num = max(priorities)
        pop = index_list.pop(0)
        pop2 = priorities.pop(0)
        if max_num == pop[1]:
            answer += 1
            if pop[0] == location:
                break
        else:
            index_list.append(pop)
            priorities.append(pop2)
    return answer


a = [2, 1, 3, 2]
b = 2
c = [1, 1, 9, 1, 1, 1]
d = 0
print(solution(a,b))
print(solution(c,d))