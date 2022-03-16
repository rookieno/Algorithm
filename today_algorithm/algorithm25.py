# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = []
    dict = { 6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    count = 0
    zero = 0
    for i in lottos:
        if i != 0 and i in win_nums:
            count += 1
        elif i == 0:
            zero += 1
    answer.append(dict[count+zero])
    answer.append(dict[count])

    return answer

def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    zero = lottos.count(0)
    cur = 0
    for i in win_nums:
        if i in lottos:
            cur += 1
    answer.append(rank[zero+cur])
    answer.append(rank[cur])
    return answer


lotto = [44, 1, 0, 0, 31, 25]
win = 	[31, 10, 45, 1, 6, 19]

a = [0, 0, 0, 0, 0, 0]
b = [38, 19, 20, 40, 15, 25]

print(solution(lotto,win))
print(solution(a,b))