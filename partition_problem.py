import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def partition_problem(x):
    """
    Solve the partition problem: divide array x into two subsets A and B
    such that the difference between their sums is minimized.
    """
    # Function to calculate the sum of subsets A and B
    def sum_A_B(chromosome):
        A_sum = sum(x[i] for i in range(len(x)) if chromosome[i] == 1)
        B_sum = sum(x[i] for i in range(len(x)) if chromosome[i] == 0)
        return A_sum, B_sum
    
    # Fitness function to minimize (absolute difference between the sums)
    def fitness(chromosome):
        A_sum, B_sum = sum_A_B(chromosome)
        return abs(A_sum - B_sum)
    
    # GA configuration
    varbound = np.array([[0, 1]] * len(x))  # Each element can be 0 (B) or 1 (A)
    model = ga(
        function=fitness,
        dimension=len(x),
        variable_type='int',
        variable_boundaries=varbound
    )
    
    # Run the genetic algorithm
    model.run()
    
    # Extract results
    best_solution = model.output_dict['variable']
    A = [x[i] for i in range(len(x)) if best_solution[i] == 1]
    B = [x[i] for i in range(len(x)) if best_solution[i] == 0]
    
    return A, B

# Input vector
x = np.array([4, 5, 3, 6, 7, 5, 5, 5, 5, 7, 4, 1, 8])

# Solve the problem
A, B = partition_problem(x)

# Display results
print("Solution optimale trouvée:")
print(f"A = {A}")
print(f"B = {B}")
print(f"Somme de A = {sum(A)}")
print(f"Somme de B = {sum(B)}")
print(f"Différence = {abs(sum(A) - sum(B))}")


