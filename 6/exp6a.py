def findSubsets(arr, target_sum):
    result = []
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0 or start == len(arr):
            return
        
        current.append(arr[start])
        backtrack(start + 1, current, remaining - arr[start])

        current.pop()
        backtrack(start + 1, current, remaining)
    
    backtrack(0, [], target_sum)
    return result

arr1 = [1, 2, 1]
sum1 = 3
print("Input:", arr1, " Sum:", sum1)
print("Output:", findSubsets(arr1, sum1))