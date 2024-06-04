import random


def is_attacking(queens, row1, col1, row2, col2):
    return col1 == col2 or abs(row1 - row2) == abs(col1 - col2)


def calculate_attacks(queens):
    attacks = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens, i, queens[i], j, queens[j]):
                attacks += 1
    return attacks


def get_all_neighbors(queens):
    neighbors = []
    for queen_idx in range(len(queens)):
        for new_row in range(8):
            if queens[queen_idx] != new_row:
                new_queens = queens.copy()
                new_queens[queen_idx] = new_row
                neighbors.append(new_queens)
    return neighbors


def local_beam_search(k=5, max_iterations=100):
    beam = [[random.randint(0, 7) for _ in range(8)] for _ in range(k)]

    for _ in range(max_iterations):
        scores = [calculate_attacks(state) for state in beam]

        sorted_beam = sorted(zip(beam, scores))
        beam, scores = zip(*sorted_beam)

        if scores[0] == 0:
            return beam[0]

        new_beam = []
        for state in beam[:k]:
            new_beam.extend(get_all_neighbors(state))

        new_beam = sorted(new_beam, key=calculate_attacks)[:k]
        beam = new_beam

    return None


def print_board(queens):
    for row in range(8):
        for col in range(8):
            if queens[col] == row:
                print(u"\U0001F451", end=" ")
            else:
                print(". ", end=" ")
        print()


solution = local_beam_search()
if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution found")
