# 8. Reverse a String
# Given a string, print the string reversed.

# #

string = "I want to sleep."
stringlist = list(string)
loc = len(stringlist)
counter = 1
backwards = []
for letter in stringlist:
    backwards.append(stringlist[loc-counter])
    counter += 1
backwards_final = "".join(backwards)
print(backwards_final)