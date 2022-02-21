import re

# def solution(s):
#     result = []    
#     only_num = re.findall('\d', s)
#     tuple = set(only_num)

#     for i in tuple:
#         result.append(int(i))

#     return result


# def solution(s):
#     result = []    
#     only_num = re.findall('\d+', s)
#     tuple = set(only_num)
#     print(tuple)

#     for i in tuple:
#         result.append(int(i))

#     return result

def solution(s):
    result = []
    repeat = []
    answer = []

    only_num = re.findall('\d+', s) # 정규표현식 숫자만 남김 \d+ 연결된숫자는 연걸되게
    
    tuple = set(only_num) # 중복제거

    for i in tuple:
        a = only_num.count(i) # 하나의 숫자가 몇번나오는지 
        result.append(int(i)) # 중복제거판 리스트 정수형으로 만들기
        repeat.append(int(a)) # 반복되는 횟수 리스트 정수형으로 만들기
    
    dictionary = dict(zip(repeat,result)) # 딕셔너리 형태로 반복수:숫자 

    sort_dict = sorted(dictionary.items(), reverse=True) # 키값(반복수)를 기준으로 내림차순 정렬
    
    for i in range(len(sort_dict)): 
        answer.append(sort_dict[i][1]) # 정렬된 딕셔너리에서 벨류값만 저장

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))