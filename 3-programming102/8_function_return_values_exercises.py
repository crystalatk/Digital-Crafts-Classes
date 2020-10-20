# 1. Write a program that has a function with two parameters.

# return the concatinated value of the two parameters.
# print the results.
print("****1****")

def my_function(a, b):
    return a + b

print(my_function("Good", "Bye"))

# 2. Write a program that has a function named total_count that expects a list of strings as it argument when the function is called.

# Have the returned value be a dictionary with the keys 'list_length' and 'total_chars'.
# The list_length value needs to be the length of the list and the total_chars needs to be the total count of characters of all of the items in the array.
# Call the function 3 times with 3 different lists.
# (hint) len is usable on lists and strings.
#     #expected output
#     totals = total_count(['I', 'Am', 'Awesome'])
#     print(totals) #{list_length:3, total_chars:10}
print("***2***")

def total_count(list_of_strings):
    ll_value = len(list_of_strings)
    tc_value = 0
    for string in list_of_strings:
        tc_value += len(string)
    return {'list_length' : ll_value, 'total_chars': tc_value}

print(total_count(["Ella", "Eli", "Caitlin", "Charlotte", "Eddie"]))
print(total_count(["Georgie", "Onyx", "Gandy", "Sophia"]))
print(total_count(["Leo", "Bigsby", "Marley", "Cow", "Chico", "Angie", "BooBoo", "Emu"]))


