# Computational Algorithms & Optimization Suite

A comprehensive collection of classic computational algorithms, optimization techniques, and graph theory implementations developed for academic and research purposes.

## 📋 Table of Contents

- [Overview](#overview)
- [Algorithms Implemented](#algorithms-implemented)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Algorithm Categories](#algorithm-categories)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains implementations of fundamental algorithms in computer science, focusing on:
- **Graph Theory Algorithms** (BFS, DFS, Shortest Path)
- **Optimization Problems** (TSP, Vertex Cover, Independent Set)
- **Search Algorithms** (Linear, Binary Search)
- **Sorting Algorithms** (Bubble Sort, Merge Sort)
- **Metaheuristics** (Genetic Algorithm, Simulated Annealing)
- **Network Flow & Path Finding**

All implementations are written in Python and designed for educational purposes, demonstrating both classical algorithms and modern optimization techniques.

## 🧮 Algorithms Implemented

### Graph Algorithms
- **BFS.py** - Breadth-First Search with path cost calculation
- **DFS.py** - Depth-First Search with recursive implementation
- **shortestpath.py** - Multiple shortest path algorithms
- **shortestVplusElogn.py** - Optimized shortest path with adjacency lists
- **Findcycle.py** - Cycle detection in graphs
- **prime.py** - Dijkstra's algorithm for shortest paths

### Optimization Problems
- **TSP_DFS.py** - Traveling Salesman Problem using DFS with branch and bound
- **tspGA3.py** - TSP solved using Genetic Algorithm
- **TSPSA.py** - TSP solved using Simulated Annealing
- **BruteForceCover.py** - Brute force vertex cover solution
- **VertexCoverGreedy.py** - Greedy approximation for vertex cover
- **BruteForceIndepSet.py** - Maximum independent set using brute force
- **CoveLS.py** - Local search for vertex cover problem

### Search & Sort Algorithms
- **SearchLinear.py** - Linear search with performance analysis
- **SearchDicotomy.py** - Binary search implementation
- **BubbleSortTimeOpt.py** - Optimized bubble sort with early termination
- **mergsort.py** - Merge sort implementation

### Metaheuristics & Advanced Optimization
- **GeneticAlgo.py** - Genetic algorithm for knapsack problem
- **partition_problem.py** - Genetic algorithm for partition problem

### Utility & Test Files
- **__pycache__/** - Python bytecode cache

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/computational-algorithms.git
cd computational-algorithms
```

2. **Install required dependencies:**
```bash
pip install numpy matplotlib geneticalgorithm heapq
```

3. **Run any algorithm:**
```bash
python BFS.py
python TSP_DFS.py
python GeneticAlgo.py
```

## 💻 Usage

### Basic Graph Traversal
```python
# BFS Example
from BFS import bfs
graph = [[0,2,1,3,0], [0,0,0,0,4], ...]
bfs(graph, start_node=0)
```

### Solving TSP
```python
# Using Genetic Algorithm
python tspGA3.py

# Using Simulated Annealing
python TSPSA.py

# Using DFS with Branch and Bound
python TSP_DFS.py
```

### Search Algorithms Performance
```python
# Compare linear vs binary search
python SearchLinear.py
python SearchDicotomy.py
```

## 📁 File Structure

```
├── Graph Algorithms/
│   ├── BFS.py                 # Breadth-First Search
│   ├── DFS.py                 # Depth-First Search
│   ├── shortestpath.py        # Shortest path algorithms
│   ├── Findcycle.py          # Cycle detection
│   └── prime.py              # Dijkstra's algorithm
│
├── Optimization/
│   ├── TSP_DFS.py            # TSP with DFS
│   ├── tspGA3.py             # TSP with Genetic Algorithm
│   ├── TSPSA.py              # TSP with Simulated Annealing
│   ├── BruteForceCover.py    # Vertex Cover (Brute Force)
│   ├── VertexCoverGreedy.py  # Vertex Cover (Greedy)
│   └── GeneticAlgo.py        # Knapsack GA
│
├── Search & Sort/
│   ├── SearchLinear.py       # Linear search
│   ├── SearchDicotomy.py     # Binary search
│   ├── BubbleSortTimeOpt.py  # Optimized bubble sort
│   └── mergsort.py           # Merge sort
│
└── Utilities/
    ├── partition_problem.py          # Partition problem GA
```

## 🔍 Algorithm Categories

### 1. **Graph Theory** 🌐
- **Complexity:** O(V + E) for BFS/DFS
- **Applications:** Social networks, web crawling, pathfinding
- **Features:** Adjacency matrix representation, cost tracking

### 2. **Traveling Salesman Problem** 🚗
- **DFS Approach:** Exact solution with branch and bound
- **Genetic Algorithm:** Metaheuristic approximation
- **Simulated Annealing:** Probabilistic optimization
- **Complexity:** Exponential (exact), Polynomial (approximation)

### 3. **Vertex Cover Problem** 🎯
- **Brute Force:** O(2^n) - Exact solution
- **Greedy:** O(V²) - 2-approximation
- **Local Search:** Iterative improvement

### 4. **Search Algorithms** 🔎
- **Linear Search:** O(n) - Sequential scanning
- **Binary Search:** O(log n) - Divide and conquer

## 📊 Performance Analysis

Most algorithms include performance metrics:
- **Time Complexity** measurements
- **Iteration counting**
- **Memory usage** tracking
- **Solution quality** evaluation

Example output:
```
Pour N = 100000
Temps = 0.0156 seconds
Iterations = 50000
```

## 🛠️ Requirements

- **Python 3.7+**
- **NumPy** - Numerical computations
- **Matplotlib** - Visualization (for some algorithms)
- **geneticalgorithm** - GA library
- **heapq** - Priority queue operations

## 🎓 Educational Value

This collection is designed for:
- **Computer Science Students** learning algorithm design
- **Researchers** studying optimization techniques
- **Developers** implementing graph algorithms
- **Anyone** interested in computational problem solving

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Add new algorithms or improve existing ones
4. Submit a pull request

## 📈 Future Enhancements

- [ ] Add visualization for graph algorithms
- [ ] Implement parallel versions of algorithms
- [ ] Add more metaheuristic approaches
- [ ] Include performance benchmarking suite
- [ ] Add algorithm animation features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**M1 HPC Student** - Computational Algorithms Implementation

---

⭐ **Star this repository if you find it helpful!**

📧 **Questions?** Feel free to open an issue or contact the maintainer.

---

### Quick Start Commands

```bash
# Clone and run
git clone <repository-url>
cd computational-algorithms

# Test graph algorithms
python BFS.py
python DFS.py

# Test optimization
python TSP_DFS.py
python GeneticAlgo.py

# Test search performance
python SearchLinear.py
python SearchDicotomy.py
```
