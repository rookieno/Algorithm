# 프로그래머스 예산
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1
    return answer

a = [1,3,2,5,4]
b = 9

print(solution(a,b))