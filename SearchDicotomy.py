import time

def binary_search(arr, start, end, key):
     """
     Binary search implementation that finds key in arr between start and end indices.
     Returns the value if found, or the key itself if not found.
     """
     iterations = 0
     
     while start <= end:
          iterations += 1
          mid = (start + end) // 2
          
          if mid >= len(arr):
               print("Key Not Found!")
               return key, iterations
               
          if arr[mid] == key:
               return arr[mid], iterations
          elif arr[mid] < key:
               start = mid + 1
          else:
               end = mid - 1
     
     print("Key Not Found!")
     return key, iterations


# Parameters
start_idx = 0
end_idx = 100000
target = 2  # Value to search for

# Create the sorted list
sorted_list = list(range(start_idx, end_idx))

# Measure the search time
start_time = time.process_time()
result, iterations = binary_search(sorted_list, start_idx, len(sorted_list) - 1, target)
end_time = time.process_time()

# Print results
print(f"For N = {len(sorted_list)}")
print(f"Time = {end_time - start_time}")
print(f"Iterations = {iterations}")


