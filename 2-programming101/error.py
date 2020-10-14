# Error Handling
# 10/0 #<<<<<---Errors!

try:
    if 2 > "3":
        print("Never Prints")
except TypeError:
    print("You did something wrong with the type")
except ZeroDivisionError:
    print("You tried to divide by 0")

#try gets you around an error, but considered very bad!
#will catch any type of exception. including control c -> won't exit the loop

print("**Part 2***")
try:
    100 / int(input("Give me a number\n"))
except ZeroDivisionError:
    print("You tried to divide by 0")
except TypeError:
    print("You did something wrong with the type")
except ValueError:
    print("You didn't give a number! I said a number!")

#If you use the variable again outside of the try blocks, it will still throw an error.

print("***Part 3***")
my_num = input("Give me a number")

try:
    my_num = int(my_num)
    print(100 / my_num)
except ZeroDivisionError:
    print("You Tried to Divide by Zero")
except TypeError:
    print("You did something wrong with the type")
except ValueError:
    print("You didn't give a number")

print(my_num)