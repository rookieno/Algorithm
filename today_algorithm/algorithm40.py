# 프로그래머스 [1차] 다트 게임
def solution(dartResult):
    answer = ''
    result = []
    for i in dartResult:
        if i.isdigit():
            answer += i
        elif i == 'S':
            result.append(int(answer) ** 1)
            answer = ''
        elif i == 'D':
            result.append(int(answer) ** 2)
            answer = ''
        elif i == 'T':
            result.append(int(answer) ** 3)
            answer = ''
        elif i == '*':
            if len(result) == 1:
                result[-1] = result[-1] * 2
            else:
                result[-2] = result[-2] * 2
                result[-1] = result[-1] * 2
        elif i == '#':
            result[-1] = -result[-1]      

    return sum(result)