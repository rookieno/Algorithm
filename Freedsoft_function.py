def solution(order, warehouse):
        answer = []
        order_num = len(order)

        for i in warehouse:
            cnt = 0
            check = {}
            check[i['name']] = {}

            """
            한 창고에서 모두 처리가능한지 확인
            """
            for fruit, num in order.items():
                if fruit in i['inventory'].keys() and i['inventory'][fruit] >= num:
                    cnt += 1
                    check[i['name']][fruit] = num
                    print(check)
                    if cnt == order_num:
                        answer.append(check)
        return answer

def solution2(order, warehouse):
    answer = []

    for i in warehouse:
        check = {}
        check[i['name']] = {}
        for fruit, num in order.items():
            if fruit in i['inventory'].keys():
                if 0 < i['inventory'][fruit] < num:
                    order[fruit] -= i['inventory'][fruit]
                    print(order)
                    check[i['name']][fruit] = i['inventory'][fruit]
                elif i['inventory'][fruit] >= num:
                    order[fruit] -= num
                    print(order)
                    check[i['name']][fruit] = num

        answer.append(check)
                    
    return answer