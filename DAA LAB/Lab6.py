import random

def deterministic_partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1  
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return i + 1  

def quicksort_deterministic(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)  
        quicksort_deterministic(arr, low, pi - 1)  
        quicksort_deterministic(arr, pi + 1, high)  

def randomized_partition(arr, low, high):
    random_pivot = low + (high - low) // 2  
    arr[random_pivot], arr[high] = arr[high], arr[random_pivot]  
    return deterministic_partition(arr, low, high) 

def quicksort_randomized(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)  
        quicksort_randomized(arr, low, pi - 1)  
        quicksort_randomized(arr, pi + 1, high)  

def analyze_quicksort(arr):
   
    arr_copy1 = arr.copy()  
    quicksort_deterministic(arr_copy1, 0, len(arr_copy1) - 1)
    
    arr_copy2 = arr.copy()  
    quicksort_randomized(arr_copy2, 0, len(arr_copy2) - 1)
    
    print("\nDeterministic Quick Sort Result:")
    print(arr_copy1)
    
    print("\nRandomized Quick Sort Result:")
    print(arr_copy2)

if __name__ == "__main__":
    print("Enter the number of elements in the array:")
    n = int(input())  

    arr = []
    print("Enter the elements of the array:")
    for i in range(n):
        arr.append(int(input(f"Element {i+1}: ")))

    print("\nOriginal Array:")
    print(arr)
    analyze_quicksort(arr)
