import re

def match_pattern(s):
    pattern = re.compile(r"^\w+")  # Matches a word at the beginning of the string
    match = pattern.match(s)
    return match.group() if match else None

# Test cases
strings = ["The quick brown fox jumps over the lazy dog.", " The quick brown fox jumps over the lazy dog."]

for s in strings:
    print(f"First word in '{s}': {match_pattern(s)}")
