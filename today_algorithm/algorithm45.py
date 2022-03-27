# 프로그래머스 2016년
from datetime import date

def solution(a, b):
    days =['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = days[date(2016,a,b).weekday()]
    return answer

month = 5
day = 24
print(solution(month,day))