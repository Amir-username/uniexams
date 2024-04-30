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

shuffle(start)

frontier = [PuzzleNode(start, '')]
visited = set()

while frontier:
    current_node = frontier.pop(0)

    if current_node.puzzle == result:
        break

    if tuple(map(tuple, current_node.puzzle)) in visited:
        continue

    visited.add(tuple(map(tuple, current_node.puzzle)))

    row, col = find_empty(current_node.puzzle)

    if row < 2:
        node_up = PuzzleNode(current_node.puzzle[:], 'up')
        node_up.puzzle[row][col], node_up.puzzle[row + 1][col] = node_up.puzzle[row + 1][col], node_up.puzzle[row][col]
        frontier.append(node_up)

    if row > 0:
        node_down = PuzzleNode(current_node.puzzle[:], 'down')
        node_down.puzzle[row][col], node_down.puzzle[row - 1][col] = node_down.puzzle[row - 1][col], node_down.puzzle[row][col]
        frontier.append(node_down)

    if col < 2:
        node_left = PuzzleNode(current_node.puzzle[:], 'left')
        node_left.puzzle[row][col], node_left.puzzle[row][col + 1] = node_left.puzzle[row][col + 1], node_left.puzzle[row][col]
        frontier.append(node_left)

    if col > 0:
        node_right = PuzzleNode(current_node.puzzle[:], 'right')
        node_right.puzzle[row][col], node_right.puzzle[row][col - 1] = node_right.puzzle[row][col - 1], node_right.puzzle[row][col]
        frontier.append(node_right)

    print(current_node.action)

for f in frontier:
    print(f.action)