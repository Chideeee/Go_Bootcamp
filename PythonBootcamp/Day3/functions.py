# A function argument are values which are executed inside a function.
number = "111"

# finding the length of an object
print(len(number))  # 3

# converting types
integer = int(number)  # 111
float_number = float(number)  # 111.0

# adding numbers
my_sum = sum((integer, float_number))

print(my_sum)  # 222.0
print(round(my_sum))  # 222

# finding the minimum and the maximum
integer = 3
float_number = 5.4
my_sum = sum((integer, float_number))

print(min(integer, float_number))  # 3
print(type(max(integer, float_number, my_sum)))  # <class 'float'>