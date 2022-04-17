# 백준 3009번 네 번째 점
x_all = []
y_all = []
answer = []
for _ in range(3):
    x, y = map(int, input().split())
    x_all.append(x)
    y_all.append(y)


for i in x_all:
    if x_all.count(i) == 1:
        answer.append(i)

for i in y_all:
    if y_all.count(i) == 1:
        answer.append(i)

print(answer[0],answer[1])
