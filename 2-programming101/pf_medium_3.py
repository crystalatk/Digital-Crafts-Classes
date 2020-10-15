coin = 0
request = "yes"

while request.upper() == "YES":
    print(f"You have {coin} coins.")
    request = input("Do you want another coin? yes or no\n")
    if request.upper() != "YES" and request.upper() != "NO":
        request = input("Looks like you had a woopsie! Please answer yes or no.\n")
    coin += 1
print("Bye")