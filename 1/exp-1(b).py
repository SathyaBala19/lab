def find_first_last_position(nums, target):
    def binary_search(is_first):
        low, high = 0, len(nums) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                index = mid
                if is_first:
                    high = mid - 1  # ml
                else:
                    low = mid + 1  # mr
        return index

    first = binary_search(True)
    last = binary_search(False)
    return [first, last]

print(find_first_last_position([5,7,7,8,8,10], 8))
print(find_first_last_position([5,7,7,8,8,10], 6))
print(find_first_last_position([], 0))