def solution(n, lost, reserve):
    lost_students = set(lost)-set(reserve) # 중복제거 가져왔는데 도난당할경우
    reserve_students = set(reserve)-set(lost) # 중복제거 가져왔는데 도난당할경우
    for i in reserve_students:
        if i-1 in lost_students: # 탐욕법 왼쪽친구부터 주어야함 lost 2,4 reserve 3,5 오른쪽부터 줄시 2번이 못받는다.
            lost_students.remove(i-1)
        elif i+1 in lost_students:
            lost_students.remove(i+1)
    return n - len(lost_students)

n = 5
lost = [2, 3, 4]
reserve = [1, 3, 5]


print(solution(n, lost, reserve))