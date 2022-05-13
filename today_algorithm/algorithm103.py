# 백준 1358번 하키

w, h, x, y, p = map(int, input().split())

cnt = 0

for _ in range(p):
    a, b  = map(int, input().split())

    y1 = y+h/2
    x1 = x+h

    if a >= x and a <= x+w and b >= y and b <= y+h:
        cnt += 1
    elif a < x and ((a-x) ** 2 + (b-y1) ** 2) <= (h/2) ** 2:
        cnt += 1
    elif a > x+w and ((a-x1) ** 2 + (b-y1) **2) <= (h/2) ** 2:
        cnt += 1

    print(cnt)

print(cnt)
