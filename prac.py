# import math

# print(math.lcm(3,5))

# a = []
# print(a[-1:])

# 한번에 받아왔다.
# msg1 = 'a b 2022-03-22 2022-03-22'
# msg1 = (msg1.split(' '))
# print(msg1)
# for i,j in enumerate(msg1):
#     if j.isalnum():
#         title = msg1[:i+1]
        # back = msg1[i+1:]

# 백준 1929번 소수구하기
# m, n = map(int,input().split())

# if m == 1:
#     a = set(range(2, n+1))
# else:
#     a = set(range(m, n+1))

# for i in range(2, n+1):
#     a -= set(range(i*2, n+1, i))

# a = list(a)
# a.sort()
# for i in a:
#     print(i)

# 백준 2609번 최대공약수와 최소공배수
# import math

# a ,b = map(int,input().split())

# gcd = math.gcd(a,b)

# lcm = a*b//gcd

# print(gcd)
# print(lcm)


# 유클리드 호재법
# a = 1071

# b = 1029

# def gcd(a,b):
#     if a < b:
#         a, b = b, a
#     if b == 0:
#         return a
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a%b)
# print(gcd(a,b))

# print(1029%42)

# a = [5,4,3,2,1]

# a.sort() # a 리스트 그 자체를 정렬해줌

# b = sorted(a) # a 리스트 원래 값은 변경하지않고 새롭게 정렬한 리스트를 만듬, 리스트형태가 아니라 모든 iterable이면 사용가능

# print(a)

# 백준 10828 스택
# import sys

# n = int(input())

# stack = []

# for i in range(n):
#         order = sys.stdin.readline().split()

#         if order[0] == 'push':
#                 stack.append(int(order[1]))
        
#         if order[0] == 'pop':
#                 if len(stack) != 0:
#                         print(stack.pop())
                        
#                 else:
#                         print(-1)
#         if order[0] == 'size':
#                 print(len(stack))
        
#         if order[0] == 'empty':
#                 if len(stack) == 0:
#                         print(1)
#                 else:
#                         print(0)
#         if order[0] == 'top':
#                 if len(stack) != 0:
#                         print(stack[-1])
#                 else:
#                         print(-1)

# def solution(grid):
#     answer = 0
#     for i in grid:
#         for j in i:

#     return answer


# a = ["??b", "abc", "cc?"]

# print(solution(a))

# # 재귀동닥 예시
# def recur(n):
#     if n < 1:
#         return 0
#     return recur(n-1) + n

# # recur(3) 실행했을때

# # recur(3)실행 원본으로부터 복사본을 가져옴 
# def recur(3): # n == 3
#     if 3 < 1:
#         return 0
#     return recur(3-1) + 3 # n이 1보다 작지 않으므로 recur(2) 실행

# # recur(2) 실행 원본으로부터 복서본 가져옴
# def recur(2): # n == 2
#     if 2 < 1:
#         return 0
#     return recur(2-1) + 2 # n이 1보다 작지 않으므로 recur(1) 실행

# # recur(1) 실행 원본으로부터 복사본을 가져옴 
# def recur(1): # n == 1
#     if 1 < 1:
#         return 0
#     return recur(1-1) + 1 # n이 1보다 작지 않으므로 recur(0) 실행

# # recur(0) 실행 원본으로부터 복사본을 가져옴
# def recur(1): # n == 0
#     if 1 < 1: # n이 1보다 작으므로 0을 반환 함수좀료 스택에서 사라짐
#         return 0
#     return recur(0-1) + 0

# # 이제 호출 했던 곳으로 반환하고 스택에서 사라지는 단계를 반복 결과적으로 recur(3) == 6

t = int(input())

for _ in range(t):
    a = int(input())
    print(a ** 0.5)