# This is the execise material for the Numbers section

# question 1: Write a program that prints out the result of adding two numbers together.
print(3+2)

# quesiton 2: Write a program that prints the results of your age divided by the year you graduated from high school.
a = 2020-1983 #just subtracting to get age since birthday is past...not needed just practice
g = 2002 #year graduated

b = a /g #basic formula for question 2 once variables are defined

print(b)

# question 3: Write a program that 
    # Assigns a number to the variable named 'my_number'.
    # Assign another variable named 'increment_by' another number.
    # increase my_number by the increment_by number 3 times, printing the value of my_number every time.

my_number = 36 #this is a random number I assigned
increment_by = 4 #I like going up by a factor, makes the math easy
my_number += increment_by #this is the actual work. doing the increasing.
# The spacing on the increment statement only matters in the part "+="

print("My first number is",my_number) #First print

my_number += increment_by

print("My second number is",my_number) #second print

my_number += increment_by

print("My third number is",my_number) #third print

