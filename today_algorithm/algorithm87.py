# 백준 1018번 체스판 다시 칠하기
n ,m = map(int, input().split())

chess = []

for i in range(n):
    line = list(str(input()))
    chess.append(line)

check = 0
