s = input()

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croa:
    s = s.replace(i, 'a') # 같은변수를 주어야함

print(len(s))

# replace함수는 함수를 사용한 문자열 원형을 변형시키지 않는 비파괴적 함수이기 때문이다.


