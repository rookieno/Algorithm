# 백준 1764번 듣보잡

n, m = map(int, input().split())

people1 = []
people2 = []

for i in range(1, n+m+1):
    if i < n+2:
        people1.append(str(input()))
    else:
        people2.append(str(input()))

answer = set(people1)&set(people2)

print(len(answer))

answer = sorted(answer)

for i in answer:
    print(i)