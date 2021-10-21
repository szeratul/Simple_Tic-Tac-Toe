user_string = input()

i = 0
for letter in user_string:
    if not letter.islower():
        if i != 0:
            print('_', end="")
        print(letter.lower(), end="")
    else:
        print(letter, end="")
    i += 1
print("")
