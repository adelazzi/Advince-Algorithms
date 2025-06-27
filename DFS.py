graph = [ 
    [0,2,1,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,4,0,0,0,0,0,0,0,0],   
    [0,0,0,0,0,6,0,0,0,0,0,0,0],
    [0,0,0,0,0,12,4,2,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,5,0,0,2,0],
    [0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,4,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0]   
]
# Constants and global variables
N = 13
costs = [0] * N
visited = [0] * N

def dfs_recursive(graph, node):
    """
    Depth-first search recursive implementation that calculates maximum path costs.
    
    Args:
        graph: Adjacency matrix representing the graph
        node: Current node to process
    """
    visited[node] = 1
    print(f"Processing node: {node}")
    
    for neighbor in range(N):
        if graph[node][neighbor] != 0:
            # Update cost to neighbor if path through current node is better
            costs[neighbor] = max(costs[neighbor], costs[node] + graph[node][neighbor])
            if visited[neighbor] == 0:
                dfs_recursive(graph, neighbor)
    
    # Mark as done with this node
    visited[node] = 0

def dfs_iterative(graph, start):
    """
    Depth-first search iterative implementation that calculates maximum path costs.
    
    Args:
        graph: Adjacency matrix representing the graph
        start: Starting node for the search
    """
    stack = [start]
    visited[start] = 1
    
    while stack:
        node = stack.pop()
        print(f"Processing node: {node}")
        
        for neighbor in range(N):
            if graph[node][neighbor] != 0:
                # Update cost to neighbor if path through current node is better
                costs[neighbor] = max(costs[neighbor], costs[node] + graph[node][neighbor])
                if visited[neighbor] == 0:
                    stack.append(neighbor)
                    visited[neighbor] = 1

# Run the recursive DFS starting from node 0
dfs_recursive(graph, 0)
print(f"Maximum path costs: {costs}")

# Uncomment to use iterative version instead:
# visited = [0] * N  # Reset visited array
# costs = [0] * N    # Reset costs array
# dfs_iterative(graph, 0)
# print(f"Maximum path costs: {costs}")
