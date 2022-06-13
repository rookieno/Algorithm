# int
a = 1
print(id(a))
a += 1
print(id(a))

# str
a = 'a'
print(id(a))

a += 'b'
print(id(a))

# tuple

a = (1,2)
print(id(a))

a += (3,)
print(id(a))

# int
a = 1
b = a
print(a == b) # True
b += 1
print(a == b) # False

# String
a = 'a'
b = a
print(a == b) # True
b += 'b'
print(a == b) #False

# Tuple
a = (1,2)
b = a
print(a == b) # True
b += (3,)
print(a == b) # False

# List
a = [1,2]
print(id(a))
a.append(3)
print(id(a))

# Dict
a = {1:'a'}
print(id(a))
a[2] = 'b'
print(id(a))

# List
a= [1,2]
b = a
print(a == b) # True
b.append(3)
print(a == b) # True

# Dict
a = {1:'a'}
b = a
print(a == b) # True
b[2] = 'b'
print(a == b) # True

# 얕은 복사
arr1 = [1,2]
arr2 = arr1
arr2.append(3)
print(arr1)
print(arr2)

arr1 = [1,2,3,[4,5,6]]
arr2 = arr1[:] # 복사

# 메모리 주소가 다르다 깊은 복사가 아닌가?
print(arr1, id(arr1)) # [1, 2, 3, [4, 5, 6]] 4315672384
print(arr2, id(arr2)) # [1, 2, 3, [4, 5, 6]] 4315704448

# 값이 다름 깊은 복사가 아닌가?
arr2.append(32)
print(arr1, id(arr1)) # [1, 2, 3, [4, 5, 6]] 4315672384
print(arr2, id(arr2)) # [1, 2, 3, [4, 5, 6], 32] 4315704448

# 리스트 안에 리스트 가르키고있는 주소가 같다 얕은 복사!
print(arr1[3], id(arr1[3])) # [4, 5, 6] 4315099776
print(arr2[3], id(arr2[3])) # [4, 5, 6] 4315099776

# 리스트 안에 리스트에 값 추가
arr1[3].append(64)
print(arr1[3], id(arr1[3])) # [4, 5, 6, 64] 4315099776
print(arr2[3], id(arr2[3])) # [4, 5, 6, 64] 4315099776

# 전체 다시 확인 내부적으로 보면 앝은 복사이다!
print(arr1, id(arr1)) # [1, 2, 3, [4, 5, 6, 64]] 4315672384
print(arr2, id(arr2)) # [1, 2, 3, [4, 5, 6, 64], 32] 4315704448
# 겉에 있는 리스트만 새롭게 객체를 추가했지만 사실 내부에 있는 리스트 요소는 하나의 [4,5,6] 리스트를 가리키고있음
# 완전한 깊은 복사도 아니고 완전한 얕은 복사도 아니지만 이것 또한 얕은 복사로 구분한다.

import copy

dict1 = {'a': 'rookie', 'b': [1,2,3]}
dict2 = copy.copy(dict1)

print(dict1, id(dict1)) # {'a': 'rookie', 'b': [1, 2, 3]} 433311033
print(dict2, id(dict2)) # {'a': 'rookie', 'b': [1, 2, 3]} 4333110592

# 새 key, value 추가
dict2['c'] = '루키쉐'
print(dict1, id(dict1)) # {'a': 'rookie', 'b': [1, 2, 3]} 4333110336
print(dict2, id(dict2)) # {'a': 'rookie', 'b': [1, 2, 3], 'c': '루키쉐'} 4333110592

# 딕셔너리 내부 리스트
print(dict1['b'], id(dict1['b'])) # [1, 2, 3] 4333439808
print(dict2['b'], id(dict2['b'])) # [1, 2, 3] 4333439808

# 내부 리스트에 값 추가
dict1['b'].append('no')
print(dict1['b'], id(dict1['b'])) # [1, 2, 3, 'no'] 4333439808
print(dict2['b'], id(dict2['b'])) # [1, 2, 3, 'no'] 4333439808

# 전체 다시 확인
print(dict1, id(dict1)) # {'a': 'rookie', 'b': [1, 2, 3, 'no']} 4333110336
print(dict2, id(dict2)) # {'a': 'rookie', 'b': [1, 2, 3, 'no'], 'c': '루키쉐'} 4333110592
# key, value를 추가했을때 보면 깊은 복사 같다.
# 내부 리스트를 보면 주소가 동일한 것을 볼수 있고 내부 리스트에 값을 추가하면 둘다 추가되는 것을 확인 가능 얕은복사