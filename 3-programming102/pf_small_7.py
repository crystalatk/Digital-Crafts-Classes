# # 7. Multiply a list
# Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.

# #

my_numbers = [3, 5, 4, 8, 9]
a = 5
a_numbers = []

for new in my_numbers:
    a_numbers.append(new *a)
print(a_numbers)