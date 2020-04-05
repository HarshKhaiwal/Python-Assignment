k = int(input("Enter the  length k : "))

print(*list(x for x in list(input("Enter the string : ").split()) if len(x) > k))

