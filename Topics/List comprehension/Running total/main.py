input_numbers = [int(num) for num in input()]

next_element = 0
new_list = []
for i in range(len(input_numbers)):
    next_element += input_numbers[i]
    new_list.append(next_element)
print(new_list)
