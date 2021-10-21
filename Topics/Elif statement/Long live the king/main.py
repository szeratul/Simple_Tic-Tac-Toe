position_1 = int(input())
position_2 = int(input())
n = 0

if position_1 == 1 or position_1 == 8:
    n += 1
    if position_2 == 1 or position_2 == 8:
        n += 2
    else:
        n += 4
else:
    n += 2
    if position_2 == 1 or position_2 == 8:
        n += 3
    else:
        n += 6
print(n)
