# START
from cmd import PROMPT

# 1
decimal: float = float(input("1. Enter a decimal number: "))
# if decimal > 10:
#     print(f"The difference between {decimal} and 10 is: {decimal - 10}")
# else:
#     print(f"The multiplier between {decimal} and 10 is: {decimal * 10}")
print(f"The difference is {decimal - 10}" if decimal > 10 else f"The multiplier is {decimal * 10} ")

# 2
total_sum: float = 0
for i in range(3):
    dec_num: float = float(input("2. Enter a decimal number: "))
    total_sum += dec_num
print(f"The sum of the numbers is {total_sum}." if total_sum > 100 else f"The sum is smaller than 100.")

# 3 - BONUS

dec_1: float = float(input("3. Enter a decimal number: "))
dec_2: float = float(input("Enter a decimal number: "))
frac1: float = dec_1 - int(dec_1)
frac2: float = dec_2 - int(dec_2)
if frac1 == frac2:
    print("The fractions are equal.")
elif frac2 > frac1:
    print(f"The bigger fraction is {frac2}.")
else:
    print(f"The bigger fraction is {frac1}.")

# 4
age: int = int(input("4. Enter a age: "))
print(f"Age is illegal." if age > 120 or age < 0 else age)

# 5
three_dig: int = int(input("5. Enter a 3 digit number:"))
# int
print(f"The digit in the middle is {(three_dig % 100 - three_dig % 10) // 10}" if 100 <= three_dig <= 999 else "Enter a three digit number.")
# str
# three_dig: str = (input("Enter a 3 digit number:"))
# if len(three_dig) == 3 and three_dig.isdigit():
#     print(f"The digit in the middle is {three_dig[1]}")
# STOP
