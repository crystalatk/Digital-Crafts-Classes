# 3. Matrix Addition II
# Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.

# #


matrix_a = [[3, 1, 3, 2, 4],
        [4, 6, 7, 8, 9]
        ]

matrix_b = [[8, 2, 1, 3, 2],
        [5, 7, 9, 8, 6]
        ]
matrix_c = []
matrix_d = []


# for i in range(len(matrix_a)):
#     for j in range(len(matrix_a[i])):
#         sum_1 = matrix_a[i][j] + matrix_b[i][j]
#         if i < 1:
#             matrix_c.append(sum_1)
#         else:
#             matrix_d.append(sum_1)
# matrix_e = [matrix_c] + [matrix_d]
# print(matrix_e)

new_matrix = []
for i in range(len(matrix_a)):
    m = []
    for j in range(len(matrix_a[i])):
        m.append(matrix_a[i][j] + matrix_b[i][j])
    new_matrix.append(m)
print(new_matrix)