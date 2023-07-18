print("Welcome to the tip calculator.")  # print welcome message
totalBill = float(input("What was the total bill? $"))  # accept total bill as float
paySplit = int(input("How many people to split the bill?\n"))  # accept number of people paying as int
tipPercentage = float(int(input("What percentage do you want to tip? 12, 15, or 20\n")) / 100)
tip = round((totalBill / paySplit) * tipPercentage, 2)  # calculate 20% tip based on number of people tipping
print(f"Each person should tip ${tip}")  # display tip
