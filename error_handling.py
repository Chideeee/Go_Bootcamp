try:
    age = int(input("Age: "))
except (ValueError, ZeroDivisionError):
    print("Please enter a number for your age.")
print(age)
