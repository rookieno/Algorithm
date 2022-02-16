def solution(clothes):
    dict = {}
    answer = 1
    for value, key in clothes:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    for key, value in dict.items():
        answer *= (value + 1)
     
    return answer - 1


a = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
b = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(a))
print(solution(b))