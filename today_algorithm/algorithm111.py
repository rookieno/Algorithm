# 백준 11051본 이항계수 2

# dp
import sys 

n, k = map(int, sys.stdin.readline().split()) 

dp = [[1 for _ in range(k+1)] for _ in range(n+1)] 

for i in range(1, k+1):
     for j in range(i+1, n+1):
        dp[j][i] = (dp[j-1][i-1] + dp[j-1][i]) % 10007 

print(dp[n][k])


# nCr = n!/r!(n-r)! n, r 중복 약분
import sys 

n, k = map(int, sys.stdin.readline().split()) 

top = list(set(range(n+1)) - set(range(k+1)))
bot = list(range(1, n-k+1))

a = 1
b = 1

for i in top:
   a *= i

for i in bot:
    b *= i

print(a//b % 10007)