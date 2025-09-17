# Given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost,
# you can either climb one or two steps. You can either start from the step with index 0, or the step with
# index 1. Write a program to print the minimum cost to reach the top of the floor.

def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 0
    
    for i in range(2, n + 1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    
    return dp[n]

# Example 1
cost = [10, 15, 20]
print("Minimum Cost:", minCostClimbingStairs(cost))
