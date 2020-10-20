# 5. Leetspeak
# Given a paragraph of text as a String, print the paragraph in leetspeak.

# To translate a String to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

# Letter	Translates To
# A	4
# E	3
# G	6
# I	1
# O	0
# S	5
# T	7
# Example: If your program is given the String "I am a leet programmer", it should print "1 4m 4 l337 pr0gr4mm3r" as the leetspeak translation

# #

angelou = "You will face many defeats in life, but never let yourself be defeated."
angeloulist = list(angelou.upper())
leet_lists = [["A", "E", "G", "I", "O", "S", "T"], ["4", "3", "6", "1", "0", "5", "7"]]
leet_angelou = []

for i in angeloulist:
    n = 0
    for j in leet_lists[0]:
        this_is_not_leet = True
        if i == j:
            this_is_not_leet = False
            leet_angelou.append(leet_lists[1][n])
            break
        n += 1    
    if this_is_not_leet:
        leet_angelou.append(i)        
leet_ang = "".join(leet_angelou)
print(leet_ang)

