import re

def match_pattern(s):
    pattern = re.compile(r"^[a-z]+_[a-z]+$")  # Matches sequences of lowercase letters joined by an underscore
    return bool(pattern.fullmatch(s))

# Test cases
strings = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]

for s in strings:
    print(f"'{s}' matches pattern: {match_pattern(s)}")
