# def solution(progresses, speeds):
#     answer = []
#     days = 0
#     count = 0

#     while len(progresses) != 0:
#         if progresses[0] + days * speeds[0] > 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             days += 1
    
#     answer.append(count)

#     return answer

def solution(progresses, speeds):
    answer = []
    days = 0
    for i in range(len(progresses)):
        if progresses[i] + days * speeds[i] > 100:
            answer.append(days)
        else:
            days += 1
        
    return answer




a = [93, 30, 55]
b = [1, 30, 5]

c = [95, 90, 99, 99, 80, 99]
d = [1, 1, 1, 1, 1, 1]

print(solution(a,b))
print(solution(c,d))