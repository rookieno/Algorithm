# 백준 1978 소수찾기

n = int(input())

a = list((map(int, input().split())))
result = 0

for i in a:
    check = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0 or i == 1:
            check = False
    if check == True:
        result += 1
    
print(result)