print("Welcome to the tip calculator")
total_cost = float(input("How much is the total bill?"))
tip_percent = int(input("What tip percentage would you like to give?"))
number_payers = int(input("How many people are splitting the bill?"))

bill = round(total_cost, 2)
tip_total = 1 + (tip_percent / 100)

individual_total = (bill * tip_total) / number_payers

rounded_individual = round(individual_total, 2)

print(f"Each person should pay: ${rounded_individual}")