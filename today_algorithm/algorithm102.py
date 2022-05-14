# 백준 1004번 어린왕자

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        start = (((x1-cx) ** 2) + ((y1-cy) ** 2)) ** 0.5
        goal = (((x2-cx) ** 2) + ((y2-cy) ** 2)) ** 0.5

        if start < r and goal < r:
            pass
        elif start < r:
            cnt += 1
        elif goal < r:
            cnt += 1

    print(cnt)