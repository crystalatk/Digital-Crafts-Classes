try:
    bill = float(input("How much was your total bill?\n$ "))
    service = input("How was your serivce today?\nPlease choose: Good, Fair, or Bad\n")
    service_u = service.upper()
    if service_u == "GOOD":
        tip_multiplier = .2
    elif service_u == "FAIR":
        tip_multiplier = .15
    elif service_u == "BAD":
        tip_multiplier = .1
    else:
        print("Please choose the level of service using the terms: Good, Fair, or Bad.\nThanks!")
        exit()
    parts = int(input("How many ways would you like to split the bill?\n"))
    tip_f = bill * tip_multiplier
    tip = "${:,.2f}".format(tip_f)
    total = "${:,.2f}".format(bill + tip_f)
    total_pp = "${:,.2f}".format((bill + tip_f)/parts)
    print(f"Tip amount: {tip}")
    print(f"Total Amount: {total}")
    print(f"Amount per person: {total_pp}")
except ValueError:
    print("Your bill and ways to split it should be a number.")