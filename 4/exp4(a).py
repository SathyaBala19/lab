def lcs_length(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    
    # Create a 2D DP table initialized with 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Build the table bottom-up
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]  # Characters match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Skip one character
    
    return dp[n][m]  # Final answer in bottom-right cell


# Example usage:
s1 = "AGGTAB"
s2 = "GXTXAYB"
print("Length of LCS:", lcs_length(s1, s2))  # Output: 4

s1 = "ABC"
s2 = "CBA"
print("Length of LCS:", lcs_length(s1, s2))  # Output: 1
