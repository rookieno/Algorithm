# 백준 1018번 체스판 다시 칠하기
n ,m = map(int, input().split())

chess = []

for i in range(n):
    line = str(input())
    chess.append(line)

check = 0

for idx,i in enumerate(chess):
    for j in range(m-2):
        if i[j] == i[j+1]:
            if i[j] == 'W':
                chess[idx][j+1] = 'B'
            else:
                chess[idx][j+1] = 'W'
            check += 1

print(check)