list1 = []
list2 = []
n = int(input('Enter no. of elements you want to enter in a list : '))
for i in range(0, n):
    x = int(input())
    list1.append(x)
print('Original list {}'.format(list1))
list1.sort()
for i in range(len(list1) - 1):
    if list1[i] == list1[i + 1]:
        list2.append(list1[i])
print("list containing duplicate elements {}".format(list2))

