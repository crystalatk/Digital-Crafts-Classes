try:
    start = int(input("Choose any whole number to start with.\n"))
    end = int(input("Choose any whole number to end with.\n"))
    while start <  end:
        start += 1
        print(start)
except ValueError:
    print("I said, choose a whole number!")

