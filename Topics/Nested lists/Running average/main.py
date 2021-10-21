input_list = [int(num) for num in input()]
new_list = []

for i in range(len(input_list) - 1):
    new_list.append((input_list[i] + input_list[i + 1]) / 2)
print(new_list)
