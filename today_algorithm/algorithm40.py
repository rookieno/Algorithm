def solution(dartResult):
    answer = 0
    result = []
    for i in dartResult:
        if i.isdigit():
            answer += int(i)
        elif i == 'S':
            answer = answer ** 1
            result.append(answer)
            answer = 0
        elif i == 'D':
            answer = answer ** 2
            result.append(answer)
            answer = 0
        elif i == 'T':
            answer = answer ** 3
            result.append(answer)
            answer = 0
        elif i == '*':
            for i,j in enumerate(result):
                result[i] = j*2
                print(result[i])
        elif i == '#':
            result[-1] = -result[-1]
    print(result)      

    return sum(result)


print(solution("1D2S3T*"))