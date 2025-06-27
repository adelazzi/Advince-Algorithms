#Simulated anealing
import numpy as np
import matplotlib.pyplot as plt

graph2 = [[0, 5, 1, 3, 2],
             [5, 0, 2, 3, 1],
             [1, 2, 0, 2, 3],
             [3, 3, 2, 0, 4],
             [2, 1, 3, 4, 0] ]
    
graph = [
[0,29,82,46,68,52,72,42,51,55,29,74,23,72,46],
[29,0,55,46,42,43,43,23,23,31,41,51,11,52,21],
[82,55,0,68,46,55,23,43,41,29,79,21,64,31,51],
[46,46,68,0,82,15,72,31,62,42,21,51,51,43,64],
[68,42,46,8,0,74,23,52,21,46,82,58,46,65,23],
[52,43,55,15,74,0,61,23,55,31,33,37,51,29,59],
[72,43,23,72,23,61,0,42,23,31,77,37,51,46,33],
[42,23,43,31,52,23,42,0,33,15,37,33,33,31,37],
[51,23,41,62,21,55,23,33,0,29,62,46,29,51,11],
[55,31,29,42,46,31,31,15,29,0,51,21,41,23,37],
[29,41,79,21,82,33,77,37,62,51,0,65,42,59,61],
[74,51,21,51,58,37,37,33,46,21,65,0,61,11,55],
[23,11,64,51,46,51,51,33,29,41,42,61,0,62,23],
[72,52,31,43,65,29,46,31,51,23,59,11,62,0,59],
[46,21,51,64,23,59,33,37,11,37,61,55,23,59,0] ]
    #graph = [[0, 4, 3, 2],
    #         [4, 0, 1, 2],
    #         [3, 1, 0, 5],
    #         [1, 2, 5, 0] ]
def voisinage(s):
   """Generate a neighbor solution by reversing a random subsequence."""
   n, m = np.random.randint(0, len(graph), size=2)
   i, j = min(n, m), max(n, m)
   s1 = s.copy()
   while i < j:
      s1[i], s1[j] = s1[j], s1[i]
      i += 1
      j -= 1
   return s1

def cost(G, s):
   """Calculate the total cost of a tour."""
   total = 0
   for i in range(len(s) - 1):
      total += G[s[i]][s[i + 1]]
   total += G[s[-1]][s[0]]  # Return to starting point
   return total

def initial():
   """Generate initial solution."""
   return list(range(len(graph)))

def simulated_annealing(T_initial=30, alpha=0.9, iterations=1500):
   """Run simulated annealing algorithm for TSP."""
   costs = []
   T = T_initial
   s = initial()
   c = cost(graph, s)
   
   for i in range(iterations):
      sp = voisinage(s)
      cp = cost(graph, sp)
      
      if cp < c:
         s, c = sp, cp
      else:
         probability = np.exp((c - cp) / T)
         if np.random.rand() < probability:
            s, c = sp, cp
      
      T *= alpha
      costs.append(c)
   
   return s, c, costs

# Run the algorithm
best_path, best_cost, cost_history = simulated_annealing()
print(f"Best path: {best_path}")
print(f"Best cost: {best_cost}")

# Plot the cost history
plt.figure(figsize=(10, 6))
plt.plot(cost_history)
plt.title("Simulated Annealing for TSP")
plt.xlabel("Iteration")
plt.ylabel("Path Cost")
plt.grid(True)
