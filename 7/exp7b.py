def findKthSmallest(arr, k):
    n = len(arr)
    for i in range(k):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr[k - 1]

arr1 = [7, 10, 4, 3, 20, 15]
k1 = 3
print("Input:", arr1, "k =", k1)
print("Output:", findKthSmallest(arr1, k1))