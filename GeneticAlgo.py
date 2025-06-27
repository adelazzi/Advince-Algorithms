# Import necessary packages
from geneticalgorithm import geneticalgorithm as ga
import numpy as np

# Define problem parameters
limit = 29  # Bus capacity limit (29 passengers)
dim = 10     # Number of families (10 families in the example)
value = [4*1000, 5*1000, 3*1000, 6*1000, 7*1000, 5*1000, 7*1000, 4*1000, 6*1000, 8*1000]  # Value per family (1000 DA per person)
weight = [4, 5, 3, 6, 7, 5, 7, 4, 6, 8]  # Number of passengers per family
pen = 1000   # Penalty for exceeding the weight limit

# Define the fitness function
def g(x):
    v = 0
    w = 0  # Initialize the weight (total passengers) to 0
    for i in range(len(x)):
        w += x[i] * weight[i]  # Calculate total weight (number of passengers)
        v += x[i] * value[i]   # Calculate total value (revenue from families)
    if w > limit:  # Check if the weight exceeds the bus capacity
        v -= (w - limit) * pen  # Apply penalty to the value (revenue)
    return -v # Return negative value for minimization in GA

# Define the boundaries for each variable (0 or 1 for binary decisions)
boundaries = np.array([[0, 1]] * dim)  # Binary variables (0 for not selecting, 1 for selecting)

# Create the GA model
model = ga(
    function=g,  # Fitness function
    dimension=dim,  # Number of decision variables (families)
    variable_type='bool',  # Type of variables (binary: select or not select a family)
    variable_boundaries=boundaries  # Boundaries for each family (either 0 or 1)
)

# Run the genetic algorithm
model.run()
