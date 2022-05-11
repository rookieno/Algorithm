# 백준 2981번 검문
# 시간초과
import sys

input = sys.stdin.readline

n = int(input())

nums = []

answer = []

for _ in range(n):
    num = int(input())
    nums.append(num)

target = 1

while target != max(nums):
    check = []
    target += 1
    for i in nums:
        check.append(i%target)
    if len(set(check)) == 1:
        answer.append(target)

print(' '.join(map(str,answer)))

# 알고리즘 분류 : 수학, 정수론, 유클리드 호재법
# 약수를 이용해보자
import sys
from math import gcd

input = sys.stdin.readline

n = int(input())

answer = []

nums = []

for _ in range(n):
    num = int(input())
    nums.append(num)

result = [nums[i] - nums[i-1] for i in range(1, n)]

target = result[0]

for i in range(1, len(result)):
    target = gcd(target, result[i])


for i in range(2, int(target**0.5)+1):
    if target % i == 0:
        answer.append(i)
        answer.append(target//i)
    
answer.append(target)

answer = list(set(answer))

answer.sort()

print(*answer)