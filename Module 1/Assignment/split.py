sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create a dictionary using dictionary comprehension
word_lengths = {word: len(word) for word in words}

# Print the resulting dictionary
print("Word lengths dictionary:")
print(word_lengths)