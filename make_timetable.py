import pandas as pd


def make_timetable(a_time: list, b_time: list, c_time: list, d_time: list):
    time = [10,11,12,13,14,15,16,17,18]
    days = ["월","화","수","목","금"]
    timetable = pd.DataFrame(index=days,columns=time)
    a_hour = hour_generater(a_time)
    b_hour = hour_generater(b_time)
    c_hour = hour_generater(c_time)
    d_hour = hour_generater(d_time)
    
    for i, day in enumerate(days):
        for time in time:
            a_hour[i]
        
    return timetable


def hour_generater(time_list: list):
    result = []
    # time.split(";")[0].split("~")[0].spilt(":")[0]
    for time in time_list:
        if ";" in time:
            start = int(time.split(";")[0].split("~")[0].split(":")[0])
            end = int(time.split(";")[0].split("~")[1].split(":")[0])
            next_start = int(time.split(";")[1].split("~")[0].split(":")[0])
            next_end = int(time.split(";")[1].split("~")[1].split(":")[0])
            is_workable = list(range(start, end+1)) + list(range(next_start, next_end+1))
        else:
            start = int(time.split("~")[0].split(":")[0])
            end = int(time.split("~")[1].split(":")[0])
            is_workable = list(range(start, end+1))
        result.append(is_workable)
    return result



a = ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
b = ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
c = ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
d = ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']

print(make_timetable(a_time=a, b_time=b, c_time=c, d_time=d))
print(hour_generater(a))