# 백준 2447번 별찍기 - 10
def star(n):
    if n == 1:
        return '*'
    line = star(n//3)
    answer = []
    
    for i in line:
        answer.append(i*3)
    for i in line:
        answer.append(i+' '*(n//3)+i)
    for i in line:
        answer.append(i*3)

    return answer

n = int(input())

print('\n'.join(star(n)))



