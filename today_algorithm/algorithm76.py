# 백준 2581번 소수
m = int(input())
n = int(input())

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

first = 0
cnt = 0
result = 0
for i in range(m, n+1):
    if i != 1:
        if is_prime(i) == True:
            cnt += 1
            result += i
            if cnt == 1:
                first += i
if result != 0:
    print(result)
    print(first)
else:
    print(-1)