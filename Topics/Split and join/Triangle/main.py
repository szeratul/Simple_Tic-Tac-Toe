height = int(input())
lower_size = height * 2 - 1

for i in range(height):
    row = (2 * i + 1) * "#"
    print(row.center(lower_size))
