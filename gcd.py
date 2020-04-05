print("Enter two no. : ")
x = int(input())
y = int(input())
for i in range(1, min(x, y)+1):
    if x % i == 0 and y % i == 0:
        gcd = i
print("GCD of {} and {} is {}".format(x, y, gcd))


