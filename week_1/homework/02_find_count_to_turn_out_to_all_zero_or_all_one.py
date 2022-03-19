input = "011110"

# 전제조건
# 1. 문자열을 모두 같은 숫자로 만들어라 0으로 만들 때와 1로 만들 때를 비교하여 최소값을 구해라.
# 2. 같은 숫자가 연속으로 나오면 한번에 뒤집는다.
# + 모두 0으로 만들 때와 1로 만들 때의 값을 구한다.
# + 모두 같게 만드려면 0 -> 1 , 1 -> 0 으로 바뀌는 시점에서 뒤집는다
# + 제일 첫 번째 숫자도 고려해야한다 !
# + 0으로 만들 때와 1로 만들 때의 횟수를 비교해 최소값을 반환한다.

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                count_to_all_one += 1
            if string[i+1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)


