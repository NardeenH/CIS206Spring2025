import re

def search_literals(text, words):
    found_words = {word: bool(re.search(rf"\b{word}\b", text)) for word in words}
    return found_words

# Sample text
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

# Search for words
results = search_literals(sample_text, searched_words)

# Print results
for word, found in results.items():
    print(f"'{word}' found in text: {found}")
