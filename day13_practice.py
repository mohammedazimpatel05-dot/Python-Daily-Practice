# Create an input tuple of words
words_tuple = ("python", "tuple", "uppercase", "conversion")

# Convert words to uppercase using a tuple comprehension
uppercase_tuple = tuple(word.upper() for word in words_tuple)

# Output results
print("Original Tuple:", words_tuple)
print("Uppercase Tuple:", uppercase_tuple)
