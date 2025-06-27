from itertools import product

# Graph represented as an adjacency matrix
graph = [
    [0, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
]

n = len(graph)

def copy_matrix(source, target):
    """Copy the source matrix to the target matrix"""
    for i in range(n):
        for j in range(n):
            target[i][j] = source[i][j]

def calculate_cost(solution):
    """Calculate the number of selected nodes in the solution"""
    return sum(1 for bit in solution if bit == '1')

def check_constraint(solution):
    """Check if the solution covers all edges"""
    # Create a working copy of the graph
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    copy_matrix(graph, matrix)
    
    # Remove edges covered by selected nodes
    for i in range(n):
        if solution[i] == '1':
            for j in range(n):
                matrix[i][j] = 0
                matrix[j][i] = 0
                
    # Count remaining edges
    remaining_edges = sum(matrix[i][j] for i in range(n) for j in range(n))
    return remaining_edges

def initial_solution():
    """Create an initial solution with all nodes selected"""
    return ['1' for _ in range(n)]

# Initialize best solution found
best_solution = initial_solution()
best_cost = n

# Enumerate all possible combinations
for candidate in product(['0', '1'], repeat=n):
    # Check if candidate solution covers all edges
    if check_constraint(candidate) == 0:
        current_cost = calculate_cost(candidate)
        # Update best solution if current is better
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = candidate

print(best_solution, best_cost)
