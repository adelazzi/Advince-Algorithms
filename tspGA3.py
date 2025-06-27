import numpy as np
 
graph2 = [[0, 4, 3, 2],
         [4, 0, 1, 2],
         [3, 1, 0, 5],
         [1, 2, 5, 0] ]

graph3 = [[ 0, 5, 1, 3, 2],
         [ 5, 0, 2, 3, 1],
         [ 1, 2, 0, 2, 3],
         [ 3, 3, 2, 0, 4],
         [ 2, 1, 3, 4, 0] ]

graph = [
[0,29,82,46,68,52,72,42,51,55,29,74,23,72,46],
[29,0,55,46,42,43,43,23,23,31,41,51,11,52,21],
[82,55,0,68,46,55,23,43,41,29,79,21,64,31,51],
[46,46,68,0,82,15,72,31,62,42,21,51,51,43,64],
[68,42,46,8,0,74,23,52,21,46,82,58,46,65,23],
[52,43,55,15,74,0,61,23,55,31,33,37,51,29,59],
[72,43,23,72,23,61,0,42,23,31,77,37,51,46,33],
[42,23,43,31,52,23,42,0,33,15,37,33,33,31,37],
[51,23,41,62,21,55,23,33,0,29,62,46,29,51,11],
[55,31,29,42,46,31,31,15,29,0,51,21,41,23,37],
[29,41,79,21,82,33,77,37,62,51,0,65,42,59,61],
[74,51,21,51,58,37,37,33,46,21,65,0,61,11,55],
[23,11,64,51,46,51,51,33,29,41,42,61,0,62,23],
[72,52,31,43,65,29,46,31,51,23,59,11,62,0,59],
[46,21,51,64,23,59,33,37,11,37,61,55,23,59,0] ]


def compute_fitness(G, s):
    """Calculate the total path length for a solution"""
    total_distance = 0
    for i in range(len(s) - 1):
        total_distance += G[s[i]][s[i+1]]
    total_distance += G[s[-1]][s[0]]  # Return to starting point
    return total_distance

def do_crossover(s1, s2, crossover_point):
    """Perform crossover between two parent solutions"""
    s1, s2 = s1.copy(), s2.copy()
    
    # Create first child
    c1 = s2.copy()
    for i in range(crossover_point, len(s1)): 
        c1.remove(s1[i])
    for i in range(crossover_point, len(s1)): 
        c1.append(s1[i])
    
    # Create second child
    c2 = s1.copy()
    for i in range(crossover_point, len(s2)): 
        c2.remove(s2[i])
    for i in range(crossover_point, len(s2)): 
        c2.append(s2[i])
        
    return (c1, c2)
         
def do_mutation(s, pos1, pos2):
    """Reverse the segment between pos1 and pos2"""
    i, j = min(pos1, pos2), max(pos1, pos2)
    s_mutated = s.copy()
    while i < j:
        s_mutated[i], s_mutated[j] = s_mutated[j], s_mutated[i]
        i += 1
        j -= 1
    return s_mutated

def evaluate(G, population, k):
    """Sort population by fitness and keep the best k individuals"""
    return sorted(population, key=lambda s: compute_fitness(G, s))[:k]

def generate_initial_population(graph, population_size):
    """Generate initial random population"""
    population = []
    path = list(range(len(graph)))
    
    while len(population) < population_size:
        path_candidate = path.copy()
        np.random.shuffle(path_candidate)
        if path_candidate not in population:
            population.append(path_candidate)    
    return population

def create_offspring(population, mutation_prob, population_size):
    """Create the next generation through crossover and mutation"""
    next_gen = []
    num_cities = len(population[0])
    
    for _ in range(round(population_size/2)):
        # Select random parents
        parent1_idx = np.random.randint(0, len(population))
        parent2_idx = np.random.randint(0, len(population))
        
        # Perform crossover
        crossover_point = np.random.randint(0, num_cities)
        child1, child2 = do_crossover(population[parent1_idx], population[parent2_idx], crossover_point)
        
        # Possibly mutate first child
        if np.random.rand() < mutation_prob:
            pos1 = np.random.randint(0, num_cities)
            pos2 = np.random.randint(0, num_cities)
            child1 = do_mutation(child1, pos1, pos2)
            
        # Possibly mutate second child
        if np.random.rand() < mutation_prob:
            pos1 = np.random.randint(0, num_cities)
            pos2 = np.random.randint(0, num_cities)
            child2 = do_mutation(child2, pos1, pos2)
        
        # Add children to next generation
        next_gen.append(child1)
        next_gen.append(child2)
          
    return next_gen

def get_best_solution(population, graph):
    """Return the best solution and its fitness in the population"""
    best_solution = min(population, key=lambda s: compute_fitness(graph, s))
    best_fitness = compute_fitness(graph, best_solution)
    return best_solution, best_fitness

# Algorithm parameters
MUTATION_PROBABILITY = 0.5
NUM_GENERATIONS = 400 
POPULATION_SIZE = 20 
   
# Initialize population
population = generate_initial_population(graph, POPULATION_SIZE)

# Track best solution
best_solution = None
best_distance = float('inf')

# Main genetic algorithm loop
for generation in range(NUM_GENERATIONS):
    # Evaluate and select best individuals
    population = evaluate(graph, population, POPULATION_SIZE)
    
    # Create next generation
    offspring = create_offspring(population, MUTATION_PROBABILITY, POPULATION_SIZE)
    
    # Replace population with offspring
    population = offspring[:POPULATION_SIZE]
    
    # Update best solution if improved
    current_best, current_distance = get_best_solution(population, graph)
    if current_distance < best_distance:
        best_distance = current_distance
        best_solution = current_best

print(f"Best path: {best_solution}")
print(f"Distance: {best_distance}")
