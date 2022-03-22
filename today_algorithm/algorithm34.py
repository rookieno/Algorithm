# 백준 4938번 베르트랑 공준
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     last = n*2
#     a = set(range(n+1, last+1))

#     for i in range(2, last+1):
#         a -= set(range(i*2, last+1, i))
#         # print(f'빼기:{set(range(i*2, last+1, i))}')
#         # print(f'결과:{a}')
#     print(len(a))

a = set(range(2,123456*2))

for i in range(2, 123456*2):
    a -= set(range(i*2, 123456*2, i))

a = list(a)

while True:
    n = int(input())
    answer = 0
    if n == 0:
        break
    for num in a:
        if n < num <= n*2:
            answer += 1
    print(answer)
    