# 2. Largest Number
# Create a list of numbers, print the largest of the numbers.

my_numbers = [0, 2, 5, 6, 7, 8, 0, 2]
greatest_number = my_numbers[0]
for current in my_numbers:
    if greatest_number < current:
        greatest_number = current
print(greatest_number)
