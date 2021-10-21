mean_ = 0
length = 0
while True:
    num = input()
    if num == '.':
        break
    mean_ += int(num)
    length += 1

print(mean_ / length)
