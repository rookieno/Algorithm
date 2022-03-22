# 백준 2839번 설탕배달
n = int(input())

num = 0
while True:
    if n % 5 == 0:
        num = num + n//5
        print(num)
        break
    n = n - 3
    num += 1
    if n < 0:
        print(-1)
        break