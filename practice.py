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

n = int(input())

for _ in range(n):
        point = list(map(int, input().split()))
        avg = sum(point[1:])/point[0]

        cnt = 0
        for i in point[1:]:
            if i > avg:
                cnt += 1
        
        per = (cnt/point[0]) * 100
        print('%.3f' %per + '%')