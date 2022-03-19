# 프로그래머스 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    answer = 0
    in_bridge = [0] * bridge_length # [0, 0]
    sum_weight = sum(in_bridge)
    while len(in_bridge) != 0:
        answer += 1
        a = in_bridge.pop(0)
        if a != 0:
            sum_weight = sum(in_bridge)
            if truck_weights:
                if sum_weight + truck_weights[0] <= weight:
                    in_bridge.append(truck_weights.pop(0))
                    sum_weight = sum(in_bridge)
                else:
                    in_bridge.append(0)
        else:
            if truck_weights:
                if sum_weight + truck_weights[0] <= weight:
                    in_bridge.append(truck_weights.pop(0))
                    sum_weight = sum(in_bridge)
                else:
                    in_bridge.append(0)
            
    return answer


a = 2
b = 10
c = [7,4,5,6]

print(solution(a,b,c))

