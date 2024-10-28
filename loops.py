# START

# 6
n: int = int(input("6. Enter a number: "))
for i in range(n, 0, -1):
    print(i, end=", ")
print()

# 7
num1: int = int(input("7. Enter a number: "))
num2: int = int(input("Enter a number that's bigger: "))
if num2 <= num1:
    print("The second number needs to be bigger than the first one.")
else:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i, end=" ")
print()

# 8
num8: int = int(input("8. Enter a positive number: "))
for i in range(1, num8 + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" ")
print()

# 9
num9: int = int(input("9. Enter a number: "))
for i in range(1, num9 + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()

# STOP
