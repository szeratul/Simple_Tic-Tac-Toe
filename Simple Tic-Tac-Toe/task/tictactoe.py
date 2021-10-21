def check_rows(cells):
    r = 0
    c = 0
    symbol_r = ''
    symbol_c = ''
    for i in range(3):
        if cells[3 * i] == cells[3 * i + 1] == cells[3 * i + 2] != '_':
            r += 1
            symbol_r = cells[3 * i]
        elif cells[i] == cells[i + 3] == cells[i + 6] != '_':
            c += 1
            symbol_c = cells[i]
    return [(r, symbol_r), (c, symbol_c)]


def check_diagonals(cells):
    if cells[0] == cells[4] == cells[8] != '_' or cells[2] == cells[4] == cells[6] != '_':
        return cells[4]
    return None


def check_impossible(cells):
    x = 0
    o = 0
    for c in cells:
        if c == 'X':
            x += 1
        elif c == 'O':
            o += 1
    if abs(x - o) >= 2:
        return True
    result = check_rows(cells)
    if (result[0][0] > 1 and result[0][1] != '_') or (result[1][0] > 1 and result[1][1] != '_'):
        return True
    return False


def print_grid(grid):
    print('---------')
    print('|', grid[0], grid[1], grid[2], '|')
    print('|', grid[3], grid[4], grid[5], '|')
    print('|', grid[6], grid[7], grid[8], '|')
    print('---------')


def check_state(grid):
    if check_impossible(grid):
        print('Impossible')
    else:
        result = check_rows(grid)
        if result[0][0] == 1:
            print(result[0][1], 'wins')
            return True
        elif result[1][0] == 1:
            print(result[1][1], 'wins')
            return True
        elif check_diagonals(grid):
            print(check_diagonals(grid), 'wins')
            return True
        else:
            if '_' not in grid:
                print('Draw')
                return True
            # else:
            #     print('Game not finished')
    return False


def process_coordinates(grid, coordinates, player):
    n_coordinates_checked = 0
    while True:
        for coordinate in coordinates:
            if coordinate.isalpha():
                n_coordinates_checked = 0
                print("You should enter numbers!")
                coordinates = input("Enter the coordinates: ").split()
                break
            elif coordinate.isdigit():
                if int(coordinate) < 1 or int(coordinate) > 3:
                    n_coordinates_checked = 0
                    print("Coordinates should be from 1 to 3!")
                    coordinates = input("Enter the coordinates: ").split()
                    break
                else:
                    n_coordinates_checked += 1
        if n_coordinates_checked == 2:
            position = (int(coordinates[0]) - 1) * 3 + int(coordinates[1]) - 1
            if grid[position] == '_':
                grid[position] = player
                print_grid(grid)
                break
            else:
                n_coordinates_checked = 0
                print("This cell is occupied! Choose another one!")
                coordinates = input("Enter the coordinates: ").split()


input_grid = ['_' for _ in range(9)]
print_grid(input_grid)
i = 0

while not check_state(input_grid):
    input_coordinates = input("Enter the coordinates: ").split()
    process_coordinates(input_grid, input_coordinates, 'X' if i % 2 == 0 else 'O')
    i += 1


