# 백준 10816번 숫자카드2

n = int(input())

n_list = list(map(int, input().split()))

m = int(input())

m_list = list(map(int, input().split()))

answer = {}

for i in n_list:
    if i in answer:
        answer[i] += 1
    else:
        answer[i] = 1

for i in m_list:
    if i in answer:
        print(answer[i], end=' ')
    else:
        print(0, end=' ')