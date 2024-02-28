import random

puzzle = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', ' '],
]

result = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', ' '],
]


def print_puzzle(puzzle__):
    print("--------------------------------------------------")
    for row in puzzle__:
        print(f'{row}\n')
    print("--------------------------------------------------")


def find_empty(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == " ":
                return i, j


def shuffle(puzzle_):
    for k in range(100):
        row, col = find_empty(puzzle_)
        path = random.choice(['up', 'down', 'left', 'right'])

        if path == 'up':
            if row < 2:
                puzzle_[row][col], puzzle_[row + 1][col] = puzzle_[row + 1][col], puzzle_[row][col]

        if path == 'down':
            if row > 0:
                puzzle_[row][col], puzzle_[row - 1][col] = puzzle_[row - 1][col], puzzle_[row][col]

        if path == 'left':
            if col < 2:
                puzzle_[row][col], puzzle_[row][col + 1] = puzzle_[row][col + 1], puzzle_[row][col]

        if path == 'right':
            if col > 0:
                puzzle_[row][col], puzzle_[row][col - 1] = puzzle_[row][col - 1], puzzle_[row][col]


shuffle(puzzle)

print_puzzle(puzzle)

while True:
    if puzzle == result:
        print("you solved the puzzle!!!")
        break

    move = input("enter direction: ")

    if move == "left":
        x, y = find_empty(puzzle)

        if y < 2:
            puzzle[x][y], puzzle[x][y + 1] = puzzle[x][y + 1], puzzle[x][y]

            print_puzzle(puzzle)
            continue
        else:
            print("this move is not legal")
            continue

    if move == "right":
        x, y = find_empty(puzzle)

        if y > 0:
            puzzle[x][y], puzzle[x][y - 1] = puzzle[x][y - 1], puzzle[x][y]

            print_puzzle(puzzle)
            continue
        else:
            print("this move is not legal")
            continue

    if move == "up":
        x, y = find_empty(puzzle)

        if x < 2:
            puzzle[x + 1][y], puzzle[x][y] = puzzle[x][y], puzzle[x + 1][y]

            print_puzzle(puzzle)
            continue

        else:
            print("this move is not legal")
            continue

    if move == "down":
        x, y = find_empty(puzzle)

        if x > 0:
            puzzle[x - 1][y], puzzle[x][y] = puzzle[x][y], puzzle[x - 1][y]

            print_puzzle(puzzle)
            continue
        else:
            print("this move is not legal")
            continue

    if move == "exit":
        break
