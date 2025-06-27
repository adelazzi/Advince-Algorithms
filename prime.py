import numpy as np
import heapq


def dijkstra(adj_matrix, start):
    """
    Dijkstra's algorithm to find shortest paths from a starting node.
    
    Args:
        adj_matrix: Square matrix where adj_matrix[i][j] is the weight of edge i->j
        start: Index of the starting node
        
    Returns:
        Tuple of (distances, prev_nodes) where:
        - distances is a list of shortest distances from start to each node
        - prev_nodes is a list tracking the previous node in each shortest path
    """
    n = len(adj_matrix)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    prev_nodes = [None] * n

    # Priority queue of (distance, node) pairs
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if already processed this node
        if visited[current_node]:
            continue

        visited[current_node] = True

        # Process all neighbors
        for neighbor in range(n):
            weight = adj_matrix[current_node][neighbor]
            if weight > 0:  # If edge exists
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    prev_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances, prev_nodes


def shortest_path_subgraph(adj_matrix):
    """
    Creates a subgraph containing only the edges used in all shortest paths.
    
    Args:
        adj_matrix: Square adjacency matrix of the original graph
        
    Returns:
        A new adjacency matrix representing the shortest path subgraph
    """
    n = len(adj_matrix)
    subgraph = np.zeros((n, n))

    # For each possible start node
    for start in range(n):
        _, prev_nodes = dijkstra(adj_matrix, start)

        # For each possible end node
        for end in range(n):
            # If there's a path and it's not the start node itself
            if end != start and prev_nodes[end] is not None:
                # Add the final edge of this shortest path to the subgraph
                parent = prev_nodes[end]
                subgraph[parent][end] = adj_matrix[parent][end]

    return subgraph



"""Main function to demonstrate the shortest path subgraph algorithm."""
# Example graph (adjacency matrix where 0 means no edge)
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

# Display results
print("Graph1 (Original Adjacency Matrix):")
print(graph1)
print("\nGraph2 (Shortest Path Subgraph):")
print(graph2)


