n = 0
try:
    max_lines = int(input("How big do you want the shape to be?\n"))
    while n < max_lines:
        n += 1
        print("*" * max_lines)
except ValueError:
    print("It needs to be a number, silly pants!")


print("break")

# Another Solution

max_lines = int(input("How big do you want the shape to be?\n"))
stars = "*" * max_lines + "\n"

print(stars * max_lines)