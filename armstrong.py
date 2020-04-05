# Find whether a given number is Armstrong number or not
x = int(input('Enter a no. : '))
temp = x
s = 0
while temp > 0:
    rem = temp % 10
    s += rem ** 3
    temp //= 10
if s == x:
    print("{} is a armstrong no.".format(x))
else:
    print("{} is not a armstrong no.".format(x))

