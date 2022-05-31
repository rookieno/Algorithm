# 백준 1676번 팩토리얼 0의 개수

n = int(input())

n_fac = 1

for i in range(1, n+1):
    n_fac *= i

n_fac = list(str(n_fac))[::-1]

answer = 0

for i in n_fac:
    if i == '0':
        answer += 1
    else:
        break

print(answer)
