import re

def match_word_with_z(s):
    pattern = re.compile(r"\b\w*z\w*\b", re.IGNORECASE)  # Matches words containing 'z'
    return pattern.findall(s)

# Test cases
strings = ["The quick brown fox jumps over the lazy dog.", "Python Exercises."]

for s in strings:
    print(f"Words containing 'z' in '{s}': {match_word_with_z(s)}")
