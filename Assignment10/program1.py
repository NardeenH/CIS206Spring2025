import re

def is_valid_string(s):
    pattern = re.compile("^[A-Za-z0-9]+$")
    return bool(pattern.match(s))

# Test cases
strings = ["ABCDEFabcdef123450", "*&%@#!}{"]

for s in strings:
    print(f"'{s}' is valid: {is_valid_string(s)}")
