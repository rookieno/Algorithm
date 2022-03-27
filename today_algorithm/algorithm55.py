# 프로그래머스 신고 결과 받기
def solution(id_list, report, k):
    answer = []
    push_report = []
    
    for i in report:
        push_report.append([i.split(' ')])
    
    for i in push_report:
        i
    return answer

a = ["muzi", "frodo", "apeach", "neo"]
b = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
c = 2
print(solution(a,b,c))