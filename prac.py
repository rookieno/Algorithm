# import math

# print(math.lcm(3,5))

# a = []
# print(a[-1:])

# 한번에 받아왔다.
# msg1 = 'a b 2022-03-22 2022-03-22'
# cnt = 0
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




from tkinter import N


a = 1071

b = 1029

def gcd(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
print(gcd(a,b))
