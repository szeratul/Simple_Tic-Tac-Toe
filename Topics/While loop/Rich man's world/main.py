deposit = float(input())

year = 0
while deposit < 700000.0:
    deposit += deposit * 0.071
    year += 1
print(year)
