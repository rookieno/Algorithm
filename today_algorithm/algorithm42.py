# 프로그래머스 부족한 금액 계산하기
def solution(price, money, count):
    answer = 0
    all_price = 0
    for i in range(1, count+1):
        all_price += price * i

    if money > all_price:
        answer = 0
    else:
        answer = all_price - money
    return answer


a = 3
b = 20
c = 4

print(solution(a,b,c))