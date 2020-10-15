# 2. Factor a Number
# Given a number, print its factors.

while True:
    try:
        user_number = int(input("What number would you like to find the factors of?\n"))
        break
    except ValueError:
        print("Please use a number.")

max_number = user_number + 1

for n in range(1, max_number):
    factor = (user_number / n)
    if factor.is_integer():
        print(int(factor))
    n += 1