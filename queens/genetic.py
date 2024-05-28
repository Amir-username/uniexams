import random

def calculate_fitness(queens):
    attacks = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens, i, queens[i], j, queens[j]):
                attacks += 1
    return 28 - attacks

def is_attacking(queens, row1, col1, row2, col2):
    return col1 == col2 or abs(row1 - row2) == abs(col1 - col2)

def mutate(queens):
    new_queens = queens.copy()
    idx1, idx2 = random.sample(range(8), 2)
    new_queens[idx1], new_queens[idx2] = new_queens[idx2], new_queens[idx1]
    return new_queens

def crossover(parent1, parent2):
    idx = random.randint(0, 7)
    child1 = parent1[:idx] + parent2[idx:]
    child2 = parent2[:idx] + parent1[idx:]
    return child1, child2

def genetic_algorithm(population_size=100, max_generations=1000):
    population = [random.sample(range(8), 8) for _ in range(population_size)]

    for generation in range(max_generations):
        fitness_scores = [calculate_fitness(individual) for individual in population]
        best_idx = fitness_scores.index(max(fitness_scores))

        if fitness_scores[best_idx] == 28:
            return population[best_idx]

        selected = [population[i] for i in sorted(range(population_size), key=lambda x: fitness_scores[x], reverse=True)[:population_size // 2]]

        new_population = selected.copy()  
        for i in range(population_size // 2):
            parent1, parent2 = selected[i], selected[(i + 1) % (population_size // 2)]
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])

        population = new_population

    return None

solution = genetic_algorithm()
if solution:
    print("Solution found:")
    for row in range(8):
        for col in range(8):
            if solution[col] == row:
                print(u"\U0001F451", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution found")