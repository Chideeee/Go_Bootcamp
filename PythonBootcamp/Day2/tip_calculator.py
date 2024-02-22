print("Welcome to the tip calculator. \n")
# Enter the Initial Bill from provided by the Cashier
Total_bill = float(input("What was the total bill? $"))
# Enter the tip percentage you desire to give to the cashier from the options
Tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 0r 15? "))
# Enter the number of people that will share the overall bill
People_count = int(input("How many people to split the bill? "))
# Performs the Tip calculation based on the customer accepted Tip percentage
Tip = (Tip_percentage/100) * Total_bill
# Calculates the Overall Bill which includes the tip amount
Overall_bill = Total_bill + Tip
# Splits the Total bill among the number of persons paying the bill
Amount_per_person = Overall_bill/People_count
# Rounds the figure to a 2 Decimal place
#Rounded_Amount = round(Amount_per_person, 2)
# Displays the amount payable by each of the persons
Rounded_Amount = "{:.2f}".format(Amount_per_person)
print(f"Each person should pay: ${Rounded_Amount}")