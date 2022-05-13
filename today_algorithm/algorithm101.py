# 백준 2477번 참외밭

n = int(input())

index_list = []

idx = 0
x = 0
y = 0
x_idx = 0
y_idx = 0

for i in range(6):
    a, b = map(int, input().split())
    index_list.append((idx,b))
    if a == 1 or a == 2:
        if x < b:
            x = b
            x_idx = idx
    else:
        if y < b:
            y = b
            y_idx = idx
    idx += 1

index_list = sorted(index_list, key=lambda x:x[0])

for i in range(6):
    if i == x_idx:
        x1 = abs(index_list[(i+5)%6][1] - index_list[(i-5)%6][1])
    elif i == y_idx:
        y1 = abs(index_list[(i+5)%6][1] - index_list[(i-5)%6][1])


answer = (x*y-x1*y1) * n

print(answer)

