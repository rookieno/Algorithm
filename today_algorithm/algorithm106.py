# 백준 1620번 나는야 포켓몬 마스터 이다솜
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon = {}

for i in range(1, n+1):
    a = input()
    pokemon[i] = a
    pokemon[a] = i

for _ in range(m):
    target = input()

    if target.isdigit():
        print(pokemon[int(target)])
    
    else:
        print(pokemon[target])