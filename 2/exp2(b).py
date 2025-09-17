def repeatedSubstringPattern(s):
    # Concatenate string with itself
    doubled = s + s
    # Remove first and last character
    check_str = doubled[1:-1]
    # Check if original string exists inside
    return s in check_str

# Example input
s = "abab"   # From Example 1
result = repeatedSubstringPattern(s)

# Output
print("Input:", s)
print("Output:", result)
