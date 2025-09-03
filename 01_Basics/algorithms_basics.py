# algorithms_basics.py

# ==============================================================================
# SECTION 1: Search Algorithms
# ==============================================================================
print("--- Search Algorithms ---")

def linear_search(arr, x):
    """
    Performs a linear search.
    It checks each element of the list sequentially to find the target value.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Return the index of the value
    return -1  # Return -1 if the value is not found

def binary_search(arr, x):
    """
    Performs a binary search.
    It works only on a sorted list and is much more efficient.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

# Application
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

print(f"Linear search for target {target} (index): {linear_search(numbers, target)}")
print(f"Binary search for target {target} (index): {binary_search(numbers, target)}")
print(f"Linear search for target 99 (index): {linear_search(numbers, 99)}")

# ==============================================================================
# SECTION 2: Sorting Algorithms
# ==============================================================================
print("\n--- Sorting Algorithms ---")

def bubble_sort(arr):
    """
    Performs a bubble sort.
    It repeatedly steps through the list, compares adjacent elements and swaps them.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap elements

def insertion_sort(arr):
    """
    Performs an insertion sort.
    It builds the final sorted array one item at a time.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
# Application
unsorted_list = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort
bubble_list = unsorted_list.copy()
bubble_sort(bubble_list)
print(f"List sorted with Bubble Sort: {bubble_list}")

# Insertion Sort
insertion_list = unsorted_list.copy()
insertion_sort(insertion_list)
print(f"List sorted with Insertion Sort: {insertion_list}")
