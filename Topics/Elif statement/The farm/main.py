money = int(input())

if money < 23:
    print('None')
elif money < 678:
    num = money // 23
    if num > 1:
        print(f"{num} chickens")
    else:
        print('1 chicken')
elif money < 1296:
    num = money // 678
    if num > 1:
        print(f"{num} goats")
    else:
        print('1 goat')
elif money < 3848:
    num = money // 1296
    if num > 1:
        print(f"{num} pigs")
    else:
        print('1 pig')
elif money < 6769:
    num = money // 3848
    if num > 1:
        print(f"{num} cows")
    else:
        print('1 cow')
else:
    num = money // 6769
    print(f"{num} sheep")
