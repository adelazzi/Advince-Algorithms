# graph = [
#     [0, 4, 4, 0, 0, 0],
#     [4, 0, 2, 0, 0, 0],
#     [4, 2, 0, 2, 3, 4],
#     [0, 0, 2, 0, 0, 3],
#     [0, 0, 3, 0, 0, 3],
#     [0, 0, 4, 3, 3, 0] 
# ];
graph =    [
    [0, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23, 72, 46],
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
def findcycle(graph, start_node=0):
    N = len(graph)
    mark = [0] * N
    stack = [start_node]
    mark[start_node] = 1
    cycle = []
    path = [start_node]  # Track the current path
    
    print(f"Searching for cycles starting from node {start_node}...")
    
    while stack:
        current = stack[-1]  # Look at the top of the stack without popping
        found_unvisited = False
        
        # Check neighbors for unvisited nodes
        for neighbor in range(N):
            if graph[current][neighbor] != 0 and mark[neighbor] == 0:
                stack.append(neighbor)
                path.append(neighbor)
                mark[neighbor] = 1
                found_unvisited = True
                print(f"Visiting node {neighbor}")
                break
        
        # If we've found no unvisited neighbors, backtrack
        if not found_unvisited:
            stack.pop()
            
            # Check for cycle
            if len(path) >= 3:
                last_node = path[-1]
                if graph[last_node][start_node] != 0:
                    cycle = path + [start_node]  # Complete the cycle
                    print("Cycle found:", cycle)
                    return cycle
            
            if path:  # Prevent error for empty path
                path.pop()
    
    print("No cycle found")
    return []

# Test the function
cycle = findcycle(graph)
if cycle:
    print(f"Final cycle: {cycle}")
