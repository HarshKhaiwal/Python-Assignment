def sumofdigits(x):
    sod = 0
    for i in range(0, len(str(x))):
        sod += int(x[i])
    print('Sum of digits of {} is {}'.format(x, sod))


x = input('Enter a no. : ')
sumofdigits(x)
