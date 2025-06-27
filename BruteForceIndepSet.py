def bin_representation(x, n):
    """Convert an integer to its binary representation of length n."""
    res = []
    while x != 0:
        res.append(x % 2)
        x = x // 2
    # Pad with zeros to reach length n
    while len(res) < n:
        res.append(0)
    return res
# Contraints Function
def is_independent_set(vertices, graph):  
    """Check if vertices form an independent set in the graph."""
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            if vertices[i] == 1 and vertices[j] == 1 and graph[i][j] == 1:
                return False
    return True
# Cout Function
def cost(sp, graph, n):
    """Calculate cost: maximize set size while ensuring it's an independent set."""
    binary = bin_representation(sp, n)
    set_size = sum(binary)
    
    # Count edges between selected vertices
    edge_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if binary[i] == 1 and binary[j] == 1 and graph[i][j] == 1:
                edge_count += 1
    
    # Penalize edges between vertices (not independent set)
    return -(set_size - 10 * edge_count)

# Object Function
def find_max_independent_set(graph):
    """Find maximum independent set using brute force."""
    n = len(graph)
    N = 2**n
    
    best_solution = 0
    best_cost = cost(0, graph, n)
    
    for candidate in range(N):
        candidate_cost = cost(candidate, graph, n)
        if candidate_cost < best_cost:
            best_cost = candidate_cost
            best_solution = candidate
    
    return best_solution, best_cost

# Graph representation (adjacency matrix)
graph=[ 
[ 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[ 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[ 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[ 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[ 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[ 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[ 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
[ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
[ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
[ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]       
]

# Find maximum independent set
solution, solution_cost = find_max_independent_set(graph)
vertices = bin_representation(solution, len(graph))

print(f"Maximum independent set: {vertices}")
print(f"Cost: {abs(solution_cost)}")
