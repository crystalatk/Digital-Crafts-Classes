try:
    C = int(input("Temperature in C?\n"))
    F = (C * 9/5) + 32
    print(f"{F} F")
except ValueError:
    print("I need a number, boss!")