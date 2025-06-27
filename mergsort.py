def merge_sort(arr):
  """
  Sorts a list using the merge sort algorithm.
  
  Args:
    arr: List to be sorted
  
  Returns:
    Sorted list
  """
  # Base case: lists with 0 or 1 elements are already sorted
  if len(arr) < 2:
    return arr
    
  # Divide the list into two halves
  middle = len(arr) // 2
  left = merge_sort(arr[:middle])
  right = merge_sort(arr[middle:])
  
  # Merge the sorted halves
  return merge_lists(left, right)


def merge_lists(left, right):
  """
  Merges two sorted lists into a single sorted list.
  
  Args:
    left: First sorted list
    right: Second sorted list
  
  Returns:
    Merged sorted list
  """
  result = []
  i = j = 0
  
  # Compare elements from both lists and add the smaller one to the result
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  
  # Add remaining elements
  result.extend(left[i:])
  result.extend(right[j:])
  
  return result


if __name__ == "__main__":
  # Test the merge sort implementation
  original_list = [5, 6, 4, 8, 7, 9, 2]
  sorted_list = merge_sort(original_list)
  
  print("Original list:", original_list)
  print("Sorted list:", sorted_list)