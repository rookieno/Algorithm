# 백준 11653번 소인수분해

n = int(input())

answer = []

def solution(n):
    if n == 1:
        return
    for i in range(2, n+1):
        if n % i == 0:
            answer.append(i)
            result = n // i
            return solution(result)

solution(n)
for i in answer:
    print(i)