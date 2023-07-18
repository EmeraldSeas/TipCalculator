print("Welcome to the tip calculator.")  # print welcome message
totalBill = float(input("What was the total bill? $"))  # accept total bill as float
paySplit = int(input("How many people to split the bill? "))  # accept number of people paying as int
tip = round((totalBill / paySplit) * .20, 2)  # calculate 20% tip based on number of people tipping
print("Each person should tip: $" + str(tip)) # display tip
