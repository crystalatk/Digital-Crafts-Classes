my_children = ["Olivia", "Alle", "Mark"]


print("***While Loop***")
index = 0 #This variable name could be anything....

# Just like you can put a variable into a list, you can use a variable to access the index
my_children[index] #my_children[0] <---exact same thing...
while index < len(my_children): #This will give us the length of the list!
    print(index + 1, my_children[index])
    index += 1

print("***For Loop***")
#Range is created on the spot!

index = 0
for child in my_children: #for each item in my_children list, i'm going to assign it to child, over and over until finished.
    print(index,child)
    index += 1 #Do not have to increase the index for the for loop, this is for better printing...The index doesn't impact the looping. So we can start at whatever number we want...

print("***Enumerate in the For Loop***")
#  There is a function called enumerate.
# It will create a variable in front of child.

for idx, child in enumerate(my_children):
    print(idx,child)


# You can use the .index() to show index number

for example:
    my_list = ["she", "he", "they"]
    my_list.index() # this is fine in a for loop...

# range is creating a list in the previous for loops. except that ranges do not include the last term...
# You can even insert a list directly into the for loop.
# for i in range(10):
# same as
# for i in [1,2,3,4,5,6,7,8,9,]:
