# 6. Positive Numbers II
# Create a list of numbers, create a new list which contains every number in the given list which is positive.


my_numbers = [2, -5, -6, -7, 8]
pos_numbers = []
for current in my_numbers:
    if 0 < current:
        pos_numbers.append(current)
print(pos_numbers)