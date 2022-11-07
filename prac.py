# import math

# print(math.lcm(3,5))

# a = []
# print(a[-1:])

# 한번에 받아왔다.
# msg1 = 'a b 2022-03-22 2022-03-22'
# msg1 = (msg1.split(' '))
# print(msg1)
# for i,j in enumerate(msg1):
#     if j.isalnum():
#         title = msg1[:i+1]
        # back = msg1[i+1:]

# 백준 1929번 소수구하기
# m, n = map(int,input().split())

# if m == 1:
#     a = set(range(2, n+1))
# else:
#     a = set(range(m, n+1))

# for i in range(2, n+1):
#     a -= set(range(i*2, n+1, i))

# a = list(a)
# a.sort()
# for i in a:
#     print(i)

# 백준 2609번 최대공약수와 최소공배수
# import math

# a ,b = map(int,input().split())

# gcd = math.gcd(a,b)

# lcm = a*b//gcd

# print(gcd)
# print(lcm)


# 유클리드 호재법
# a = 1071

# b = 1029

# def gcd(a,b):
#     if a < b:
#         a, b = b, a
#     if b == 0:
#         return a
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a%b)
# print(gcd(a,b))

# print(1029%42)

# a = [5,4,3,2,1]

# a.sort() # a 리스트 그 자체를 정렬해줌

# b = sorted(a) # a 리스트 원래 값은 변경하지않고 새롭게 정렬한 리스트를 만듬, 리스트형태가 아니라 모든 iterable이면 사용가능

# print(a)

# 백준 10828 스택
# import sys

# n = int(input())

# stack = []

# for i in range(n):
#         order = sys.stdin.readline().split()

#         if order[0] == 'push':
#                 stack.append(int(order[1]))
        
#         if order[0] == 'pop':
#                 if len(stack) != 0:
#                         print(stack.pop())
                        
#                 else:
#                         print(-1)
#         if order[0] == 'size':
#                 print(len(stack))
        
#         if order[0] == 'empty':
#                 if len(stack) == 0:
#                         print(1)
#                 else:
#                         print(0)
#         if order[0] == 'top':
#                 if len(stack) != 0:
#                         print(stack[-1])
#                 else:
#                         print(-1)

# def solution(grid):
#     answer = 0
#     for i in grid:
#         for j in i:

#     return answer


# a = ["??b", "abc", "cc?"]

# print(solution(a))

# # 재귀동닥 예시
# def recur(n):
#     if n < 1:
#         return 0
#     return recur(n-1) + n

# # recur(3) 실행했을때

# # recur(3)실행 원본으로부터 복사본을 가져옴 
# def recur(3): # n == 3
#     if 3 < 1:
#         return 0
#     return recur(3-1) + 3 # n이 1보다 작지 않으므로 recur(2) 실행

# # recur(2) 실행 원본으로부터 복서본 가져옴
# def recur(2): # n == 2
#     if 2 < 1:
#         return 0
#     return recur(2-1) + 2 # n이 1보다 작지 않으므로 recur(1) 실행

# # recur(1) 실행 원본으로부터 복사본을 가져옴 
# def recur(1): # n == 1
#     if 1 < 1:
#         return 0
#     return recur(1-1) + 1 # n이 1보다 작지 않으므로 recur(0) 실행

# # recur(0) 실행 원본으로부터 복사본을 가져옴
# def recur(1): # n == 0
#     if 1 < 1: # n이 1보다 작으므로 0을 반환 함수좀료 스택에서 사라짐
#         return 0
#     return recur(0-1) + 0

# # 이제 호출 했던 곳으로 반환하고 스택에서 사라지는 단계를 반복 결과적으로 recur(3) == 6

# # int
# a = 1
# print(id(a))
# a += 1
# print(id(a))

# # str
# a = 'a'
# print(id(a))

# a += 'b'
# print(id(a))

# # tuple

# a = (1,2)
# print(id(a))

# a += (3,)
# print(id(a))

# # int
# a = 1
# b = a
# print(a == b) # True
# b += 1
# print(a == b) # False

# # String
# a = 'a'
# b = a
# print(a == b) # True
# b += 'b'
# print(a == b) #False

# # Tuple
# a = (1,2)
# b = a
# print(a == b) # True
# b += (3,)
# print(a == b) # False

# # List
# a = [1,2]
# print(id(a))
# a.append(3)
# print(id(a))

# # Dict
# a = {1:'a'}
# print(id(a))
# a[2] = 'b'
# print(id(a))

# # List
# a= [1,2]
# b = a
# print(a == b) # True
# b.append(3)
# print(a == b) # True

# # Dict
# a = {1:'a'}
# b = a
# print(a == b) # True
# b[2] = 'b'
# print(a == b) # True

# # 얕은 복사
# arr1 = [1,2]
# arr2 = arr1
# arr2.append(3)
# print(arr1)
# print(arr2)

# arr1 = [1,2,3,[4,5,6]]
# arr2 = arr1[:] # 복사

# # 메모리 주소가 다르다 깊은 복사가 아닌가?
# print(arr1, id(arr1)) # [1, 2, 3, [4, 5, 6]] 4315672384
# print(arr2, id(arr2)) # [1, 2, 3, [4, 5, 6]] 4315704448

# # 값이 다름 깊은 복사가 아닌가?
# arr2.append(32)
# print(arr1, id(arr1)) # [1, 2, 3, [4, 5, 6]] 4315672384
# print(arr2, id(arr2)) # [1, 2, 3, [4, 5, 6], 32] 4315704448

# # 리스트 안에 리스트 가르키고있는 주소가 같다 얕은 복사!
# print(arr1[3], id(arr1[3])) # [4, 5, 6] 4315099776
# print(arr2[3], id(arr2[3])) # [4, 5, 6] 4315099776

# # 리스트 안에 리스트에 값 추가
# arr1[3].append(64)
# print(arr1[3], id(arr1[3])) # [4, 5, 6, 64] 4315099776
# print(arr2[3], id(arr2[3])) # [4, 5, 6, 64] 4315099776

# # 전체 다시 확인 내부적으로 보면 앝은 복사이다!
# print(arr1, id(arr1)) # [1, 2, 3, [4, 5, 6, 64]] 4315672384
# print(arr2, id(arr2)) # [1, 2, 3, [4, 5, 6, 64], 32] 4315704448
# # 겉에 있는 리스트만 새롭게 객체를 추가했지만 사실 내부에 있는 리스트 요소는 하나의 [4,5,6] 리스트를 가리키고있음
# # 완전한 깊은 복사도 아니고 완전한 얕은 복사도 아니지만 이것 또한 얕은 복사로 구분한다.

# import copy

# dict1 = {'a': 'rookie', 'b': [1,2,3]}
# dict2 = copy.copy(dict1)

# print(dict1, id(dict1)) # {'a': 'rookie', 'b': [1, 2, 3]} 433311033
# print(dict2, id(dict2)) # {'a': 'rookie', 'b': [1, 2, 3]} 4333110592

# # 새 key, value 추가
# dict2['c'] = '루키쉐'
# print(dict1, id(dict1)) # {'a': 'rookie', 'b': [1, 2, 3]} 4333110336
# print(dict2, id(dict2)) # {'a': 'rookie', 'b': [1, 2, 3], 'c': '루키쉐'} 4333110592

# # 딕셔너리 내부 리스트
# print(dict1['b'], id(dict1['b'])) # [1, 2, 3] 4333439808
# print(dict2['b'], id(dict2['b'])) # [1, 2, 3] 4333439808

# # 내부 리스트에 값 추가
# dict1['b'].append('no')
# print(dict1['b'], id(dict1['b'])) # [1, 2, 3, 'no'] 4333439808
# print(dict2['b'], id(dict2['b'])) # [1, 2, 3, 'no'] 4333439808

# # 전체 다시 확인
# print(dict1, id(dict1)) # {'a': 'rookie', 'b': [1, 2, 3, 'no']} 4333110336
# print(dict2, id(dict2)) # {'a': 'rookie', 'b': [1, 2, 3, 'no'], 'c': '루키쉐'} 4333110592
# # key, value를 추가했을때 보면 깊은 복사 같다.
# # 내부 리스트를 보면 주소가 동일한 것을 볼수 있고 내부 리스트에 값을 추가하면 둘다 추가되는 것을 확인 가능 얕은복사

# import copy

# arr1 = [1,2,3,[4,5,6]]
# arr2 = copy.deepcopy(arr1) # 복사

# # 메모리 주소가 다르다 깊은 복사
# print(arr1, id(arr1)) # [1, 2, 3, [4, 5, 6]] 4367780608
# print(arr2, id(arr2)) # [1, 2, 3, [4, 5, 6]] 4367785152

# # 값이 다름 
# arr2.append(32)
# print(arr1, id(arr1)) # [1, 2, 3, [4, 5, 6]] 4367780608
# print(arr2, id(arr2)) # [1, 2, 3, [4, 5, 6], 32] 4367785152

# # 리스트 안에 리스트 들의 주소가 다르다!
# print(arr1[3], id(arr1[3])) # [4, 5, 6] 4367780288
# print(arr2[3], id(arr2[3])) # [4, 5, 6] 4367780736

# # 리스트 안에 리스트에 값 추가 주소가 달라서 arr2에 영향을 주지 않음
# arr1[3].append(64)
# print(arr1[3], id(arr1[3])) # [4, 5, 6, 64] 4367780288
# print(arr2[3], id(arr2[3])) # [4, 5, 6] 4367780736

# # 전체 다시 확인 독립적이다 깊은 복사
# print(arr1, id(arr1)) # [1, 2, 3, [4, 5, 6, 64]] 4367780608
# print(arr2, id(arr2)) # [1, 2, 3, [4, 5, 6], 32] 4367785152

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)