# 프로그래머스 신고 결과 받기
def solution(id_list, report, k):
    answer = dict(zip(id_list, len(id_list)*[0]))
    result = {}
    check_user = {}

    for i in id_list:
        result[i] = []

    for i in report:
        user = i.split(' ')[0]
        target_user = i.split(' ')[1]
        if target_user not in result[user]:
            result[user].append(target_user)
            if target_user in check_user:
                check_user[target_user] += 1
            else:
                check_user[target_user] = 1
    
    for i,j in check_user.items():
        for a,b in result.items():
            if j >= k:
                if i in b:
                    answer[a] += 1
    print(check_user)
    print(result)
    return list(answer.values())

a = ["muzi", "frodo", "apeach", "neo"]
b = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
c = 2
print(solution(a,b,c))

a1 = ["con", "ryan"]
b1 = ["ryan con", "ryan con", "ryan con", "ryan con"]
c1 = 3
print(solution(a1,b1,c1))
