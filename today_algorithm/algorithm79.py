# 백준 1085번 직사각형에서 탈출
import sys

input = sys.stdin.readline

a = list(map(int, input().split()))

x = min(abs(a[0]-0),abs(a[2]-a[0]))
y = min(abs(a[1]-0),abs(a[3]-a[1]))

result = min(x,y)
print(result)