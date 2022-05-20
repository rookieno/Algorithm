"""
배송비가 2000, 3000, 4000 천원씩 늘어난다고 가정
하나의 창고에서 해결가능한 것을 제일 합리적이다고 가정
ex) case1: (1,2), case2:(3) 두가지가 가능할 때 case2가 한 창고에서 모두 해결 가능하기 때문에 case2 선택
1. 한 곳의 창고에서 원하는 주문을 모두 처리가능한지를 확인 1번 창고부터
2. 1번 창고부터 주문량에 맞게 뽑고 나머지 창고중에 남은 주문을 한번에 해결가능한지 확인을 반복 (창고와 뽑아간 과일종류, 개수를 저장), (현재 남은 주문량 업데이트)
3. 반복이 끝난 후 주문이 가능하면 저장해놓은 창고들을 출력 불가능할시 빈 리스트 출력
"""
class InventoryAllocator():
    def __init__(self, order, warehouse):
        self.order = order
        self.warehouse = warehouse
    
    def get_order(self):
        return self.order
    
    def get_warehouse(self):
        return self.warehouse

    """
    한 창고에서 해결이 가능한지 확인
    """
    def available_in_one_warehouse(self, order, warehouse):
        answer = []
        order_num = len(order)
        for i in warehouse:
            cnt = 0
            check = {}
            check[i['name']] = {}
            for fruit, num in order.items():
                if fruit in i['inventory'].keys() and i['inventory'][fruit] >= num:
                    cnt += 1
                    if num != 0:
                        check[i['name']][fruit] = num
                    if cnt == order_num:
                        answer.append(check)                   
                        return answer
        return False
    
    """
    첫 번째 창고부터 탐색
    """
    def solution(self):
        order = self.get_order()
        warehouse = self.get_warehouse()
        answer = []

        """한 창고에서 해결가능한지"""
        result = self.available_in_one_warehouse(order, warehouse)
        if result != False:
            return result

        for target, i in enumerate(warehouse):
            check = {}
            check[i['name']] = {}
            if target != 0:
                check_one = self.available_in_one_warehouse(order, warehouse[target:])
                if check_one != False:
                    for fruit, num in order.items(): 
                        order[fruit] = 0
                    answer.append(check_one[0])
                    break
                    
            for fruit, num in order.items():

                if fruit in i['inventory'].keys():

                    if 0 < i['inventory'][fruit] < num:
                        order[fruit] -= i['inventory'][fruit]
                        check[i['name']][fruit] = i['inventory'][fruit]

                    elif num != 0 and i['inventory'][fruit] >= num:
                        order[fruit] -= num
                        check[i['name']][fruit] = num

            if check[i['name']] != {}:
                answer.append(check)
        
        """
        주문이 해결되었는지 확인
        """
        check_order = list(set(order.values()))
        if len(check_order) == 1 and check_order[0] == 0:
            return answer
        else:
            return []

#region testcodes
"""테스트 에시 1"""
print('testcase1:', end=' ')
test1 = InventoryAllocator({'apple': 1 },[{ 'name': 'owd', 'inventory': { 'apple': 1 } }])
print(test1.solution())

"""테스트 예시 2"""
print('testcase2:', end=' ')
test2 = InventoryAllocator({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }])
print(test2.solution())

"""테스트 예시 3"""
print('testcase3:', end=' ')
test3 = InventoryAllocator({ 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}])
print(test3.solution())

"""한 창고에서 모두 해결 가능할 경우"""
print('testcase4:', end=' ')
test4 = InventoryAllocator({ 'apple': 10, 'banana': 1}, [{ 'name': 'owd', 'inventory': { 'apple': 7 , 'banana': 2 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}, { 'name': 'ok', 'inventory': { 'apple': 10, 'banana': 1}}])
print(test4.solution())

"""두 품목의 주문에서 한 품목이 불가능 할 경우"""
print('testcase5:', end=' ')
test5 = InventoryAllocator({ 'apple': 10, 'banana': 7 }, [{ 'name': 'owd', 'inventory': { 'apple': 5, 'banana': 3 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}, { 'name': 'ok', 'inventory': { 'apple': 10 }}])
print(test5.solution())

"""1번, 3번 창고에서 처리하는게 가장 합리적일 경우"""
print('testcase6:', end=' ')
test6 = InventoryAllocator({ 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5} }, { 'name': 'dm', 'inventory': { 'apple': 3 }}, { 'name': 'ok', 'inventory': { 'apple': 5}}])
print(test6.solution())

"""1번, 3번 창고에서 처리하는게 가장 합리적일 경우 2가지 주문"""
print('testcase7:', end=' ')
test7 = InventoryAllocator({ 'apple': 10, 'banana': 3 }, [{ 'name': 'owd', 'inventory': { 'apple': 5, 'banana': 1} }, { 'name': 'dm', 'inventory': { 'apple': 3, 'banana': 2 }}, { 'name': 'ok', 'inventory': { 'apple': 5, 'banana': 2}}])
print(test7.solution())

"""한 창고에서 해결 가능한 경우가 2가지 일때 가장 저렴한 창고"""
print('testcase8:', end=' ')
test8 = InventoryAllocator({ 'apple': 10, 'banana': 1}, [{ 'name': 'owd', 'inventory': { 'apple': 7 , 'banana': 2 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}, { 'name': 'ok', 'inventory': { 'apple': 10, 'banana': 10}}, { 'name': 'ok2', 'inventory': { 'apple': 10, 'banana': 1}}])
print(test8.solution())

"""3가지 주문 한 창고에서 해결 가능할 경우"""
print('testcase9:', end=' ')
test9 = InventoryAllocator({ 'apple': 10, 'banana': 1, 'orange': 4}, [{ 'name': 'owd', 'inventory': { 'apple': 7 , 'banana': 2 , 'orange': 3} }, { 'name': 'dm', 'inventory': { 'apple': 5 }}, { 'name': 'ok', 'inventory': { 'apple': 10, 'banana': 10, 'orange': 40}}])
print(test9.solution())

"""3가지 주문 1번, 3번 창고에서 처리하는게 가장 합리적일 경우"""
print('testcase10:', end=' ')
test10 = InventoryAllocator({ 'apple': 10, 'banana': 1, 'orange': 4}, [{ 'name': 'owd', 'inventory': { 'apple': 7 , 'banana': 2 , 'orange': 3} }, { 'name': 'dm', 'inventory': { 'apple': 5 }}, { 'name': 'ok', 'inventory': { 'apple': 10, 'banana': 1, 'orange': 2}}])
print(test10.solution())

"""3가지 주문 기본"""
print('testcase11:', end=' ')
test11 = InventoryAllocator({ 'apple': 10, 'banana': 1, 'orange': 4}, [{ 'name': 'owd', 'inventory': { 'apple': 7 , 'banana': 2 , 'orange': 3} }, { 'name': 'dm', 'inventory': { 'apple': 3 }}, { 'name': 'ok', 'inventory': { 'apple': 1, 'banana': 1, 'orange': 2}}])
print(test11.solution())

"""1번 창고에 주문 품목이 없을때"""
print('testcase12:', end=' ')
test12 = InventoryAllocator({ 'banana': 1, 'orange': 4}, [{ 'name': 'owd', 'inventory': { 'apple': 7} }, { 'name': 'dm', 'inventory': { 'orange':4 }}, { 'name': 'ok', 'inventory': { 'apple': 1, 'banana': 1, 'orange': 2}}])
print(test12.solution())
#endregion