# 백준 2775번 부녀회장이 될테야
t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

result = 0

for i in range(1, n):
    result += sum(list(range(1, i+1)))

    print(result)

# k층 n호 
# 3층 1 5 15 35
# 41020
# 2츨 1 4 10 20
# 361015
# 1츨 1 3 6 10 15
# 2345
# 0층 1 2 3 4 5 6 7 8 
# 1234