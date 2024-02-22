# A Python program that picks customer's name at random
# from a list and chose who pays the bills for the food
# eaten in a restaurant by a group of customers who came in together

import random

customers = input("Enter the names of customers you wish to choose from: \n").lower()
customers_list = customers.split(", ")
customers_count = len(customers_list)
print(
    f"The names of the customers are {customers_list} and they are {customers_count} in number"
)
user_to_pay = random.choice(customers_list)
print(f"The User to Pay for the Meal today is {user_to_pay}. Thank you {user_to_pay} ")
