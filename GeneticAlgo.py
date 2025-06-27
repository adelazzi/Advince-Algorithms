# Import necessary packages
from geneticalgorithm import geneticalgorithm as ga
import numpy as np

def define_problem():
    """Define the bus scheduling problem parameters."""
    # Bus capacity limit (29 passengers)
    capacity = 29
    # Number of families
    num_families = 10
    # Revenue per family (1000 DA per person)
    revenue_per_family = [4000, 5000, 3000, 6000, 7000, 5000, 7000, 4000, 6000, 8000]
    # Number of passengers per family
    passengers_per_family = [4, 5, 3, 6, 7, 5, 7, 4, 6, 8]
    # Penalty for exceeding capacity
    penalty_coefficient = 1000
    
    return capacity, num_families, revenue_per_family, passengers_per_family, penalty_coefficient

def fitness_function(x):
    """Calculate the fitness value (negative revenue with penalty if applicable).
    
    Args:
        x: Binary array representing selected families
        
    Returns:
        Negative total revenue (with penalty if capacity is exceeded)
    """
    capacity, _, revenue_per_family, passengers_per_family, penalty_coefficient = define_problem()
    
    total_revenue = 0
    total_passengers = 0
    
    # Calculate total passengers and revenue
    for i in range(len(x)):
        if x[i] == 1:
            total_passengers += passengers_per_family[i]
            total_revenue += revenue_per_family[i]
    
    # Apply penalty if capacity is exceeded
    if total_passengers > capacity:
        total_revenue = 0
        
    # Return negative value for minimization in GA
    return -total_revenue


"""Main function to run the genetic algorithm."""
# Get problem parameters
_, num_families, _, _, _ = define_problem()

# Define the boundaries for each variable (0 or 1 for binary decisions)
boundaries = np.array([[0, 1]] * num_families)

# Create and configure the GA model
model = ga(
    function=fitness_function,     # Fitness function
    dimension=num_families,        # Number of decision variables (families)
    variable_type='bool',          # Type of variables (binary)
    variable_boundaries=boundaries # Boundaries for each family (0 or 1)
)

# Run the genetic algorithm
model.run()

# Display the best solution
print("Best solution found:")
print("Selected families:", model.best_variable.astype(int))
print("Total revenue:", -model.best_function)

