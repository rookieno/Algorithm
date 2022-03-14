def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    left_num = [1,4,7]
    center_num = [0,2,5,8]
    right_num = [3,6,9]

    for i in numbers:
        if i in left_num:
            left = i
            answer += 'L'
        elif i in right_num:
            right = i
            answer += 'R'
        elif i in center_num:
            if i == 0:
                i = 11
                left_distance = abs(i-left) // 3 + abs(i-left) % 3
                right_distance = abs(i-right) // 3 + abs(i-right) % 3

                if left_distance > right_distance:
                    right = i
                    answer += 'R'
                elif right_distance > left_distance:
                    left = i
                    answer += 'L'
                else:
                    if hand == 'right':
                        right = i
                        answer += 'R'
                    else:
                        left = i
                        answer += 'L'
            else:
            


a = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
b = 'right'

print(solution(a,b))

# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #