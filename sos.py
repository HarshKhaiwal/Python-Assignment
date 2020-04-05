# find sum of series 1/2 + 2/3 + ¾ + …..+ n/n+1
n = int(input('Enter n : '))
sos = 0.0
for i in range(1, n + 1):
    sos += i / (i + 1)
print('Sum of series for first {} terms is {}'.format(n, sos))

