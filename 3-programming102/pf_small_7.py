# # 7. Multiply a list
# Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.

# #

my_numbers = [3, 5, 4, 8, 9]
a = 5
a_numbers = []
count = 0
for new in my_numbers:
    new = a * my_numbers[count]
    a_numbers.append(new)
    count += 1
print(a_numbers)