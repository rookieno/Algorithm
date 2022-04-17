# 백준 9020번 골드바흐의 추측

# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다! 골드하흐 수
# 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.

# # 시간초과
# import sys

# input = sys.stdin.readline

# t = int(input())

# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# for i in range(t):
#     n = int(input())
#     prime_list = []
#     for j in range(2, n+1):
#         if is_prime(j) == True:
#             prime_list.append(j)
#     answer = []
#     for k in prime_list:
#         for idx in range(len(prime_list)):
#             result = prime_list[idx] + k
#             if result == n:
#                 answer.append((prime_list[idx],k))
#     idx = []
#     for a,b in answer:
#         idx.append(abs(a-b))
#     target = idx.index(min(idx))
#     sort_answer = sorted(answer[target])
#     print(sort_answer[0], sort_answer[1])


# 시간초과 해결 최적화
import sys

input = sys.stdin.readline

t = int(input())

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(t):
    n = int(input())
    result = []
    for i in range(n//2,1,-1):
        if is_prime(i) and is_prime(n-i):
            print(i,n-i)
            break



