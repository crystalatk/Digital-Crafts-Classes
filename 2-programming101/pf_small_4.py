print("Let's guess a day of the week!")
try:
    day = int(input('Pick a Day (0-6)? '))
    if day == 0:
        print("Sunday")
    elif day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    else:
        print("This does not follow our days of the week. Please enter a number between 0 & 6")
except ValueError:
    print("Cannot Process. Please enter a number from 0 - 6.")
