# 백준 3036번 링

# Typeerror 발생
from math import gcd

n = int(input())

rings = list(map(int, input().split()))

target = rings[0]

answer = []

for i in range(1, len(rings)):
    check = target % rings[i]
    if check == 0:
        answer.append(f'{target//rings[i]}/1')
    else:
        gcd = gcd(rings[i], target)
        answer.append(f'{target//gcd}/{rings[i]//gcd}')

for i in answer:
    print(i)

# 최대공약수 변수명을 바꾸어주니 해결
from math import gcd

n = int(input())

rings = list(map(int, input().split()))

target = rings[0]

answer = []

for i in range(1, len(rings)):
    check = target % rings[i]
    if check == 0:
        answer.append(f'{target//rings[i]}/1')
    else:
        result = gcd(rings[i], target)
        answer.append(f'{target//result}/{rings[i]//result}')

for i in answer:
    print(i)