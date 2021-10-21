vowels = "aeiou"
line = input()

for c in line:
    if not c.isalpha():
        break
    if c in vowels:
        print("vowel")
    else:
        print("consonant")

