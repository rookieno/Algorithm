# 백준 3034번 앵그리 창영

n, w, h = map(int, input().split())

len = []

for i in range(n):
    len.append(int(input()))

for i in len:
    if i <= h or i <= w or i <= (w**2+h**2)**0.5:
        print('DA')
    else:
        print('NE')