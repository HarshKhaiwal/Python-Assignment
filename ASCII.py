# function to convert character to ascii value and vice-a-versa
def chartoASCII(x):
    print("ASCII value of {} is {}".format(x, ord(x)))


def ASCIItochar(y):
    print("Character encoded by ASCII value {} is {}".format(y, chr(y)))


x = input("Enter a character : ")
chartoASCII(x)

y = int(input("Enter an ASCII value : "))
ASCIItochar(y)

