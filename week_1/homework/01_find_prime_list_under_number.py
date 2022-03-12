input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for i in range(2, number + 1):
        for n in prime_list:
            if i % n == 0 and n * n <= i:
                break
        else:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)

