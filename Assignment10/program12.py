import re

def find_words_starting_with_ae(text):
    words = re.findall(r'\b[a|eA|E]\w*', text)
    return words

# Test case
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

words_found = find_words_starting_with_ae(text)
print("Words starting with 'a' or 'e':", words_found)
