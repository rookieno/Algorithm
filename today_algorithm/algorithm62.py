# 백준 4949번 균형잡힌 세상
while True:
    n = input()
    stack1 = []
    if n == '.':
        break
    for i in n:
        if i == '(' or i == '[':
            stack1.append(i)
        elif i == ')':
            if stack1 and stack1[-1] == '(':
                stack1.pop()
            else:
                print('no')
                break
        elif i ==']':
            if stack1 and stack1[-1] == '[':
                stack1.pop()
            else:
                print('no')
                break
    if i == '.':
        if len(stack1) == 0:
            print('yes')
        else:
            print('no')

    