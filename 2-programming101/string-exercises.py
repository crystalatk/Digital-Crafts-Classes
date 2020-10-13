# 1. Create a program that prints out the combination of two different strings.
print("***strings***")
print("dog" + " brain")

# 2. rint out a haiku that spans across multiple lines using only a single string.

print("***haiku***")
haiku = "Eddie is silly,\n\the likes to climb trees and dig,\nI'm so glad he's mine!"
print(haiku)

# 3. Create a program that prints the following 3 times:
# #   Hello [person], 
#   I hope that your [today] is going well. 
#   I'm personally really [emotion].
# Where [person], [today], [emotion] are variables and using 3 different syntaxes.
#   Hello Clint,
#   I hope that your Thursday is going well.
#   I'm personally really well.

print("***attempt 1***")
# interpolation
person = "Ella"
today = "Monday"
emotion = "happy"
print("Hello %s,\nI hope that your %s is going well.\nI'm personally really %s." % (person, today, emotion))

print("***attempt 2***")
# concatenate
person = "Eli"
today = "Friday"
emotion = "disappointed"
print("Hello " + person + ",\nI hope that your " + today + " is going well.\nI'm personally really " + emotion + ".")

print("***attempt 3***")
# f-string
person = "Trixxy"
today = "night"
emotion = "snuggly"
combined = f"Hello {person},\nI hope that your {today} is going well.\nI'm personally really {emotion}."
print(combined)