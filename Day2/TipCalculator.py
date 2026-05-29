print("Welcome to the tip calculator!")

totalBill = float(input("What's the total bill? "))

percentage = 0
while percentage not in (10,12,15):
    percentage = int(input("How much percentage would like to tip?\n10, 12, 15\n"))


people = int(input("How many people to split the bill? "))

price = totalBill * (percentage/100 + 1) / people

print(f"Each person should pay: {price:.2f}")