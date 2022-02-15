def solution(phone_book):
    phone_book.sort()
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True



a = ["119", "97674223", "1195524421"]
b = ["123","456","789"]
c = ["12","123","1235","567","88"]
print(solution(a))
print(solution(b))
print(solution(c))

# print(a[0])
# print(a[1].find(a[0]))