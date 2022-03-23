# 프로그래머스 문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = []
    for i in strings:
        answer.append((i[n], i))

    sorted_list = sorted(answer, key=lambda x:(x,x))
    answer = []
    for i in sorted_list:
        answer.append(i[1])
    
    return answer