import random
import time
from threading import Thread

seconds = 10


def timer():
    global seconds
    while seconds > 0:
        time.sleep(1)
        seconds -= 1


def print_pattern(pattern, pattern_name):
    print("-------------------------------------")
    print(f"PATTERN {pattern_name}")
    for row in pattern:
        print(f'{row}\n')
    print("-------------------------------------")


puzzle = [
    [],
    [],
    [],
]

result = [
    [],
    [],
    [],
]

pattern1 = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', ' '],
]

pattern2 = [
    ['1', '2', '3'],
    ['8', ' ', '4'],
    ['7', '6', '5'],
]

pattern3 = [
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', ' '],
]

print_pattern(pattern1, "A")

print_pattern(pattern2, "B")

print_pattern(pattern3, "C")

puzzle_shape = input("select a pattern: ")

if puzzle_shape.lower() == "a":
    puzzle = pattern1
    result = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', ' '],
    ]

elif puzzle_shape.lower() == "b":
    puzzle = pattern2
    result = [
        ['1', '2', '3'],
        ['8', ' ', '4'],
        ['7', '6', '5'],
    ]

elif puzzle_shape.lower() == "c":
    puzzle = pattern3
    result = [
        ['1', '4', '7'],
        ['2', '5', '8'],
        ['3', '6', ' '],
    ]

else:
    print("please enter a valid pattern")


count = 30


def print_puzzle(puzzle__, sec):
    print("--------------------------------------------------")
    for row in puzzle__:
        print(f'{row}\n')
    print("--------------------------------------------------")
    print(f'moves: {count}')
    print(f'time: {sec}')


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

print("\n game is started \n")

print_puzzle(puzzle, seconds)


def game():
    global seconds
    global count
    while True:
        if seconds == 0:
            print("game over")
            break
        else:
            move = input("enter direction: ")

        if count == 0:
            print("you loss")
            break

        if puzzle == result:
            print("you solved the puzzle!!!")
            break

        if move == "left":
            x, y = find_empty(puzzle)

            if y < 2:
                puzzle[x][y], puzzle[x][y + 1] = puzzle[x][y + 1], puzzle[x][y]
                count = count - 1

                print_puzzle(puzzle, seconds)
                continue
            else:
                print("this move is not legal")
                continue

        if move == "right":
            x, y = find_empty(puzzle)

            if y > 0:
                puzzle[x][y], puzzle[x][y - 1] = puzzle[x][y - 1], puzzle[x][y]
                count = count - 1

                print_puzzle(puzzle, seconds)
                continue
            else:
                print("this move is not legal")
                continue

        if move == "up":
            x, y = find_empty(puzzle)

            if x < 2:
                puzzle[x + 1][y], puzzle[x][y] = puzzle[x][y], puzzle[x + 1][y]
                count = count - 1

                print_puzzle(puzzle, seconds)
                continue

            else:
                print("this move is not legal")
                continue

        if move == "down":
            x, y = find_empty(puzzle)

            if x > 0:
                puzzle[x - 1][y], puzzle[x][y] = puzzle[x][y], puzzle[x - 1][y]
                count = count - 1

                print_puzzle(puzzle, seconds)
                continue
            else:
                print("this move is not legal")
                continue

        if move == "exit":
            break


time_thread = Thread(target=timer)
game_thread = Thread(target=game)

time_thread.start()
game_thread.start()


time_thread.join()
game_thread.join()
