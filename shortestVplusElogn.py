from collections import defaultdict
import heapq
import random
import matplotlib.pyplot as plt
import networkx as nx
# Generate a graph with 50 nodes and random weights
def generate_graph(num_nodes, density=0.5, max_weight=100, seed=42):
    random.seed(seed)
    graph = [
        [
            0 if i == j else (random.randint(1, max_weight) if random.random() < density else 0)
            for j in range(num_nodes)
        ]
        for i in range(num_nodes)
    ]
    return graph

# Generate a sparse graph with 50 nodes
graph_50_nodes = generate_graph(num_nodes=5, density=0.9, max_weight=50)



def plot_graph_from_matrix(matrix):
    """
    Visualizes a graph from an adjacency matrix.

    :param matrix: 2D list or numpy array representing the adjacency matrix
    """
    # Create a graph object
    G = nx.Graph()
    
    # Add edges based on the matrix
    num_nodes = len(matrix)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # Undirected graph, skip lower triangle
            if matrix[i][j] != 0:  # Ignore zero distances (no connection)
                G.add_edge(i, j, weight=matrix[i][j])
    
    # Draw the graph
    pos = nx.spring_layout(G, seed=42)  # Layout for a neat visual
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_color='red')
    
    # Show plot
    plt.title("Graph Visualization")
    plt.show()



def build_adjacency_list(matrix):
    adjacency_list = defaultdict(list)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0 and matrix[i][j] != float('inf'):
                adjacency_list[i].append((j, matrix[i][j]))
    return adjacency_list

def shortest_cycle_sparse(graph, start_node):
    # Adjacency list representation
    adjacency_list = build_adjacency_list(graph)
    visited = set()
    path = [start_node]
    total_distance = 0

    def find_nearest(current):
        min_distance = float('inf')
        nearest_node = -1
        for neighbor, distance in adjacency_list[current]:
            if neighbor not in visited and distance < min_distance:
                min_distance = distance
                nearest_node = neighbor
        return nearest_node, min_distance

    current = start_node
    while len(visited) < len(graph):
        visited.add(current)
        next_node, dist = find_nearest(current)
        if next_node == -1:
            break  # No more reachable nodes
        path.append(next_node)
        total_distance += dist
        current = next_node

    # Return to start
    if path[-1] != start_node:
        for neighbor, distance in adjacency_list[path[-1]]:
            if neighbor == start_node:
                total_distance += distance
                path.append(start_node)
                break

    return path, total_distance


from collections import defaultdict
import itertools

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

def shortest_cycle(graph, start_node):
    all_paths = all_possible_paths(graph, start_node)
    shortest_cycle = None
    min_length = float('inf')

    for path, length in all_paths:
        # Check if the path is a cycle (ends and starts at the same node)
        if path[0][0] == path[-1][1]:
            if length < min_length:
                shortest_cycle = path
                min_length = length

    return shortest_cycle, min_length


def find_hamiltonian_cycles(graph, start_node):
    """
    Finds all Hamiltonian cycles starting and ending at a specific node.

    :param graph: 2D list representing the adjacency matrix of the graph.
                  graph[i][j] = weight of the edge between node i and j, or 0 if no edge exists.
    :param start_node: The node from which all Hamiltonian cycles must start and end.
    :return: List of tuples (cycle, distance), where cycle is a list of nodes in the cycle and
             distance is the total distance of the cycle.
    """
    def backtrack(current_node, visited, path, current_distance):
        """
        Backtracking function to explore all Hamiltonian cycles.

        :param current_node: The current node in the path.
        :param visited: Set of visited nodes.
        :param path: Current path of nodes.
        :param current_distance: Distance of the current path.
        """
        if len(path) == len(graph):  # All nodes are visited
            if graph[current_node][start_node] > 0:  # Can return to the start node
                # Form a cycle
                cycle = path + [start_node]
                total_distance = current_distance + graph[current_node][start_node]
                cycles.append((cycle, total_distance))
            return

        for neighbor in range(len(graph)):
            if graph[current_node][neighbor] > 0 and neighbor not in visited:
                # Visit this neighbor
                visited.add(neighbor)
                backtrack(
                    neighbor,
                    visited.copy(),
                    path + [neighbor],
                    current_distance + graph[current_node][neighbor],
                )
                visited.remove(neighbor)

    cycles = []
    visited = set([start_node])
    backtrack(start_node, visited, [start_node], 0)
    return cycles


# Example Graph
graph = [
    [0, 12, 0, 0, 18, 0, 10, 0, 0, 0],
    [12, 0, 10, 0, 0, 11, 0, 0, 0, 0],
    [0, 10, 0, 18, 0, 0, 14, 0, 0, 0],
    [0, 0, 18, 0, 13, 0, 0, 15, 0, 0],
    [18, 0, 0, 13, 0, 15, 0, 0, 12, 0],
    [0, 11, 0, 0, 15, 0, 19, 0, 0, 0],
    [10, 0, 14, 0, 0, 19, 0, 0, 0, 0],
    [0, 0, 0, 15, 0, 0, 0, 0, 11, 19],
    [0, 0, 0, 0, 12, 0, 0, 11, 0, 10],
    [0, 0, 0, 0, 0, 0, 0, 19, 10, 0],
]





start_node = 0
path, distance = shortest_cycle(graph, start_node)
print("methode 1")
print("Path:", path)
#plot_graph_from_matrix(graph_50_nodes)
print("Distance:", distance)
print("methode 2")
cycle, distance = shortest_cycle(graph, 0)
print(f"Shortest cycle: {cycle}, Distance: {distance}")



cycles = find_hamiltonian_cycles(graph_50_nodes, start_node)
for cycle, distance in cycles:
    print(f"Cycle: {cycle}, Distance: {distance}")




def nearest_neighbor_cycle(graph, start_node):
    n = len(graph)
    visited = set()
    path = [start_node]
    current_node = start_node
    total_distance = 0

    while len(visited) < n - 1:  # Visit all nodes except the last one
        visited.add(current_node)
        nearest_node = None
        min_distance = float('inf')

        # Find the nearest unvisited neighbor
        for neighbor in range(n):
            if neighbor not in visited and graph[current_node][neighbor] > 0:
                if graph[current_node][neighbor] < min_distance:
                    min_distance = graph[current_node][neighbor]
                    nearest_node = neighbor

        if nearest_node is None:
            break  # No more reachable nodes

        path.append(nearest_node)
        total_distance += min_distance
        current_node = nearest_node

    # Return to the starting node to complete the cycle
    if path[-1] != start_node and graph[current_node][start_node] > 0:
        path.append(start_node)
        total_distance += graph[current_node][start_node]

    return path, total_distance
graph_sparse_10 = [
    [0, 12, 0, 0, 18, 0, 10, 0, 0, 0],
    [12, 0, 10, 0, 0, 11, 0, 0, 0, 0],
    [0, 10, 0, 18, 0, 0, 14, 0, 0, 0],
    [0, 0, 18, 0, 13, 0, 0, 15, 0, 0],
    [18, 0, 0, 13, 0, 15, 0, 0, 12, 0],
    [0, 11, 0, 0, 15, 0, 19, 0, 0, 0],
    [10, 0, 14, 0, 0, 19, 0, 0, 0, 0],
    [0, 0, 0, 15, 0, 0, 0, 0, 11, 19],
    [0, 0, 0, 0, 12, 0, 0, 11, 0, 10],
    [0, 0, 0, 0, 0, 0, 0, 19, 10, 0],
]

start_node = 0
path, distance = nearest_neighbor_cycle(graph_sparse_10, start_node)
print("Cycle Path:", path)
print("Total Distance:", distance)
