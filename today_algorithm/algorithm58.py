# 백준 9012번 괄호
n = int(input())

for i in range(n):
    vps = input()
    stack = []
    for j in vps:
        if j == '(':
            stack.append(j)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(j)
                break

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

