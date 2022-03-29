# 백준 1010번 다리놓기
dp = [[1]*31 for _ in range(31)]

for i in range(31):
    dp[1][i] = i

for i in range(2,31):
    for j in range(i + 1, 31):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

n = int(input())

for i in range(n):
    a ,b = map(int, input().split())
    print(dp[a][b])
    # b = range(b)
    # c = list(combinations(b,a))
    # answer = len(b)
    # print(answer)

    # (b)! // (a)! * (b-a)!