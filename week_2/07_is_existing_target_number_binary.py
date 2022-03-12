finding_target = 0
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    num_min = 0
    num_max = len(numbers) - 1
    num_find = (num_min + num_max) // 2
    while num_min <= num_max:
        if target == num_find:
            return True
        elif num_find < target:
            num_min = num_find + 1
        else:
            num_max = num_find - 1
        num_find = (num_min + num_max) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)