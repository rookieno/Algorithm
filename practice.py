# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때,
# 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#
# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# a = int(input())

# def arithmetic_sequence(x):
#     num_list = []
#     for i in range(1, x + 1):
#         if i < 100:
#             num_list.append(i)
#         elif (i // 100) - (i // 10 % 10) == (i // 10 % 10) - (i % 10):
#             num_list.append(i)
#         elif i == 1000:
#             break

#     return len(num_list)

# print(arithmetic_sequence(a))

# n = int(input())

# for _ in range(n):
#         point = list(map(int, input().split()))
#         avg = sum(point[1:])/point[0]

#         cnt = 0
#         for i in point[1:]:
#             if i > avg:
#                 cnt += 1
        
#         per = (cnt/point[0]) * 100
#         print(f'{per:.3f}%')


# a b c
def solution(grid):
    answer = 0
    # ?있으면 개수를 세고 넣을 수 있는 경우의수를 다 적용. 그중에 상하좌우 조건을 만족하는지 검사 만족하는 횟수 출력 가장 좋은 조건만 고르자.
    # 양쪽, 다음행의 같은 인덱스의 값이 같아야함.
    # 가장 좋은조건? = 상하좌우를 확인하고 ?가 있는지 검사 ?가 아닌쪽 문자를 입력

    result = []
    for i in grid:
        row = []
        for j in i:
            row.append(j)
        result.append(row)
    print(result)
    return answer
a = ["??b", "abc", "cc?"]
print(solution(a))


# def solution(dist):
#     answer = [[]]
#     n = len(dist)
#     for i in dist:
        
#     return answer

# a = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
# # [[1,2,0,4,3],[3,4,0,2,1]]
# print(solution(a))