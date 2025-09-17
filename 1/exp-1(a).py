def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

unsorted_array = [34, 7, 23, 32, 5, 62]
target_element = int(input("Enter the element to search: "))

index_linear = linear_search(unsorted_array, target_element)
sorted_array = sorted(unsorted_array)

index_binary = binary_search(sorted_array, target_element)

print("\nSearch Results:")
if index_linear != -1:
    print(f"Linear Search: Element {target_element} found at index {index_linear} (unsorted array).")
else:
    print("Linear Search: Element not found.")

if index_binary != -1:
    print(f"Binary Search: Element {target_element} found at index {index_binary} (sorted array).")
else:
    print("Binary Search: Element not found.")

print("\nComparison Table:")
print("{:<15} {:<25} {:<25}".format('Algorithm', 'Time Complexity (Best/Worst)', 'Data Requirement'))
print("{:<15} {:<25} {:<25}".format('Linear Search', 'O(1) / O(n)', 'Works on unsorted array'))
print("{:<15} {:<25} {:<25}".format('Binary Search', 'O(1) / O(log n)', 'Requires sorted array'))