def maxRepeating(sequence, word):
    k = 0
    repeat = word
    while repeat in sequence:
        k += 1
        repeat += word
    return k

# Example usage
sequence = "ababc"
word = "ab"

result = maxRepeating(sequence, word)
print("Input sequence:", sequence)
print("Input word:", word)
print("Output:", result)
