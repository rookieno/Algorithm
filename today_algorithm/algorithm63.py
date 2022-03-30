# 백준 1874 스택 수열
n = int(input())

stack = []
answer = []
cnt = 1
for i in range(n):
    m = int(input())
    while cnt <= m:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    if stack[-1] == m:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        break
if not stack:
    for i in answer:
        print(i)

        



