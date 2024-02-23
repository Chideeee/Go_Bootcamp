# A program that will calculate the sum of all even number between 1 and 100

total = 0
numbers = range(1, 101)
for number in numbers:
    if number % 2 == 0:
        total += number
print(total)
