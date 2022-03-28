# 프로그래머스 신규 아이디 추천
import re

def solution(new_id):
    # 소문자로
    id = new_id.lower()

    # 정규 표헌식 숫자 소문자 - _ . 만남김
    id = re.sub('[^a-z\d\-\_\.]', '', id)

    # 문자욜로
    id = ''.join(id)

    # '..' -> '.'
    while '..' in id:
        id = id.replace('..','.')

    # '.'처음과 끝이면 삭제
    if id[0] == '.':
        if len(id) >= 2:
            id = id[1:]
        else:
            id = '.'

    if id[-1] == '.':
        id = id[:-1]
    
    # 비어있으면 a
    if id == '':
        id = 'a'

    # 16자 이상 15자까지만 슬라이싱
    if len(id) >= 16:
        id = id[:15]
        if id[-1] == '.':
            id = id[:-1]

    # 3자 미만 제일 뒤에 문자 반복
    while len(id) < 3:
        id += id[-1]

    return id

a = "/..D.SNA....IDNSAI....N,.,..D1,,...Q21.....41@...@@#$(@_!$($!(#@,...21.."
print(solution(a))