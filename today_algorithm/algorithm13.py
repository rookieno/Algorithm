# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.

# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드

# def solution(name):
#     count = 0
#     for i in name:
#         if i == 'A':
#             if name.index(i) > (len(name) - 1 / 2):
#                 count += len(name) - name.index(i)
#             else:
#                 count += name.index(i)
#         elif i != 'A':
#             if ord(i) - ord('A') <= 13:
#                 count += ord(i) - ord('A')
#             else:
#                 count += 26 - (ord(i) - ord('A'))       
#     return count + len(name)
# 인덱스 값을 고려해야함...

# def solution(name):
#     count = 0
#     for i in name:
#         if name.index(i) != 0 and name.index(i) > (len(name) / 2):
#             count += (len(name) - 1) - name.index(i)
#             if ord(i) - ord('A') <= 13:
#                 count += ord(i) - ord('A')
#             else:
#                 count += 26 - (ord(i) - ord('A'))
#         elif name.index(i) == 0:
#             if ord(i) - ord('A') <= 13:
#                 count += ord(i) - ord('A')
#             else:
#                 count += 26 - (ord(i) - ord('A'))
#         else:
#             count += name.index(i) 
#             if ord(i) - ord('A') <= 13:
#                 count += ord(i) - ord('A')
#             else:
#                 count += 26 - (ord(i) - ord('A'))
#     return count
# 복잡하다 enumerate를 쓰자...

# def solution(name):
#     count = 0
#     for i, alpha in enumerate(name):

#         if i != 0 and alpha != 'A' and (i > len(name) / 2):
#             count += len(name) - i
#             if ord(alpha) - ord('A') <= 13:
#                 count += ord(alpha) - ord('A')
#             else:
#                 count += 26 - (ord(alpha) - ord('A'))

#         elif i != 0 and alpha != 'A' and i <= (len(name) / 2):
#             count += i
#             if ord(alpha) - ord('A') <= 13:
#                 count += ord(alpha) - ord('A')
#             else:
#                 count += 26 - (ord(alpha) - ord('A'))
        
#         else:
#             if ord(alpha) - ord('A') <= 13:
#                 count += ord(alpha) - ord('A')
#             else:
#                 count += 26 - (ord(alpha) - ord('A'))
#     return count
# 예외처리 현재 위치를 고려해야함...

# 상하 이동횟수 , 좌우 이동횟수 나누어서 구하고 합치자

def solution(name):
    up_down_count = 0
    left_right_count = 0

    for i, alpha in enumerate(name):
        up_down_count += min(ord(alpha) - ord('A'), 26 - (ord(alpha) - ord('A')))
        
        next_alpha = i + 1
        if next_alpha < len(name) and name[next_alpha] == 'A':
           left_right_count += min(i + len(name[next_alpha+1:]), len(name) - 1)
    
    if 'A' not in name:
        left_right_count += len(name) - 1

    return up_down_count + left_right_count

print(solution('JAZ'))
print(solution('JAN'))
print(solution('JEROEN')) 



