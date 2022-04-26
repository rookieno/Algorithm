# 백준 1018번 체스판 다시 칠하기
n ,m = map(int, input().split())

chess = []

for i in range(n):
    line = list(str(input()))
    chess.append(line[:8])

check = 0

for idx,i in enumerate(chess):
    for j in range(7):
        if i[j] == i[j+1]:
            if i[j] == 'W':
                chess[idx][j+1] = 'B'
            else:
                chess[idx][j+1] = 'W'
            check += 1

# for i in chess:
    

print(check)