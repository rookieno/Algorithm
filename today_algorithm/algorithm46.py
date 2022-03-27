# 프로그래머스 두개 뽑아서 더하기
def solution(numbers):
    answer = []
    while numbers:
        a = numbers.pop()
        for i in numbers:
            answer.append(a+i)
    return sorted(list(set(answer)))

a = [2,1,3,4,1]
print(solution(a))