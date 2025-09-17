def rearrangeMaxMin(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1
    result = []

    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(arr[right])
            right -= 1
        else:
            result.append(arr[left])
            left += 1
    return result

# Sample Inputs
arr1 = [7, 1, 2, 3, 4, 5, 6]


# Sample Outputs
print("Output:", rearrangeMaxMin(arr1))  # [7, 1, 6, 2, 5, 3, 4]
