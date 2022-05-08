# 백준 1018번 체스판 다시 칠하기
n ,m = map(int, input().split())

chess = []

for i in range(n):
    line = input()
    chess.append(line)

check = []

for y in range(n-7):
    for x in range(m-7):
        W = 0
        B = 0
        for i in range(y, y+8):
            for j in range(x, x+8):
                if (i+j) % 2 == 0:  # 합이 짝수가되는 좌표가 처음시작 값과 같아야함 W로 시작할 때 or B로 시작할 때
                    if chess[i][j] == 'W':
                        B += 1
                    else:
                        W += 1
                else:
                    if chess[i][j] == 'W':
                        W += 1
                    else:
                        B += 1
        check.append(min(W,B))
    
print(min(check))