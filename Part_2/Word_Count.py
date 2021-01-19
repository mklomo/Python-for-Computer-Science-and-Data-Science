""" Tokenizing a string and counting unique characters """

# Initializing Phase

text = text = f"{input('Please enter the sentence here:')}"

word_counts = {}

# Processing Phase

# Count occurrences of each unique word

for word in text.split():           # Tell text to split
    if word in word_counts:         # Check if key exists in dictionary
        word_counts[word] += 1      # Update existing key-value pair

    else:                           # Create if it does not exist
        word_counts[word] = 1       # Insert new key-value pair

print(f"{'WORD':<12}COUNT")

for word, count in sorted(word_counts.items()):
    print(f"{word:<12}{count}")


print("\nNumber of unique words: ", len(word_counts))