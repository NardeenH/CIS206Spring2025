import re

def match_pattern(s):
    pattern = re.compile(r"^ab+$")  # Matches 'a' followed by one or more 'b's
    return bool(pattern.fullmatch(s))

# Test cases
strings = ["ab", "abc", "a", "ab", "abb"]

for s in strings:
    print(f"'{s}' matches pattern: {match_pattern(s)}")
