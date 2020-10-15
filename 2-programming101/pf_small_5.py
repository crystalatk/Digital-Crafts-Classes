print("Let's guess a day of the week!")
try:
    day = int(input('Pick a Day (0-6)? '))
    if day == 0 or day == 6:
        print("Sleep in")
    elif 6 > day > 0:
        print("Go to work")
    else:
        print("This does not follow our days of the week. Please enter a number between 0 & 6")
except ValueError:
    print("Cannot Process. Please enter a number from 0 - 6.")