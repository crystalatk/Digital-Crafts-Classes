# # 3. Smallest Number
# Create a list of numbers, print the smallest of the numbers.

# #

my_numbers = [2, 5, 6, 7, 8]
smallest_number = my_numbers[0]
for current in my_numbers:
    if smallest_number > current:
        smallest_number = current
print(smallest_number)