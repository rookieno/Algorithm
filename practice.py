# # 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때,
# # 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# #
# # 입력
# # 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# #
# # 출력
# # 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# # a = int(input())

# # def arithmetic_sequence(x):
# #     num_list = []
# #     for i in range(1, x + 1):
# #         if i < 100:
# #             num_list.append(i)
# #         elif (i // 100) - (i // 10 % 10) == (i // 10 % 10) - (i % 10):
# #             num_list.append(i)
# #         elif i == 1000:
# #             break

# #     return len(num_list)

# # print(arithmetic_sequence(a))

# # n = int(input())

# # for _ in range(n):
# #         point = list(map(int, input().split()))
# #         avg = sum(point[1:])/point[0]

# #         cnt = 0
# #         for i in point[1:]:
# #             if i > avg:
# #                 cnt += 1
        
# #         per = (cnt/point[0]) * 100
# #         print(f'{per:.3f}%')


# # a b c
# # def solution(grid):
#     # answer = 0
#     # ?있으면 개수를 세고 넣을 수 있는 경우의수를 다 적용. 그중에 상하좌우 조건을 만족하는지 검사 만족하는 횟수 출력 가장 좋은 조건만 고르자.
#     # 양쪽, 다음행의 같은 인덱스의 값이 같아야함.
#     # 가장 좋은조건? = 상하좌우를 확인하고 ?가 있는지 검사 ?가 아닌쪽 문자를 입력
    

#     # return answer

# # a = ["??b", "abc", "cc?"]
# # print(solution(a))


# # def solution(dist):
# #     answer = [[]]
# #     n = len(dist)
# #     for i in dist:
        
# #     return answer

# # a = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
# # # [[1,2,0,4,3],[3,4,0,2,1]]
# # print(solution(a))

# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     return n * factorial(n-1)

# # num = int(input())

# # print(factorial(num))

# # def fibo(n):
# #     if n == 0:
# #         return 0
# #     elif n <= 2:
# #         return 1
# #     return fibo(n-1) + fibo(n-2)

# # num = int(input())

# # print(fibo(num))

# # def star(n):
# #     answer = ''
# #     if n <= 3:
# #         return '***\n* *\n***'
# #     answer += '***\n* *\n***'
# #     return star(n/3)

# # print(star(27))


# # import re

# # memo = input()
# # memo2 = input()
# # memo3 = input()

# # dict = {}

# # dict['memo'] = memo
# # dict['memo2'] = memo2
# # dict['memo3'] = memo3

# # memo_day = re.findall('\d+',memo)
# # memo2_day = re.findall('\d+',memo2)
# # memo3_day = re.findall('\d+',memo3)

# # # print(memo_day)
# # # print(memo2_day)
# # # print(memo3_day)

# # for i in range(3):
# # 	if len(memo_day[0]) == 4:
# # 		memo_day[0] = memo_day[0][2:]
# # 	elif len(memo2_day[0]) == 4:
# # 		memo2_day[0] = memo2_day[0][2:]
# # 	elif len(memo3_day[0]) == 4:
# # 		memo3_day[0] = memo3_day[0][2:]
		
# # print(memo_day)
# # print(memo2_day)
# # print(memo3_day)
		
# # result = {}

# # result['memo'] = memo_day
# # result['memo2'] = memo2_day
# # result['memo3'] = memo3_day

# # # print(result)

# # sorted_result = sorted(result, key=lambda x: result[x])

# # # print(sorted_result)

# # for i in sorted_result:
# # 	print(dict[i])



# # def recur(list):
# # 	check = len(list)
# # 	if check == 1:
# # 		return print(list[0], end=' ')
# # 	elif check % 2 == 0:
# # 		list.reverse()
# # 		recur(list[:check//2])
# # 		recur(list[check//2:])
# # 	else:
# # 		list.reverse()
# # 		recur(list[:check//2+1])
# # 		recur(list[check//2+1:])
 
# # a = [1,2,3,4,5,6]

# # recur(a)

# # def solution(n, k):
# # 	num = 2**n
# # 	bin_list = []
# # 	answer = 0
# # 	for i in range(num):
# # 		target = format(i, 'b').rjust(n, '0')
# # 		if target.count('1') == k:
# # 			if i % 3 == 0:
# # 				answer += 1

# # 	# for i in bin_list:
# # 	# 	if i.count('1') == k:
# # 	# 		target = int(i, 2)
# # 	# 		if target % 3 == 0:
# # 	# 			answer += 1
# # 	return answer

# # print(solution(3,2))


# # 매드업 코테

# # 1번
# # 배열 numbers가 있습니다. numbers의 특정 구간의 숫자를 모두 합하는 작업을 반복하려고 합니다.
# # 작업은 배열 start와 finish에 명시되어 있습니다. 예를들어

# # number가 [100, 101, 102, 103, 104]
# # start가 [1, 2]
# # finish가 [2, 4]
# # 라면

# # 첫 번째 작업은 start[0]부터 finish[0] 구간의 숫자를 모두 더하는겁니다. start[0]은 1이고 finish[0]은 2 이므로 numbers의 1~2사이의 숫자를 모두 더하면 101 + 102 = 203이 됩니다.
# # 두 번째 작업은 start[1]부터 finish[1] 구간의 숫자를 모두 더하는 작업이므로 numbers의 2~4 사이의 숫자를 모두 더하면 102 + 103 + 104 = 309가 됩니다.
# # 이렇게 수행한 작업의 결과를 순서대로 넣은 배열을 return 하도록 함수 solution을 완성하세요.
# # 위의 예제 대로라면 [203, 309]를 반환하면 됩니다.

# # 제한사항
# # numbers의 길이 N : N은 100,000 이하의 자연수입니다.
# # numbers의 원소의 값: 10,000 이하의 자연수입니다.
# # 작업의 개수(start와 finish 배열의 길이) 는 100,000 이하입니다.
# # start와 finish 배열의 길이는 항상 같습니다.
# # k번째 작업 start[k]와 finish[k]에 대해서 0 ≤ start[k] ≤ finish[k] < N 입니다.

# # 딕셔너리, 튜플로 먼저해봄 시간초과
# # 큐로 구현하니 테스트는 통과하나 효율성에서 개박살
# # 시간으로 보았을때 딕셔너리나 튜플로하는건데.. 어디서 더 줄여야할지 모르겠음



# # 2번
# # 문제 설명
# # 다이어트를 하기 위해 식단을 조절하려 합니다. 다이어트 원칙은 다음과 같습니다.

# # 연속해서 3끼를 굶어서는 안 된다.
# # 다이어트 기간에는 칼로리를 최소한으로 섭취해야 한다.
# # 기숙사는 정해진 식단표에 따라 아침, 점심, 저녁을 줍니다. 식단표에는 칼로리가 적혀 있습니다.

# # 예를 들어서 7일 동안 다이어트를 하고, 식단표에 적힌 칼로리는 다음과 같다고 하겠습니다.

# # ▼ 7일간 식단표 예. (단위: ㎉)

# # 아침	점심	저녁
# # 1일	360	138	338
# # 2일	230	102	311
# # 3일	320	474	214
# # 4일	131	498	484
# # 5일	366	176	249
# # 6일	323	407	116
# # 7일	265	433	317
# # 이때 다이어트 원칙을 지키려면 다음과 같이 먹어야 합니다.

# # 1일차: 점심(138)
# # 2일차: 점심(102)
# # 3일차: 아침(320)
# # 4일차: 아침(131)
# # 5일차: 아침(366)
# # 6일차: 아침(323)
# # 7일차: 아침(265)
# # 위와 같이 먹으면 총 1,645㎉를 섭취하게 되며, 더 적은 칼로리를 섭취할 수 있는 방법은 없습니다.

# # 다이어트 기간 동안의 식단 diet가 매개변수로 주어질 때, 다이어트 기간에 섭취하게 되는 최소 칼로리 return 하도록 solution 함수를 완성해주세요.

# # 제한 사항
# # diet의 세로(행) 길이는 다이어트 기간을 나타내며, 3 이상 1,000 이하입니다.
# # diet의 가로(열) 길이는 3입니다.
# # diet의 각 행은 [아침, 점심, 저녁] 식단의 칼로리를 나타냅니다.
# # 식단의 칼로리는 1일 차부터 다이어트 기간만큼 순서대로 주어집니다.
# # 각 식단의 칼로리(단위:㎉)는 100 이상 1,000 이하인 자연수입니다.

# # 1번에서 너무 시간 끌어서 2번풀다 끝남
# # 1일차부터 인덱스를 이용해 3끼 이상 굶지않게 구현해서 예시 테스트는 통과했으나 정답에서 다 터짐
# # 생각해보니 첫날 아침, 점심, 저녁 3가지 경우를 모두 구한 후 최솟값을 구해야겠다라고 떠올리고 풀다가 시간끝남


# # 3번
# # 문제 설명
# # r x r 크기 정사각 격자 형태로 된 마을에서 배달원이 물건을 배달하려 합니다. 각 칸은 1 x 1 크기 정사각형이며, 좌측 상단 칸의 좌표는 (0, 0), 우측 하단 칸의 좌표는 (r - 1, r - 1)입니다. 배달원은 처음에 (0, 0) 칸에 있으며, 상, 하, 좌, 우 방향으로 한 칸씩 이동할 수 있습니다. 시각은 0초부터 시작하며, 한 칸 이동하는 데 1초가 걸립니다.

# # 모든 격자 칸에는 물건을 배달해야 하는 집들이 있는데, 각 집마다 물건을 배달할 수 있는 제한 시간이 정해져 있습니다. 만약, 제한 시간 안에 물건을 배달한다면 각 격자 칸마다 정해진 배달 팁을 받을 수 있습니다. 반드시 모든 집에 물건을 배달할 필요는 없지만, 제한시간 안에 물건을 배달하지 못한 집에서는 배달 팁을 받을 수 없습니다. 한 번 지나간 칸을 다시 지나가는 것은 가능하나, 이 경우 제한 시간이 지났거나 이미 배달 팁을 받았다면 다시 배달 팁을 받지는 못합니다. 또, 제한시간이 끝나는 시각과 동시에 배달원이 도착했다면 배달에 성공했다고 가정합니다.

# # 다음은 크기가 3 x 3인 마을의 예시입니다. 괄호 안의 숫자는 (배달 제한 시간, 배달 팁) 순입니다.

# # 예를 들어 위 마을에서 배달원이 화살표와 같이 이동하면서 물건을 배달했다면 다음과 같이 15원의 배달 팁을 받을 수 있습니다.

# # 시각(초)	배달원 위치	설명
# # 0	(0, 0)	출발 위치에 있는 집에 바로 배달하고 배달 팁 5원을 받습니다.
# # 1	(1, 0)	2초 이전에 도달했으므로 배달 팁 3원을 받습니다.
# # 2	(1, 1)	3초 이전에 도달했으므로 배달 팁 1원을 받습니다.
# # 3	(2, 1)	5초 이전에 도달했으므로 배달 팁 2원을 받습니다.
# # 4	(2, 2)	4초에 정확히 도달했으므로 배달 팁 1원을 받습니다.
# # 5	(1, 2)	3초를 넘어서 도달했으므로 배달 팁을 받을 수 없습니다.
# # 6	(0, 2)	4초를 넘어서 도달했으므로 배달 팁을 받을 수 없습니다.
# # 7	(0, 1)	8초 이전에 도달했으므로 배달 팁 3원을 받습니다.
# # 그러나 아래 그림의 화살표와 같이 배달원이 이동하면서 물건을 배달했다면 17원의 배달 팁을 받을 수 있고, 이때가 최대로 받을 수 있는 배달 팁입니다.

# # 마을의 크기 r, 각 집의 정해진 배달 시간과 배달 팁이 담긴 2차원 배열 delivery가 매개변수로 주어질 때, 배달원이 최대로 받을 수 있는 배달 팁은 얼마인지 return 하도록 solution 함수를 완성해주세요.

# # 제한사항
# # r은 2 이상 4 이하인 자연수입니다.
# # delivery는 세로(행) 길이가 r x r, 가로길이가 2인 2차원 배열입니다.
# # delivery의 각 행은 각 격자 칸의 [배달 제한 시간, 배달 팁]을 나타냅니다.
# # i행 j열 칸에 대한 정보는 delivery[i*r + j] 위치에 담겨있습니다.
# # 즉, 길이 r 단위마다 각 행을 나타냅니다.
# # 예를 들어 입출력 예 1번의 경우 2행 1열에 해당하는 데이터는 delivery[2 * 3 + 1] = delivery[7]에 있으며, 이 값은 [제한시간 5초, 배달 팁 2원]을 나타냅니다.
# # 배달 제한 시간은 1 이상 16 이하인 자연수입니다.
# # 배달 팁은 1 이상 100 이하인 자연수입니다.


# # n = [100,101,102,103,104]
# # result = {0:[1,2], 1:[2,4],2:[2,3]}
# # answer = []

# # for i in range(3):
# # 	target = sum(n[result[i][0]:result[i][1]+1])
# # 	answer.append(target)

# # print(answer)

# # for i in range(1, 11):
# #     num = int(input())
# #     apart = list(map(int, input().split()))

# #     for j in range(2, num-2):
# #         check = apart[i+2],

# target = list(range(5, 128))

# result = {}

# for i in target:
#     temp = str(format(i, 'b')).count('1')
#     result[i] = temp

# result = sorted(result.items(), key=lambda x:x[1], reverse=True)

# print(result)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def change_name(self):


bae = Person(name="배", age=29)
print(bae.name)