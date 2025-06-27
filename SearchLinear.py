import time

def search(array, key):
    """
    Linear search algorithm to find key in array.
    Returns the index of key if found, -1 otherwise.
    """
    iterations = 0
    for i in range(len(array)):
        iterations += 1
        if array[i] == key:
            return i, iterations
    return -1, iterations

# Parameters
a = 0
b = 100000
key = 2  # Value to search for
# key = b - 1  # Uncomment to search for the last element instead

# Create the list
array = list(range(a, b))

# Perform search and measure time
start_time = time.process_time()
index, iterations = search(array, key)
end_time = time.process_time()

# Print results
print(f"Index: {index}")
print(f"For N = {len(array)}")
print(f"Time = {end_time - start_time:.6f} seconds")
print(f"Iterations = {iterations}")
