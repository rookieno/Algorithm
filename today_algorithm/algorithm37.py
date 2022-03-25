# 백준 11729번 하노이 탑 이동 순서
k = int(input())


def hanoi(k, a, b, c):
    if k == 1:
        print(a,c)
    else:
        hanoi(k-1, a, c, b)
        print(a,c)
        hanoi(k-1, b, a, c)

print(2**k-1)
hanoi(k, 1, 2, 3)



# 3       4
# 2 0 1   2 1 0
# 3 2 1   3 1 2
# 3 1 0   3 0 1
# 0 1 3   4 3 1
# 1 2 3   1 3 2
# 1 0 2   1 2 0
# 0 0 1   4 1 0
#         5 1 4
#         5 2 1
#         2 3 1
#         1 3 4
        
