# 백준 2108번 통계학
import sys
from collections import Counter

n = int(sys.stdin.readline())

nums = []

for i in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)

nums.sort()


a = round(sum(nums)/n)
b = nums[(n//2)]

sorted_count = Counter(nums).most_common()

if len(sorted_count) > 1:
    if sorted_count[0][1] == sorted_count[1][1]:
        c = sorted_count[1][0]
    else:
        c = sorted_count[0][0]
else:
    c = sorted_count[0][0]


d = max(nums) - min(nums)


print(a)
print(b)
print(c)
print(d)