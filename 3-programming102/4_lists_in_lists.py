
# Lists in Lists!

people = [
    ["Clint", "Fleetwood", 38], 
    ["Anna", "Fleetwood", 37]
] #tabbing doesn't matter when you are inside of a list. This is not a block of code, just an easy way to view the lists

# If there was an integer in the people, not a list, setting it to a variable and then changing that variable would not change it in people

coordinates = [
      [10,10], #Can comment per line!
      [20,10],
      [10,20]
  ]


# Accessing nested Lists!

print(people[0])

print(people[0][2])

# or

me = people[0]
print(me[2])

people[0][2] = 39 #if I did me[2] = 39, it would change the array in people as well!
print(people)

print(me)

del people[1][2]
print(people)


# Looping through nested Lists!

more_people = [
      ["Clint","Fleetwood", 38], 
      ["Anna", "Fleetwood", 37],
      ["Peter", "Hollens", 34],
      ["Lindsey", "Sterling", 35]
]

for person in more_people:
    print("First", "Last", "Age")
    for attribute in person:
        print(attribute)

coordinates = [[10,10], [20,10],[10,20]]

for cord in coordinates:
    idx = 0
    print("Position:")
    for position in cord:
        p = "X"
        if idx == 1:
            p = "Y"
        print(f"{p}-{position}")
        idx += 1
