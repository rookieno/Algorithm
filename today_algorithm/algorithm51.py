# 프로그래머스 모의고사
def solution(answers):
    result = []
    answer = {'1':0,'2':9,'3':0}
    one = [1,2,3,4,5] * int(len(answers))
    two = [2,1,2,3,2,4,2,5] * int(len(answers))
    three = [3,3,1,1,2,2,4,4,5,5] * int(len(answers))
    score_one = 0
    score_two = 0
    scroe_thr = 0
    for i,j in enumerate(answers):
        if j == one[i]:
            score_one += 1
        if j == two[i]:
            score_two += 1
        if j == three[i]:
            scroe_thr += 1
    answer['1'] = score_one
    answer['2'] = score_two
    answer['3'] = scroe_thr
    for i,j in answer.items():
        if max(answer.values()) == j:
            result.append(i)

    return list(map(int,result))

a = [1,3,2,4,2]	

print(solution(a))