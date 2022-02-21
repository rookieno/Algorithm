def solution(arr1, arr2):
    result = []

    for i in range(len(arr1)):
        half = []
        for j in range(len(arr1[0])):
            a = arr1[i][j] + arr2[i][j]
            half.append(a)
        result.append(half)
    return result

print(solution([[1],[2]],[[3],[5]]))