# 4. De-dup
# Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.

dup_list = [1, 2, 3, 2, 56, 6, 3]
new_list = []


# for original in dup_list:
#     is_not_a_duplicate = True
#     for new_num in new_list:
#         if original == new_num:
#             is_not_a_duplicate = False
#     if is_not_a_duplicate:
#         new_list.append(original)
# print(new_list)

for item in dup_list:
    if not item in new_list:
        new_list.append(item)

print(new_list)

# You can just turn the list into a set....

print(list(set(dup_list)))