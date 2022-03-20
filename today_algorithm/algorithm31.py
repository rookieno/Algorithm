# 프로그래머스 시저 암호
def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.islower():
            i = chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            answer += i
        else:
            i = chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            answer += i

    return answer

s = "z"
n = 1
print(solution(s,n))