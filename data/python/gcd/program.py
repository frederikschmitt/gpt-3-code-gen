x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
while y != 0:
    temp = y
    y = x % y
    x = temp
print(f"The greatest common divisor is {x}")