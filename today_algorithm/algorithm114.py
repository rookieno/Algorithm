# 백준 2004번 조합 0의 개수

# 메모리초과 20억까지임
n, m = map(int, input().split())

top = set(range(1, n+1)) - set(range(1, m+1))

bot = range(1, n-m+1)

a = 1
b = 1

for i in top:
    a *= i

for i in bot:
    b *= i

result = str(a//b)

answer = 0

for i in result[::-1]:
    if i == '0':
        answer += 1
    else:
        break

print(answer)

# 카운팅 2, 5
def count_num(a, b):
    cnt = 0
    while a != 0:
        a //= b
        cnt += a
    return cnt

n, m = map(int, input().split())

five_cnt = count_num(n, 5) - count_num(m, 5) - count_num(n-m, 5)
two_cnt = count_num(n, 2) - count_num(m, 2) - count_num(n-m, 2)

print(min(five_cnt, two_cnt))