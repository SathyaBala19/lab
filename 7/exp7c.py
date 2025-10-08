import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        p = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, p - 1)
        randomized_quick_sort(arr, p + 1, high)

arr1 = [12, -4, 0, 8, 15, 3, -1]
randomized_quick_sort(arr1, 0, len(arr1) - 1)
print("Sorted Array:", arr1)