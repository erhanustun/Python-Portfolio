# ==============================================================================
# SECTION 1: List Comprehension Examples
# ==============================================================================
print("--- List Comprehension ---")
# Create a list of squares of numbers from 1 to 10
squares = [i**2 for i in range(1, 11)]
print(f"List of squares: {squares}")

# Create a list of only even numbers
even_numbers = [i for i in range(20) if i % 2 == 0]
print(f"List of even numbers: {even_numbers}")

# Create a list of word lengths from a sentence
sentence = "Python for data science is a lot of fun"
word_lengths = [len(word) for word in sentence.split()]
print(f"Word lengths: {word_lengths}")

# ==============================================================================
# SECTION 2: Dictionary and Set Comprehension Examples
# ==============================================================================
print("\n--- Dictionary Comprehension ---")
# Create key-value pairs from a list of words
words = ["apple", "banana", "cherry"]
word_dict = {word: len(word) for word in words}
print(f"Word-length dictionary: {word_dict}")

# Create a dictionary of numbers and their squares from 1 to 5
squares_dict = {i: i**2 for i in range(1, 6)}
print(f"Number-square dictionary: {squares_dict}")

print("\n--- Set Comprehension ---")
# Create a set of unique first letters from a sentence
sentence = "python is a powerful programming language python"
first_letters = {word[0] for word in sentence.split()}
print(f"Set of unique first letters: {first_letters}")

# ==============================================================================
# SECTION 3: Application - Word Counting
# ==============================================================================
print("\n--- Application: Word Counting ---")
text = """
Python is a high-level, interpreted, and object-oriented programming language.
It is known for its clean syntax and readability, which makes it ideal for beginners.
"""
# Convert text to lowercase and remove punctuation
clean_text = ''.join(char.lower() for char in text if char.isalnum() or char.isspace())

# Count word frequencies using a dictionary comprehension
word_counts = {word: clean_text.split().count(word) for word in clean_text.split()}

print(f"Word frequencies: {word_counts}")
