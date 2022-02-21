# 1 1
# 2 7 + 6 6*1
# 3 19 + 12 6*2
# 4 37 + 18 6*3
# 5 61 + 24 6*4

n = int(input())
max_bee = 1
i = 0
while True:
    max_bee = max_bee + 6 * i
    i += 1
    if max_bee >= n:
        print(i)
        break
