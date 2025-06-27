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
file=[]
cout=[0,0,0,0,0,0,0,0,0,0,0,0,0]
mark=[0,0,0,0,0,0,0,0,0,0,0,0,0]
N=13
"""
def dfs(graph,start):
    stack = [start] 
    mark[start] = 1 
    while stack:
        s = stack.pop() 
        print('Processing:',s)
        
        for v in range(N):
            if graph[s][v] != 0:
                cout[v] = max(cout[v],cout[s] + graph[s][v])
                if mark[v] == 0: 
                    stack.append(v)
                    mark[v] = 1
"""

def dfs_rec(graph,node):
    mark[node] = 1  
    print("----:",node)
    
    for neighbor in range(N):
        if graph[node][neighbor] != 0:
            cout[neighbor] = max(cout[neighbor],cout[node] + graph[node][neighbor])
            if mark[neighbor] == 0: 
             dfs_rec(graph,neighbor)
    mark[node] = 0  

dfs_rec(graph,0)



#dfs(graph,0)
dfs_rec(graph,0)
print(cout)
