def subsetXORSum(nums):
    result = 0
    
    def dfs(index, currentXor):
        nonlocal result
        if index == len(nums):
            result += currentXor
            return
        # Include current element
        dfs(index + 1, currentXor ^ nums[index])
        # Exclude current element
        dfs(index + 1, currentXor)
    
    dfs(0, 0)
    return result


# Example Run
nums = [1, 3]
print("Sum of all subset XOR totals:", subsetXORSum(nums))
