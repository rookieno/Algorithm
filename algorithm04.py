# {1/1} {1/2, 2/1} {3/1, 2/2, 1/3} ..

x = int(input())

count = 1

while count < x:
    x -= count
    count += 1

if count % 2 == 0:
    numerator = x
    denominator = count - x + 1
else:
    numerator = count - x + 1
    denominator = x


print('{0}/{1}'.format(numerator,denominator))
    
    
    

