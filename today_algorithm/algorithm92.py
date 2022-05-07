# 백준 1427번 소트인사이드
num = list(map(int, input()))

sorted_num = sorted(num, reverse=True)

answer = int(''.join(map(str,sorted_num)))

print(answer)

