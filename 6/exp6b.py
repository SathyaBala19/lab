def canPartitionKSubsets(nums, k):
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False

    target = total_sum // k
    nums.sort(reverse=True)
    subset_sums = [0] * k

    def backtrack(index):
        if index == len(nums):
            return True
        num = nums[index]
        for i in range(k):
            if subset_sums[i] + num <= target:
                subset_sums[i] += num
                if backtrack(index + 1):
                    return True
                subset_sums[i] -= num
            if subset_sums[i] == 0:
                break
        return False

    return backtrack(0)

nums1 = [4, 3, 2, 3, 5, 2, 1]
k1 = 4
print("Input:", nums1, "k =", k1)
print("Output:", canPartitionKSubsets(nums1, k1))