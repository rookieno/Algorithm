input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    s = array[0]
    for i in array:
        if s < i:
            s = i
    return s


result = find_max_num(input)
print(result)