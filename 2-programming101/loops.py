# While Loops!

i = 2
max_num = 20 
increment = 2
while i < max_num: #will keep looping until while statement is false
    print(i)
    i += 1 #increment syntax (same as i = i + 1)(to deincrement, i -= 1 counts down)

#While look is self-contained, doesn't go above the indention

# You can increment by any value. So you can add it to a number, a variable, even itself!

# Infitite Loop: if you make a loop with no ending, you need to hit control + c


## Input to stop a loop
name = ""
while name != "clint":
    name = input("Please say your name is clint\n")

print("Great, I knew you could do it.")
