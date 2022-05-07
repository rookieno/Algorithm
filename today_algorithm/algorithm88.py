# 백준 2750번 수 정렬하기

n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()

for i in nums:
    print(i)
