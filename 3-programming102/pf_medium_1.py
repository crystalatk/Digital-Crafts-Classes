# 1.  Multiply Vectors
# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]
# 1
# #


list_a = [1, 2, 3, 4]
list_b = [5, 4, 3, 2]
list_c = []
for count in range(0, len(list_a)):
    m = list_a[count] * list_b[count]
    list_c.append(m)


print(list_c)
