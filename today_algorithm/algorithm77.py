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
# 72 36 18 9 3 1
# if n != 1:
#     for i in range(2,n):
#         if n % i == 0:
#             n = n // i
#             answer.append(i)
            
solution(n)
print(answer)