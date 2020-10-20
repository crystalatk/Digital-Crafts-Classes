# 1. Using a while loop create a program that prints the values 
#   of your favorite movie stars.
#       have a number in front of the printed name.

print("****1****")
fav_stars = ["Julia", "Jim", "Tom"]
i = 0
while i < len(fav_stars):
    print(i + 1, fav_stars[i])
    i += 1



# 2. Using a for loop, re-do the above exercise.
#       (hint) you still need to create a variable that is incrimented.
print("****2****")

fav_stars = ["Johansen", "Carrey", "Rudolf"]
index = 1
for stars in fav_stars:
    print(index,stars)
    index += 1

# 3. Create a program that will add the values of a list of numbers, and then print out the results.

#       (hint) You will need to create a variable to hold the current value.
#       Repeat with several different lists of numbers of different lengths.
#            # the list of numbers is [1,2,3]
#            #output to console
#            6
print("****3****")

list_1 = [2,4,6,8]
a = 0
for number in list_1:
    a = number + a
print(f"List 1 total: {a}")

list_2 = [1,2,3]
b = 0
for number_2 in list_2:
    b = number_2 + b
print(f"List 2 total: {b}")

list_3 = [10,20,30,40,50,60,70,80,90]
c = 0
for number_3 in list_3:
    c = number_3 + c
print(f"List 3 total: {c}")
