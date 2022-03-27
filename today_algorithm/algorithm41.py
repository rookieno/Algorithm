# 프로그래머스 비밀지도
def solution(n, arr1, arr2):
    answer = []
    dic = zip(arr1,arr2)
    for i,j in dic:
        result = bin(i|j)[2:]
        if len(result) < n:
            result = '0'*(n-len(result))+result
        result = result.replace('0',' ')
        result = result.replace('1','#')
        answer.append(result)

    return answer

# rjust