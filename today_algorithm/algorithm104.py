# 백준 10815번 숫자카드

n = int(input())

nums = set(list(map(int, input().split())))

m = int(input())

target = list(map(int, input().split()))

answer = []

in_nums = nums - set(target)

in_target = set(target) - nums

result = set(target) - in_target

print(result)

# for i in target:
#     while True:
#         half = len(nums)//2
#         cur_num = nums[half]
        
#         if i == cur_num:
#             answer.append(1)
#         elif i < cur_num:
#             nums = nums[half:]
#         elif i > cur_num:
#             nums = nums[:half]
#         elif len(nums) == 1:
#             answer.append(0)
#             break
answer = []

for i in target:
    if i in result:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
        
       
        
