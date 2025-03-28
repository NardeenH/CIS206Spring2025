import re

def replace_delimiters(text):
    return re.sub(r'[\s,\.]', ':', text)
text = 'Python Exercises, PHP exercises.'
modified_text = replace_delimiters(text)
print("Modified text:", modified_text)
