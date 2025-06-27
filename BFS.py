def bfs(graph, start, n):
    """
    Breadth-First Search algorithm that calculates maximum path costs.
    
    Args:
        graph: Adjacency matrix representation of the graph
        start: Starting vertex
        n: Number of vertices in the graph
    
    Returns:
        List of maximum path costs from start to each vertex
    """
    # Initialize data structures
    queue = [start]
    visited = [0] * n
    costs = [0] * n
    
    # Mark starting node as visited
    visited[start] = 1
    
    while queue:
        current = queue.pop(0)
        print(f'Visiting vertex: {current}')
        
        # Check all adjacent vertices
        for neighbor in range(n):
            if graph[current][neighbor] != 0:
                # Update the maximum cost to reach this neighbor
                costs[neighbor] = max(costs[neighbor], costs[current] + graph[current][neighbor])
                
                # If not yet visited, add to queue
                if visited[neighbor] == 0:
                    queue.append(neighbor)
                    visited[neighbor] = 1
    
    return costs


# Define the graph as an adjacency matrix
graph = [
    [0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 4, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Run BFS from vertex 0
N = len(graph)
result = bfs(graph, 0, N)
print("Maximum path costs:", result)