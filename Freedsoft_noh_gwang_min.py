# class InventoryAllocator():
#     def __init__(self, order, inventory):
#         self.order = order
#         self.inventory = inventory
    
#     def get_order(self):
#         return self.order
    
#     def get_inventory(self):
#         return self.inventory

#     def solution(self):
#         order = self.order
#         inventory = self.inventory

#         return 

# test1 = InventoryAllocator({'apple': 1 },[{ 'name': 'owd', 'inventory': { 'apple': 1 } }])

# test2 = InventoryAllocator({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }])

# test3 = InventoryAllocator({ 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}])

# print(test3.solution())

a = {'apple': 5}

b = [{ 'name': 'owd', 'inventory': { 'apple': 5 }}, { 'name': 'dm', 'inventory': { 'apple': 5, 'banana': 3 }}]


def solution(order, warehouse):
    answer = []
    for fruit, num in order.items():
        for i in warehouse:
            target_inventory = i['inventory']
            if fruit in target_inventory.keys():
                if num == target_inventory[fruit]:
                    i['inventory'] = {fruit: num}
                    answer.append(i)
                    break
    return answer
            


print(solution(a,b))