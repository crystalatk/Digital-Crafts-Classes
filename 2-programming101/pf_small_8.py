try:
    start = int(input("Choose any whole number to start with.\n"))
    end = int(input("Choose any whole number to end with.\n"))
    print("Thank you!")
    while start <= end:
        print(start)
        start += 1
except ValueError:
    print("I said, choose a whole number!")

