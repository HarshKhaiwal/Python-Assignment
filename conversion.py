# Convert a Decimal number to Binary, Octal and Hexadecimal
x = int(input('Enter a decimal no.'))
print(bin(x).replace('0b', '') + " in binary " + oct(x) + " in Octal and " + hex(x) + " in Hexadecimal")

