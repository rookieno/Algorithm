# 프로그래머스 최소직사각형
def solution(sizes):
    for i in sizes:
        if i[0] < i[1]:
            i[0],i[1] = i[1],i[0]
    
    width = sorted(sizes, key=lambda x:x[0], reverse=True)[0][0]
    height = sorted(sizes, key=lambda x:x[1], reverse=True)[0][1]
    
    answer = width * height

    return answer

a = [[60, 50], [30, 70], [60, 30], [80, 40]]

print(solution(a))