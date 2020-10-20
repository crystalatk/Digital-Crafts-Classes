# 1. Create a program that starts with an empty dictionary.
# Add 3 different key value pairs to the empty dictionary.
print("***1***")

georgie = {
    "name" : "Georgia",
    "color": "brown",
    "size": "tall",
    "behavior": "good dog",
}
print(georgie)

# 2. Create a program with a dictionary called person.
# The person dictionary needs to have the keys, first_name, last_name, age, hair_color.
# Print each one of these key/values pairs without directly using the key's name as a string by using a for loop.
# After each key value pair, print out a sentence using each one of the keys.
#     Hello Clint Fleetwood. Since you are 38 years old you are too old to ride this ride, but you do have nice brown hair.
print("***2***")

person = {
    "first_name" : "Crystal",
    "last_name" : "Atkinson",
    "age" : "37",
    "hair_color" : "brown",
}

for key in person:
    print(person[key])
    print(f"Hello, {person['first_name']} {person['last_name']}. I hear you are {person['age']}! Congrats! That's so old! But mayby you should dye that {person['hair_color']}...jk")


# 3. Create a program that has a list of dictionaries of people, with each dictionary including name, phone, email.
# For each dictionary print the items in the dictionary.
print("****3****")


people = [
    {
        "name" : "Nancy",
        "phone" : "867-5309",
        "email" : "mil@me.com",
    },
    {
        "name" : "Ella",
        "phone" : "do not call",
        "email" : "leave it alone",
    },
    {
        "name" : "Eli",
        "phone" : "dog",
        "email" : "minecraft?",
    }
]
for key in people:
    print("%s has phone number %s and email %s" % (key["name"], key["phone"], key["email"]))