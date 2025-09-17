def rearrange_array(arr):
    arr.sort()
    result = []
    left = 0
    right = len(arr) - 1

    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[right])
        left += 1
        right -= 1

    return result

print(rearrange_array([7, 1, 2, 3, 4, 5, 6]))
print(rearrange_array([1, 6, 9, 4, 3, 7, 8, 2]))