def solution(clothes):
    dict = {}
    answer = 1
    for value, key in clothes:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    for key, value in dict.items():
        answer *= (value + 1) # 입는경우 안입는경우가 있으므로 +1 해줌
     
    return answer - 1 # 모두 안 입는경우를 뺀다


a = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
b = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(a))
print(solution(b))