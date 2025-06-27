import itertools
import numpy as np

from collections import defaultdict

from shortestVplusElogn import build_adjacency_list




np.random.seed(42)

# Create a matrix of random integers between 10 and 1000
complete_graph_matrix = np.random.randint(10, 1001, size=(10, 10))

# Set diagonal to 0 (no self-connections)
np.fill_diagonal(complete_graph_matrix, 0)

# Optional: Ensure symmetry (if undirected graph)
# This makes sure the weight from node A to B is the same as B to A
complete_graph_matrix = np.triu(complete_graph_matrix) + np.triu(complete_graph_matrix, 1).T



def shortest_cycle(graph, start_node):
    n = len(graph)
    
   
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] == 0:
                graph[i][j] = float('inf')
    
    visited = [False] * n  
    path1, path2 = [start_node], [start_node]  
    visited[start_node] = True

    # Function to find the nearest unvisited neighbor
    def find_nearest(current):
        min_distance = float('inf')
        nearest_node = -1
        for neighbor in range(n):
            if not visited[neighbor] and graph[current][neighbor] < min_distance:
                min_distance = graph[current][neighbor]
                nearest_node = neighbor
        return nearest_node

    
    current1, current2 = start_node, start_node
    for _ in range(n - 1):  
        
        next1 = find_nearest(current1)
        next2 = find_nearest(current2)

        if next1 != -1:  
            path1.append(next1)
            visited[next1] = True
            current1 = next1

        if next2 != -1 and next2 != next1: 
            path2.append(next2)
            visited[next2] = True
            current2 = next2

    cycle = path1 + path2[::-1]  
    total_distance = 0

    for i in range(len(cycle)):
        total_distance += graph[cycle[i - 1]][cycle[i]]

    return cycle, total_distance

# Example Usage
graph =    [[0, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23, 72, 46],
            [29, 0, 55, 46, 42, 43, 43, 23, 23, 31, 41, 51, 11, 52, 21],
            [82, 55, 0, 68, 46, 55, 23, 43, 41, 29, 79, 21, 64, 31, 51],
            [46, 46, 68, 0, 82, 15, 72, 31, 62, 42, 21, 51, 51, 43, 64],
            [68 ,42 ,46 ,82 ,0 ,74 ,23 ,52 ,21 ,46 ,82 ,58 ,46 ,65 ,23],
            [52, 43, 55, 15, 74, 0, 61, 23, 55, 31, 33, 37, 51, 29, 59],
            [72 ,43 ,23 ,72 ,23 ,61 ,0 ,42 ,23 ,31 ,77 ,37 ,51 ,46 ,33],
            [42, 23, 43, 31, 52, 23, 42, 0, 33, 15, 37, 33, 33, 31, 37],
            [51 ,23 ,41 ,62 ,21 ,55 ,23 ,33 ,0 ,29 ,62 ,46 ,29 ,51 ,11],
            [55, 31, 29, 42, 46, 31, 31, 15, 29, 0, 51, 21, 41, 23, 37],
            [29 ,41 ,0 ,21 ,82 ,33 ,77 ,37 ,62 ,51 ,0 ,65 ,42 ,59 ,61],
            [74, 51, 21, 51, 58, 37, 37, 33, 46 ,21 ,65 ,0, 61, 11, 55],
            [12 ,0 ,64 ,51 ,46 ,51 ,51 ,33 ,29 ,41 ,42 ,61 ,0 ,62 ,23],
            [72, 52, 31, 43, 65, 29, 46, 31, 51, 23, 59, 11, 62, 0, 59],
            [46 ,21 ,51 ,64 ,23 ,59 ,33 ,37 ,11 ,37 ,61 ,55 ,23 ,59 ,0]
]

start_node = 0
cycle, distance = shortest_cycle(complete_graph_matrix, start_node)
print("Cycle:", cycle)
print("Total Distance:", distance)

import numpy as np

# Create a 10x10 matrix for a complete graph with larger values
# We'll use a matrix with random large numbers between 10 and 1000

# Set a random seed for reproducibility

print("Adjacency Matrix for Complete Graph with 10 Nodes (Large Values):")
print(complete_graph_matrix)

# Optional: Visualization of the matrix
print("\nMatrix Representation:")
for row in complete_graph_matrix:
    print(' '.join(map(str, row)))

# Additional information
print("\nMatrix Properties:")
print(f"Total nodes: {complete_graph_matrix.shape[0]}")
print(f"Maximum edge weight: {complete_graph_matrix.max()}")
print(f"Minimum edge weight: {complete_graph_matrix[complete_graph_matrix > 0].min()}")






def build_adjacency11_list(matrix):
    adjacency_list = defaultdict(list)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0 and matrix[i][j] != float('inf'):
                adjacency_list[i].append((j, matrix[i][j]))
    return adjacency_list



def all_possible_paths(graph, start_node):
    adjacency_list = build_adjacency_list(graph)
    nodes = list(adjacency_list.keys())
    paths = []

    for perm in itertools.permutations(nodes):
        if perm[0] == start_node:
            path = [(perm[i], perm[i + 1]) for i in range(len(perm) - 1)]
            paths.append((path, sum(graph[u][v] for u, v in path)))

    return paths
