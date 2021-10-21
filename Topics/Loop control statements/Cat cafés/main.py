cafes = {}
while True:
    line = input().split()
    if line[0] == "MEOW":
        break
    cafes[line[0]] = int(line[1])

print(max(cafes, key=cafes.get))
