

graph =     [
[0,1,0,1,0,0,1,1],
[1,0,0,1,0,1,0,0],
[0,0,0,1,0,1,0,0],
[1,1,1,0,1,0,0,0],
[0,0,0,1,0,1,0,0],
[0,1,1,0,1,0,1,1],
[1,0,0,0,0,1,0,0],
[1,0,0,0,0,1,0,0],
]
def is_empty(graph):
    """Check if the graph has no edges."""
    for row in graph:
        if any(edge != 0 for edge in row):
            return False
    return True

def find_max_degree_vertex(graph):
    """Find the vertex with the maximum number of connections."""
    max_connections = 0
    selected_vertex = 0
    
    for i, edges in enumerate(graph):
        connections = sum(1 for edge in edges if edge != 0)
        if connections > max_connections:
            max_connections = connections
            selected_vertex = i
            
    return selected_vertex

def remove_vertex(graph, vertex):
    """Remove all edges connected to the given vertex."""
    for i in range(len(graph)):
        graph[vertex][i] = 0
        graph[i][vertex] = 0
    return graph

def greedy_vertex_cover(graph):
    """Find a vertex cover using a greedy algorithm."""
    cover = []
    graph_copy = [row[:] for row in graph]  # Create a copy to avoid modifying the original
    
    while not is_empty(graph_copy):
        vertex = find_max_degree_vertex(graph_copy)
        cover.append(vertex)
        remove_vertex(graph_copy, vertex)
    
    return cover

# Find the vertex cover
vertex_cover = greedy_vertex_cover(graph)
print("Vertex cover:", vertex_cover)
