decimal = int(input("Enter a decimal number: "))

num = decimal

binary = ""

while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

print("The binary form of", num,"is:",binary)