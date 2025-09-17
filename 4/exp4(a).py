def longest_common_subsequence(s1, s2):
    n, m = len(s1), len(s2)

    # Create DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


# Example usage
s1 = "AGGTAB"
s2 = "GXTXAYB"
print("Length of Longest Common Subsequence:", longest_common_subsequence(s1, s2))
