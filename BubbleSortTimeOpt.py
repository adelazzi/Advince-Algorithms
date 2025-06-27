import time

def bubble_sort(data):
    n = len(data)
    comparisons = 0
    
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if data[j] < data[j+1]:  # For descending order
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                
        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break
            
    return comparisons


a = 0
b = 100000
data = list(range(a, b))
n = len(data)

# Measure sorting time
start_time = time.process_time()
iterations = bubble_sort(data)
end_time = time.process_time()

# Print results
print(f"For N = {n}")
print(f"Time = {end_time - start_time:.6f} seconds")
print(f"Comparisons = {iterations}")

