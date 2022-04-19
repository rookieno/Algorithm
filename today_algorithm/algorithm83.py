# 백준 1002번 터렛
# 원을그려 접점을 찾는다. 운의 방정식
# 공식 다 까먹음

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    r = (((x1-x2)**2) + ((y1-y2)**2))**0.5
    if r == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) < r < r1+r2:
        print(2)
    elif r1+r2 == r or abs(r1-r2) == r:
        print(1)
    else:
        print(0)

    