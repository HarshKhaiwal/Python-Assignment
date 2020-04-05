# Find LCM of two numbers
print('Enter two no. : ')
x = int(input())
y = int(input())
if x > y:
    greater = x
else:
    greater = y
while 1:
    if greater % x == 0 and greater % y == 0:
        lcm = greater
        break
    else:
        greater += 1
print("LCM of {} and {} is {}".format(x, y, lcm))




