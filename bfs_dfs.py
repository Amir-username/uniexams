import random


class PuzzleNode:
    def __init__(self, puzzle, action, parent=None):
        self.puzzle = puzzle
        self.action = action
        self.parent = parent


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


def bfs(start):
    frontier = [PuzzleNode(start, '')]

    visited = set()

    actions = []

    while frontier:
        current_node = frontier.pop(0)

        if current_node.puzzle == result:
            break

        if tuple(map(tuple, current_node.puzzle)) in visited:
            continue

        visited.add(tuple(map(tuple, current_node.puzzle)))

        actions.append(current_node.action)

        row, col = find_empty(current_node.puzzle)

        if row < 2:
            node_up = PuzzleNode(current_node.puzzle[:], 'up')
            node_up.puzzle[row][col], node_up.puzzle[row +
                                                     1][col] = node_up.puzzle[row + 1][col], node_up.puzzle[row][col]
            frontier.append(node_up)

        if row > 0:
            node_down = PuzzleNode(current_node.puzzle[:], 'down')
            node_down.puzzle[row][col], node_down.puzzle[row -
                                                         1][col] = node_down.puzzle[row - 1][col], node_down.puzzle[row][col]
            frontier.append(node_down)

        if col < 2:
            node_left = PuzzleNode(current_node.puzzle[:], 'left')
            node_left.puzzle[row][col], node_left.puzzle[row][col +
                                                              1] = node_left.puzzle[row][col + 1], node_left.puzzle[row][col]
            frontier.append(node_left)

        if col > 0:
            node_right = PuzzleNode(current_node.puzzle[:], 'right')
            node_right.puzzle[row][col], node_right.puzzle[row][col -
                                                                1] = node_right.puzzle[row][col - 1], node_right.puzzle[row][col]
            frontier.append(node_right)


    return len(actions)


def dfs(start):
    visited = set()
    stack = [PuzzleNode(start, '')]
    actions = []


    while stack:
        current_node = stack.pop()

        if tuple(map(tuple, current_node.puzzle)) in visited:
            continue

        visited.add(tuple(map(tuple, current_node.puzzle)))

        

        if current_node.puzzle == result:
            while current_node.parent:
                actions.append(current_node.action)
                current_node = current_node.parent
            actions.reverse()
            
            break

        row, col = find_empty(current_node.puzzle)

        if row < 2:
            node_up = PuzzleNode(
                [row[:] for row in current_node.puzzle], 'up', current_node)
            node_up.puzzle[row][col], node_up.puzzle[row +
                                                     1][col] = node_up.puzzle[row + 1][col], node_up.puzzle[row][col]
            stack.append(node_up)

        if row > 0:
            node_down = PuzzleNode(
                [row[:] for row in current_node.puzzle], 'down', current_node)
            node_down.puzzle[row][col], node_down.puzzle[row -
                                                         1][col] = node_down.puzzle[row - 1][col], node_down.puzzle[row][col]
            stack.append(node_down)

        if col < 2:
            node_left = PuzzleNode(
                [row[:] for row in current_node.puzzle], 'left', current_node)
            node_left.puzzle[row][col], node_left.puzzle[row][col +
                                                              1] = node_left.puzzle[row][col + 1], node_left.puzzle[row][col]
            stack.append(node_left)

        if col > 0:
            node_right = PuzzleNode(
                [row[:] for row in current_node.puzzle], 'right', current_node)
            node_right.puzzle[row][col], node_right.puzzle[row][col -
                                                                1] = node_right.puzzle[row][col - 1], node_right.puzzle[row][col]
            stack.append(node_right)

    return len(actions)




bfs_actions = bfs(start)

dfs_actions = dfs(start)

print(f"bfs path: {bfs_actions}")
print(f"dfs path: {dfs_actions}")
