# 백준 11478번 서로 다른 부분 문자열의 개수

s = str(input())

answer = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        result = s[i:j+1]
        answer.add(result)

print(answer)