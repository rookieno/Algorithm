def solution(n, lost, reserve):
    lost_students = set(lost)-set(reserve)
    reserve_students = set(reserve)-set(lost)
    for i in reserve_students:
        if i-1 in lost_students:
            lost_students.remove(i-1)
        elif i+1 in lost_students:
            lost_students.remove(i+1)
    return n - len(lost_students)

n = 5
lost = [2, 3, 4]
reserve = [1, 3, 5]


print(solution(n, lost, reserve))