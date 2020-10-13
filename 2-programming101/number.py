# integers
1
352
-4534
90
0

# Not an integer
"43" #this is a string!

# floats are decimals! Python2 handles floats differently, use python3
1.2
.390807
-57398.342
# there are only so many decimals to the right, but for most things they are more than enough

# 3+2 #addition
# 3-2 #subtraction
# 3*2 #multiplication
# 3/2 #division
# 3+2*3/2 #order of operation

a = 20
b = 30

# prints results of expression, not the string. Identifies as numbers and calculation
print(30+20)

print(30+a)

print(a+b)

#doesn't change values of a and b, they are not redifined.
print(a)

# Also, reassigning later only reassigns later
a = 40

print(a+b) #with new a value

print("back to a=20")
# change back a for sake of notes and class....
a = 20

# create an expression to assign the variable
c = a + b #for operators, spaces don't matter c = a+b, c = a +    b

print(c)

d=a+b #testing the theory

print("testing theory")
print(d)

print("new a=22")

a = 22

e = a+b

print(e)
print("using a +22 to redifine a")
a = a + 22 #can use a variable to reassign the variable, this is 20+22

print(a)

print("incriment test +1")
# incrimentor operator
a += 1 #same as a = a+1
print(a)
# can incriment by any amount (a += 20 would be increase by 20)

print("decrease test by -100")
# to decrease, use minus instead of +
a -= 100
print(a)


# You can't print directly from the increment because there is no value, it has to do work!
# but a+b can be in a print because it has a value
# since a += b is a = a+b, it is changing the variable....

