number = int(input())
list_of_numbers = []
while number != 55:
    list_of_numbers.append(number)
    number = int(input())
print(len(list_of_numbers))
print(sum(list_of_numbers))
print(round(sum(list_of_numbers) / len(list_of_numbers)))
