# 백준 2981번 검문
# 시간초과
# import sys

# input = sys.stdin.readline

# n = int(input())

# nums = []

# answer = []

# for _ in range(n):
#     num = int(input())
#     nums.append(num)

# target = 1

# while target != max(nums):
#     check = []
#     target += 1
#     for i in nums:
#         check.append(i%target)
#     if len(set(check)) == 1:
#         answer.append(target)

# print(' '.join(map(str,answer)))

import sys

input = sys.stdin.readline

n = int(input())

answer = []

for _ in range(n):
    nums = list(map(int, input().split()))

print(nums)

target = 1

while target != max(nums):
    check = []
    target += 1
    for i in nums:
        check.append(i%target)
    if len(set(check)) == 1:
        print(target, end=' ')

