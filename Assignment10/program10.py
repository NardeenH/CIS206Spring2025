import re

def swap_whitespace_underscore(text):
    if " " in text:
        return text.replace(" ", "_")
    elif "_" in text:
        return text.replace("_", " ")
    return text

# Test cases
texts = ["Regular Expressions", "Code_Examples"]
for t in texts:
    print(f"Original: {t} -> Modified: {swap_whitespace_underscore(t)}")
