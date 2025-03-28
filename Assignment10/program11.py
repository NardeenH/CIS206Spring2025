import re

def extract_date_from_url(url):
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', url)
    if match:
        year, month, day = match.groups()
        return year, month, day
    return None

# Test case
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

date_parts = extract_date_from_url(url)
if date_parts:
    print(f"Extracted Date - Year: {date_parts[0]}, Month: {date_parts[1]}, Day: {date_parts[2]}")
else:
    print("No date found in URL")
