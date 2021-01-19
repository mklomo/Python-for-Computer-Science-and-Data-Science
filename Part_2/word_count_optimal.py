""" Counting words in a sentence """

# Using the python function counter to count unique words in a sentence

from collections import Counter

text = f"{input('Please enter the sentence here: ')}"


# Producing a dictionary for the words

word_count = Counter(text.split())


for word, count in sorted(word_count.items()):
    print(f"{word:<12}{count}")

print(f"Number of unique keys: ", len(word_count))