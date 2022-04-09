# 1번
def solution(arr):
    answer = []
    nums = [arr.count(1),arr.count(2),arr.count(3)]
    target = max(nums)
    for i in nums:
        if i < target:
            answer.append(target-i)
        else:
            answer.append(0)
    return answer

a = [2,1,3,1,2,1]
b = [3,3,3,3,3,3]
c = [1,2,3]

print(solution(a))
print(solution(b))
print(solution(c))