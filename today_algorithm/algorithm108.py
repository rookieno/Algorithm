# 백준 1764번 듣보잡

n, m = map(int, input().split())

people1 = []
people2 = []

for _ in range(n):
    people1.append(str(input()))

for _ in range(m):
    people2.append(str(input()))
    
answer = set(people1)&set(people2)

print(len(answer))

answer = sorted(answer)

for i in answer:
    print(i)