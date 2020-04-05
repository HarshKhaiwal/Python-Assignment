x = int(input('Enter no. of parts : '))
list1 = []
for i in range(1, x + 1):
    l = input('Enter the {} auto part\'s name and price : '.format(i)).split(' ')
    list1.extend(l)
print(list1)
