#  Matrix Addition
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:

# [ [2, -2],
#    [5, 3] ]
# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add

# 1 3
# 2 4

# and
# 5 2
# 1 0

# results in

# 6 5
# 3 4

matrix_a = [[3, 1],
        [4, 6]
        ]

matrix_b = [[8, 2],
        [5, 7]
        ]
matrix_c = []
matrix_d = []

for i in range(len(matrix_a)):
    for l in range(len(matrix_a[i])):
        sum_1 = matrix_a[i][l] + matrix_b[i][l]
        if i < 1:
            matrix_c.append(sum_1)
        else:
            matrix_d.append(sum_1)
matrix_e = [matrix_c] + [matrix_d]
print(matrix_e)