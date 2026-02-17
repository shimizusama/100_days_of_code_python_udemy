print("Welcome to the tip calculator")
total = float(input("What was the total bill? $ "))
tip = int(input("How much would you like to give? 10, 12, or 15? $ "))
people = int(input("How many people to split the bill? "))


if tip == 10:
    final_tip = (total + (total * 0.10)) /  people
    print(f"Each person should pay: ${final_tip:.2f}")
elif tip == 12:
    final_tip = (total + (total * 0.12)) / people
    print(f"Each person should pay ${final_tip:.2f}")
elif tip == 15:
    final_tip = (total + (total * 0.15)) / people
    print(f"Each person should pay ${final_tip:.2f}")
