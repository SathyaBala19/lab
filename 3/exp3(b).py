def shortest_special_subarray(nums, k):
    n = len(nums)
    min_len = float('inf')

    for i in range(n):
        current_or = 0
        for j in range(i, n):
            current_or |= nums[j]
            if current_or >= k:
                min_len = min(min_len, j - i + 1)
                break

    return -1 if min_len == float('inf') else min_len

nums = [1, 2, 3]
k = 2
result = shortest_special_subarray(nums, k)

print("Input nums:", nums)
print("k:", k)
print("Output:", result)