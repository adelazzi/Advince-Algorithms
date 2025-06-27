import numpy as np
import heapq

def dijkstra(adj_matrix, start):
    n = len(adj_matrix)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    prev_nodes = [None] * n

    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue

        visited[current_node] = True

        for neighbor in range(n):
            weight = adj_matrix[current_node][neighbor]
            if weight > 0:  # Check if there's an edge
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    prev_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances, prev_nodes

def shortest_path_subgraph(adj_matrix):
    n = len(adj_matrix)
    subgraph = np.zeros((n, n))  # Initialize the subgraph matrix with 0

    for start in range(n):
        _, prev_nodes = dijkstra(adj_matrix, start)

        for end in range(n):
            if end != start and prev_nodes[end] is not None:
                subgraph[prev_nodes[end]][end] = adj_matrix[prev_nodes[end]][end]

    return subgraph

# Example adjacency matrix with 0 for no edges
graph1 = np.array([
    [0, 4, 4, 0, 0, 0],
    [4, 0, 2, 0, 0, 0],
    [4, 2, 0, 2, 3, 4],
    [0, 0, 2, 0, 0, 3],
    [0, 0, 3, 0, 0, 3],
    [0, 0, 4, 3, 3, 0]
])

# Generate the subgraph with only shortest paths
graph2 = shortest_path_subgraph(graph1)

print("Graph1 (Adjacency Matrix):")
print(graph1)

print("\nGraph2 (Shortest Path Subgraph):")
print(graph2)
