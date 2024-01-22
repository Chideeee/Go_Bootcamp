number = int(input("Enter the number to evaluate \n"))


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz_Buzz"
    elif number % 5 == 0:
        return "Fizz"
    elif number % 3 == 0:
        return "Buzz"
    return "Number not divisible by 3 or 5"


evaluated_number = fizz_buzz(number)
print(evaluated_number)
