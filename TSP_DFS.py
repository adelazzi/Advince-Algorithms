graph = [
    [0, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23, 72, 46],
    [29, 0, 55, 46, 42, 43, 43, 23, 23, 31, 41, 51, 11, 52, 21],
    [82, 55, 0, 68, 46, 55, 23, 43, 41, 29, 79, 21, 64, 31, 51],
    [46, 46, 68, 0, 82, 15, 72, 31, 62, 42, 21, 51, 51, 43, 64],
    [68, 42, 46, 82, 0, 74, 23, 52, 21, 46, 82, 58, 46, 65, 23],
    [52, 43, 55, 15, 74, 0, 61, 23, 55, 31, 33, 37, 51, 29, 59],
    [72, 43, 23, 72, 23, 61, 0, 42, 23, 31, 77, 37, 51, 46, 33],
    [42, 23, 43, 31, 52, 23, 42, 0, 33, 15, 37, 33, 33, 31, 37],
    [51, 23, 41, 62, 21, 55, 23, 33, 0, 29, 62, 46, 29, 51, 11],
    [55, 31, 29, 42, 46, 31, 31, 15, 29, 0, 51, 21, 41, 23, 37],
    [29, 41, 79, 21, 82, 33, 77, 37, 62, 51, 0, 65, 42, 59, 61],
    [74, 51, 21, 51, 58, 37, 37, 33, 46, 21, 65, 0, 61, 11, 55],
    [23, 11, 64, 51, 46, 51, 51, 33, 29, 41, 42, 61, 0, 62, 23],
    [72, 52, 31, 43, 65, 29, 46, 31, 51, 23, 59, 11, 62, 0, 59],
    [46, 21, 51, 64, 23, 59, 33, 37, 11, 37, 61, 55, 23, 59, 0]
]
class TSPSolver:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.path_length = 0
        self.min_path_length = float('inf')
        self.current_step = 1
        self.path = []
        self.upper_bound = 400
        self.source = 0
    
    def solve(self):
        """Start the TSP solving process from the source node."""
        self.dfs(self.source)
        return self.min_path_length
    
    def dfs(self, current_node):
        """Depth-first search implementation for TSP."""
        # Check if we've completed a tour
        if current_node == self.source and self.current_step == len(self.graph) + 1:
            print(f"  Tour = {self.path}, length = {self.path_length}")
            if self.path_length < self.min_path_length:
                self.min_path_length = self.path_length
                self.upper_bound = self.path_length
            return
        
        # Skip if node already visited
        if self.visited[current_node]:
            return
            
        # Prune if current path exceeds upper bound
        if self.path_length >= self.upper_bound:
            return
        
        # Mark current node as visited and add to path
        self.visited[current_node] = True
        self.path.append(current_node)
        
        # Explore neighbors
        for next_node in range(len(self.graph[current_node])):
            # Visit if unvisited, or if it's the source and we've visited all nodes
            if not self.visited[next_node] or (next_node == self.source and self.current_step == len(self.graph)):
                # Add edge weight
                self.path_length += self.graph[current_node][next_node]
                self.current_step += 1
                
                # Continue DFS if under bound
                if self.path_length <= self.upper_bound:
                    self.dfs(next_node)
                
                # Backtrack
                self.path_length -= self.graph[current_node][next_node]
                self.current_step -= 1
        
        # Unmark node and remove from path when backtracking
        self.visited[current_node] = False
        self.path.pop()


# Initialize and run solver
solver = TSPSolver(graph)
min_tour_length = solver.solve()
print(f'The best tour length = {min_tour_length}')
