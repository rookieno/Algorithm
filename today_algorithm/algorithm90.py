# 백준 2751번 수 정렬하기 2

# sorted가 기본적으로 병합정렬기반으로 만들어짐
def merge(arr1, arr2):
    target = []
    arr1_index = 0
    arr2_index = 0
    while arr1_index < len(arr1) and arr2_index < len(arr2):
        if arr1[arr1_index] < arr2[arr2_index]:
            target.append(arr1[arr1_index])
            arr1_index += 1
        else:
            target.append(arr2[arr2_index])
            arr2_index += 1
    
    if arr1_index == len(arr1):
        while arr2_index < len(arr2):
            target.append(arr2[arr2_index])
            arr2_index += 1
    
    if arr2_index == len(arr2):
        while arr1_index < len(arr1):
            target.append(arr1[arr1_index])
            arr1_index += 1
    return target

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    return merge(left_array, right_array)

import sys

n  = int(sys.stdin.readline())

result = []

for _ in range(n):
    result.append(int(sys.stdin.readline()))


answer = merge_sort(result)

for i in answer:
    print(i)