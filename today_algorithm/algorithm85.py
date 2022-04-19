# 백준 2231번 분해합

n = int(input())
target = n
answer = []
while True:
    n -= 1
    num_list = list(map(int, str(n)))
    result = n + sum(num_list)
    if result == target:
        answer.append(n)
    elif n == 0:
        if answer:
            break
        print(0)
        break

if answer:
    print(answer[-1])