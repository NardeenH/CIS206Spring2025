def search_literal_with_position(text, word):
    # Find the position of the word in the text
    start_index = text.find(word)
    if start_index != -1:
        end_index = start_index + len(word)
        return start_index, end_index
    return None

# Sample text
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

# Search for word and its position
position = search_literal_with_position(sample_text, searched_word)

if position:
    print(f"'{searched_word}' found at position: {position}")
else:
    print(f"'{searched_word}' not found in text.")
