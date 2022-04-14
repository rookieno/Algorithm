# 백준 2579번 계단오르기
import sys

input = sys.stdin.readline

n = int(input())

steps = [0] * 301
dp = [0] * 301

for i in range(n):
    steps[i] = int(input())

if n == 1:
    print(steps[0])
elif n == 2:
    print(steps[0] + steps[1])
else:
    dp[0] = steps[0]
    dp[1] = steps[0] + steps[1]
    dp[2] = max(steps[1]+steps[2], steps[0]+steps[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3]+steps[i]+steps[i-1], dp[i-2]+steps[i])
    
print(dp[n-1])