number_of_lines = int(input())

match_list = [input().split(' ') for _ in range(number_of_lines)]
i = 0
win_list = [data[0] for data in match_list if "win" in data]
print(win_list)
print(len(win_list))


