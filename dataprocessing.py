# # START

# 11
negative = 0
while True:
    num: int = int(input("11. Enter a number: "))
    if num == 0:
        break
    if num < 0:
        negative += num
print(negative)

# 12
listnum: list[int] = []
for i in range(10):
    numl: int = int(input("12. Enter a number:"))
    listnum.append(numl)
print(listnum[::-1])

# 13
prime_list: list[int] = []
while True:
    num13: int = int(input("13. Enter a number: "))
    if num13 == 0:
        break
    elif num13 == 2:
        prime_list.append(num13)
    if num13 < 2:
        continue
    elif num13 % 2 == 0:
        continue
    else:
        divider: int = 3
        found_divider: bool = False
        while divider < num13 ** 0.5 + 1:
            if num13 % divider == 0:
                found_divider = True
                break
            divider += 2
        if not found_divider:
            prime_list.append(num13)
print(prime_list)

# 14
num_list: list[int] = []
for i in range(5):
    num14: int = int(input("14. Enter a number: "))
    num_list.append(num14)
average_num: float = sum(num_list) // len(num_list)
above_average: list[int] = [num14 for num14 in num_list if num14 > average_num]
print(f"The average of the numbers is {average_num}")
print(f"There are {len(above_average)} numbers that are above average and they are: {above_average}")

# 15
num1: int = int(input("15. Enter a number: "))
num2: int = int(input("Enter a number that's smaller: "))
if num2 == 0:
    print("No number can divide by 0.")
else:
    print(f"The dividend of the numbers is {num1 // num2}")



# BONUS

# 16
dig_three: int = int(input("16. Enter a three digit number: "))
meot: int = dig_three // 100
asarot: int = (dig_three // 10) % 10
ahadot: int = dig_three % 10
sum_three_dig: int = meot + asarot + ahadot
print(f"The sum of the digits is {"" if sum_three_dig % 3 == 0 else "not"} divided by 3")

# 17
word: str = input("17. Enter a palindrome: ")
reversed_word = word[::-1]
print(f"The word is {"reversed." if word == reversed_word else "not reversed."}")

# STOP
