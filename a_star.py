import random

class PuzzleNode:
    def __init__(self, puzzle, action, parent=None):
        self.puzzle = puzzle
        self.action = action
        self.parent = parent
        self.g_cost = 0 if parent is None else parent.g_cost + 1
        self.h_cost = self.heuristic(puzzle)
        self.f_cost = self.g_cost + self.h_cost

    @staticmethod
    def heuristic(puzzle):
        distance = 0
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] != ' ':
                    target_i = (int(puzzle[i][j]) - 1) // 3
                    target_j = (int(puzzle[i][j]) - 1) % 3
                    distance += abs(i - target_i) + abs(j - target_j)
        return distance


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

        if path == 'up' and row < 2:
            puzzle_[row][col], puzzle_[row + 1][col] = puzzle_[row + 1][col], puzzle_[row][col]

        if path == 'down' and row > 0:
            puzzle_[row][col], puzzle_[row - 1][col] = puzzle_[row - 1][col], puzzle_[row][col]

        if path == 'left' and col < 2:
            puzzle_[row][col], puzzle_[row][col + 1] = puzzle_[row][col + 1], puzzle_[row][col]

        if path == 'right' and col > 0:
            puzzle_[row][col], puzzle_[row][col - 1] = puzzle_[row][col - 1], puzzle_[row][col]

    return puzzle_

def a_star(start_node):
    explored = set()
    frontier = [start_node]

    while frontier:
        current_node = frontier.pop(0)

        if tuple(map(tuple, current_node.puzzle)) in explored:
            continue

        explored.add(tuple(map(tuple, current_node.puzzle)))

        if current_node.puzzle == result:
            actions = []
            while current_node.parent:
                actions.append(current_node.action)
                current_node = current_node.parent
            actions.reverse()
            for action in actions:
                print(action)
            return

        row, col = find_empty(current_node.puzzle)

        if row < 2:
            node_up = PuzzleNode([row[:] for row in current_node.puzzle], 'up', current_node)
            node_up.puzzle[row][col], node_up.puzzle[row + 1][col] = node_up.puzzle[row + 1][col], node_up.puzzle[row][col]
            frontier.append(node_up)

        if row > 0:
            node_down = PuzzleNode([row[:] for row in current_node.puzzle], 'down', current_node)
            node_down.puzzle[row][col], node_down.puzzle[row - 1][col] = node_down.puzzle[row - 1][col], node_down.puzzle[row][col]
            frontier.append(node_down)

        if col < 2:
            node_left = PuzzleNode([row[:] for row in current_node.puzzle], 'left', current_node)
            node_left.puzzle[row][col], node_left.puzzle[row][col + 1] = node_left.puzzle[row][col + 1], node_left.puzzle[row][col]
            frontier.append(node_left)

        if col > 0:
            node_right = PuzzleNode([row[:] for row in current_node.puzzle], 'right', current_node)
            node_right.puzzle[row][col], node_right.puzzle[row][col - 1] = node_right.puzzle[row][col - 1], node_right.puzzle[row][col]
            frontier.append(node_right)

    
shuffled_start = shuffle(start)
a_star(PuzzleNode(shuffled_start, ''))