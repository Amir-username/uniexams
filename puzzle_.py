import random


class PuzzleNode:
    def __init__(self, puzzle, action):
        self.puzzle = puzzle
        self.action = action


result = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', ' '],
]


start = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', ' '],
]


def print_pattern(pattern):
    print("-------------------------------------")
    for row in pattern:
        print(f'{row}\n')


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
                puzzle_[row][col], puzzle_[
                    row + 1][col] = puzzle_[row + 1][col], puzzle_[row][col]

        if path == 'down':
            if row > 0:
                puzzle_[row][col], puzzle_[
                    row - 1][col] = puzzle_[row - 1][col], puzzle_[row][col]

        if path == 'left':
            if col < 2:
                puzzle_[row][col], puzzle_[row][col +
                                                1] = puzzle_[row][col + 1], puzzle_[row][col]

        if path == 'right':
            if col > 0:
                puzzle_[row][col], puzzle_[row][col -
                                                1] = puzzle_[row][col - 1], puzzle_[row][col]


shuffle(start)

node = PuzzleNode(start, '')

frontier = []

i = 0

while True:
    if node.puzzle == result:
        break

    valid_actions = []

    row, col = find_empty(start)

    if row < 2:
        valid_actions.append('up')

    if row > 0:
        valid_actions.append('down')

    if col < 2:
        valid_actions.append('left')

    if col > 0:
        valid_actions.append('right')

    if 'up' in valid_actions:
        node_up = node
        node_up.puzzle[row][col], node_up.puzzle[
            row + 1][col] = node_up.puzzle[row + 1][col], node_up.puzzle[row][col]
        node_up.action = 'up'

        frontier.append(node_up)

    if 'down' in valid_actions:
        node_down = node
        node_down.puzzle[row][col], node_down.puzzle[
            row - 1][col] = node_down.puzzle[row - 1][col], node_down.puzzle[row][col]
        node_down.action = 'down'

        frontier.append(node_down)

    if 'left' in valid_actions:
        node_left = node
        node_left.puzzle[row][col], node_left.puzzle[row][col +
                                    1] = node_left.puzzle[row][col + 1], node_left.puzzle[row][col]
        node_left.action = 'left'

        frontier.append(node_left)

    if 'right' in valid_actions:
        node_right = node
        node_right.puzzle[row][col], node_right.puzzle[row][col -
                                    1] = node_right.puzzle[row][col - 1], node_right.puzzle[row][col]
        node_right.action = 'right'

        frontier.append(node_right)

    new_node = PuzzleNode(frontier[i].puzzle, frontier[i].action)
    i += 1


for f in frontier:
    print(f.action)