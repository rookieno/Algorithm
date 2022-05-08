# 백준 10989번 수 정렬하기 3
import sys

n = int(sys.stdin.readline())

result = [0] * 10001

for _ in range(n):
    target = int(sys.stdin.readline())
    result[target] = result[target] + 1

for i in range(10001):
    if result[i] != 0:
        for _ in range(result[i]):
            print(i)