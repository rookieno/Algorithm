# 내 풀이
list = []

for i in range(1, 10):
    n = int(input())
    list.append(n)

max_num = list[0]
max_num_index = 0

for list_index in list:
    if list_index > max_num:
        max_num = list_index
print(max_num)

for index in list:
    max_num_index += 1
    if index == max_num:
        break
print(max_num_index)

print(max(list))
print(list.index(max(list))+1)

