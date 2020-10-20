# return - In programming terms, returning is the value that a function sends out of the result of calling the function.

def add_numbers(a,b):
    result = a+b
    return result #sends result out

value = add_numbers(1,3)#Where did it go?
print(value)

final = add_numbers(1, 3) / add_numbers(4, 6)
print(final)

print(add_numbers(add_numbers(4, 53), add_numbers(6, 7

)))
def mult_numbers(a, b):
    a * b

print(mult_numbers(5, 6)) #<--Prints None

# Explicit vs Implicit Return

#explicit return
def add_numbers_and_return(a,b):
    print(a+b)
    return a+b # written return is explicit

result = add_numbers_and_return(2,3)
print(result) #5

#implicit return: if no explicit return statement
def add_numbers(a,b):
    print(a+b)

result = add_numbers(2,3)
print(result) #None which is a datatype

#Return statement does not have to do with what is coming in.

def subtract_numbers_and_return(a,b):
    print(a - b)
    return "The operation was complete"#<---The return ends the function!

#Nothing after return will run

#***Return Value from Function****

#directly returning something more complex
def make_dictionary(first, last, phone, zip):
    return {
        "first_name":first,
        "last_name":last,
        "phone_number":phone,
        "zip_code":zip
    }

clint_data = make_dictionary("Clint", "Fleetwood", "555-555-5555", "30076")

print(clint_data["zip_code"])

for key in clint_data:
    print(key)



#Do something a bit more complex
def make_grid(size):
    row = 0
    col = 0
    grid = {}
    while row <= size:
        col = 0
        while col <= size:
            grid[str(col)+'-'+str(row)] = {
                "row":row,
                "col":col
            }
            col +=1
        row += 1
    return grid

grid5 = make_grid(5)
print(grid5['4-3'])