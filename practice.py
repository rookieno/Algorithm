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
# def solution(grid):
    # answer = 0
    # ?있으면 개수를 세고 넣을 수 있는 경우의수를 다 적용. 그중에 상하좌우 조건을 만족하는지 검사 만족하는 횟수 출력 가장 좋은 조건만 고르자.
    # 양쪽, 다음행의 같은 인덱스의 값이 같아야함.
    # 가장 좋은조건? = 상하좌우를 확인하고 ?가 있는지 검사 ?가 아닌쪽 문자를 입력
    

    # return answer

# a = ["??b", "abc", "cc?"]
# print(solution(a))


# def solution(dist):
#     answer = [[]]
#     n = len(dist)
#     for i in dist:
        
#     return answer

# a = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
# # [[1,2,0,4,3],[3,4,0,2,1]]
# print(solution(a))

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# num = int(input())

# print(factorial(num))

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n <= 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# num = int(input())

# print(fibo(num))

# def star(n):
#     answer = ''
#     if n <= 3:
#         return '***\n* *\n***'
#     answer += '***\n* *\n***'
#     return star(n/3)

# print(star(27))


# import re

# memo = input()
# memo2 = input()
# memo3 = input()

# dict = {}

# dict['memo'] = memo
# dict['memo2'] = memo2
# dict['memo3'] = memo3

# memo_day = re.findall('\d+',memo)
# memo2_day = re.findall('\d+',memo2)
# memo3_day = re.findall('\d+',memo3)

# # print(memo_day)
# # print(memo2_day)
# # print(memo3_day)

# for i in range(3):
# 	if len(memo_day[0]) == 4:
# 		memo_day[0] = memo_day[0][2:]
# 	elif len(memo2_day[0]) == 4:
# 		memo2_day[0] = memo2_day[0][2:]
# 	elif len(memo3_day[0]) == 4:
# 		memo3_day[0] = memo3_day[0][2:]
		
# print(memo_day)
# print(memo2_day)
# print(memo3_day)
		
# result = {}

# result['memo'] = memo_day
# result['memo2'] = memo2_day
# result['memo3'] = memo3_day

# # print(result)

# sorted_result = sorted(result, key=lambda x: result[x])

# # print(sorted_result)

# for i in sorted_result:
# 	print(dict[i])



# def recur(list):
# 	check = len(list)
# 	if check == 1:
# 		return print(list[0], end=' ')
# 	elif check % 2 == 0:
# 		list.reverse()
# 		recur(list[:check//2])
# 		recur(list[check//2:])
# 	else:
# 		list.reverse()
# 		recur(list[:check//2+1])
# 		recur(list[check//2+1:])
 
# a = [1,2,3,4,5,6]

# recur(a)

# def solution(n, k):
# 	num = 2**n
# 	bin_list = []
# 	answer = 0
# 	for i in range(num):
# 		target = format(i, 'b').rjust(n, '0')
# 		if target.count('1') == k:
# 			if i % 3 == 0:
# 				answer += 1

# 	# for i in bin_list:
# 	# 	if i.count('1') == k:
# 	# 		target = int(i, 2)
# 	# 		if target % 3 == 0:
# 	# 			answer += 1
# 	return answer

# print(solution(3,2))


	
# 1번
# 배열 numbers가 있습니다. numbers의 특정 구간의 숫자를 모두 합하는 작업을 반복하려고 합니다.
# 작업은 배열 start와 finish에 명시되어 있습니다. 예를들어

# number가 [100, 101, 102, 103, 104]
# start가 [1, 2]
# finish가 [2, 4]
# 라면

# 첫 번째 작업은 start[0]부터 finish[0] 구간의 숫자를 모두 더하는겁니다. start[0]은 1이고 finish[0]은 2 이므로 numbers의 1~2사이의 숫자를 모두 더하면 101 + 102 = 203이 됩니다.
# 두 번째 작업은 start[1]부터 finish[1] 구간의 숫자를 모두 더하는 작업이므로 numbers의 2~4 사이의 숫자를 모두 더하면 102 + 103 + 104 = 309가 됩니다.
# 이렇게 수행한 작업의 결과를 순서대로 넣은 배열을 return 하도록 함수 solution을 완성하세요.
# 위의 예제 대로라면 [203, 309]를 반환하면 됩니다.

# 제한사항
# numbers의 길이 N : N은 100,000 이하의 자연수입니다.
# numbers의 원소의 값: 10,000 이하의 자연수입니다.
# 작업의 개수(start와 finish 배열의 길이) 는 100,000 이하입니다.
# start와 finish 배열의 길이는 항상 같습니다.
# k번째 작업 start[k]와 finish[k]에 대해서 0 ≤ start[k] ≤ finish[k] < N 입니다.
# 딕셔너리로하니까 닶이 안맞음 뭐냐 튜플로하니까 또 정답임 버근가
# 큐로 구현하니 테스트는 통과하나 효율성에서 개박살
# 시간으로 보았을때 딕셔너리나 튜플로하는건데.. 어디서 더 줄여야핧지 모르겠음




n = [100,101,102,103,104]
result = {0:[1,2], 1:[2,4],2:[2,3]}
answer = []

for i in range(3):
	target = sum(n[result[i][0]:result[i][1]+1])
	answer.append(target)

print(answer)

