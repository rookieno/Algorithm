# # def extendList(val, list=[]):
# #     list.append(val)
# #     return list

# # list1 = extendList(10)
# # list2 = extendList(123, [])
# # list3 = extendList('a')
# # print(list3)

# # print("list1 = %s" % list1)
# # print("list2 = %s" % list2)
# # print("list3 = %s" % list3)

# # name = 10

# # print("%s" %name)

# def multipliers():
#     return [lambda x: i * x for i in range(4)]
# # print ([m(2) for m in multipliers()])

# # print(multipliers()[0](2))
# # print(multipliers()[1](1))
# # print(multipliers()[2])
# # print(multipliers()[3])

# for i in [lambda x: i * x for i in range(4)]:
#     print(i(1))

# def call():
#     for i in range(4):
#         return lambda x: i * x

# print(call())

# # def test(x):
# #     print(i)
# #     return i * x

# # for i in range(4):
# #     print(test(2))


# # print(test(2))

# # class Parent(object):
# #     x = 1

# # class Child1(Parent):
# #     pass

# # class Child2(Parent):
# #     pass

# # print(Parent.x, Child1.x, Child2.x)
# # Child1.x = 2
# # print(Parent.x, Child1.x, Child2.x)
# # Parent.x = 3
# # print(Parent.x, Child1.x, Child2.x)

# # list = ['a', 'b', 'c', 'd', 'e']

# # print(list[10:])

# # list = [[]] * 5
# # print(list)
# # list[0].append(10)
# # print(list)
# # list[1].append(20)
# # print(list)
# # list.append(30)
# # print(list)

class DefaultDict(dict):
      def __missing__(self, key):
            return []

d = DefaultDict()
d['florp'] = 127
print(id(d))

d = DefaultDict()
print(id(d))
print(f"d 1: {d}")
print(f"d 2: {d['foo']}")

normal = dict()
normal['florp2'] = 127
print(f"normal 1 : {normal}")
print(f"normal 2 :  {normal['foo']}")