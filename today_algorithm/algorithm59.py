# 백준 1934번 최소공배수
import math

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    gcd = math.gcd(a,b)
    lcm = a*b/gcd
    print(int(lcm))
