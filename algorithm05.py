def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))
# str sort 첫번째 인덱스 값 비교 후 같으면 다음 인덱스값을 비교함!!
