def is_attacking(queens, row1, col1, row2, col2):
  """
  Checks if two queens are attacking each other (diagonals or same row/column)
  """
  # Same column or diagonals
  return col1 == col2 or abs(row1 - row2) == abs(col1 - col2)

def calculate_attacks(queens):
  """
  Calculates the number of attacks between all queens on the board
  """
  attacks = 0
  for i in range(len(queens)):
    for j in range(i + 1, len(queens)):
      if is_attacking(queens, i, queens[i], j, queens[j]):
        attacks += 1
  return attacks

def get_random_neighbor(queens):
  """
  Generates a random neighbor state by moving a single queen
  """
  new_queens = queens.copy()
  # Select a random queen and a random row for her to move to
  queen_to_move = random.randint(0, len(queens) - 1)
  new_row = random.randint(0, len(queens) - 1)
  new_queens[queen_to_move] = new_row
  return new_queens

def hill_climbing(max_iterations=1000):
  """
  Solves the 8-Queens problem using Hill Climbing algorithm
  """
  queens = [random.randint(0, 7) for _ in range(8)]  # Random initial state
  current_attacks = calculate_attacks(queens)
  for _ in range(max_iterations):
    new_queens = get_random_neighbor(queens)
    new_attacks = calculate_attacks(new_queens)

    # If the new state has less attacks, move to it
    if new_attacks < current_attacks:
      queens = new_queens
      current_attacks = new_attacks

    # If no attacks, we found a solution
    if current_attacks == 0:
      return queens
  
  # No solution found after max iterations
  return None

def print_board(queens):
  """
  Prints the chessboard with queens represented by "Q"
  """
  for row in range(8):
    for col in range(8):
      if queens[col] == row:
        print("Q", end=" ")
      else:
        print(".", end=" ")
    print()

if __name__ == "__main__":
  import random
  solution = hill_climbing()
  if solution:
    print("Solution found:")
    print_board(solution)
  else:
    print("No solution found after max iterations")
