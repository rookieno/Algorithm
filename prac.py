# import math

# print(math.lcm(3,5))

# a = []
# print(a[-1:])

# 한번에 받아왔다.
msg1 = 'a b 2022-03-22 2022-03-22'
cnt = 0
msg1 = (msg1.split(' '))
print(msg1)
for i,j in enumerate(msg1):
    if j.isalnum():
        title = msg1[:i+1]
        back = msg1[i+1:]
