import json
import xml.etree.ElementTree as ET

def search_json(title):
    with open("books.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        books = data["books"] 
        for book in books:
            if book["title"].lower() == title.lower():
                return f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Available: {book['available']}"
        return "Title not found."

def search_xml(title):
    tree = ET.parse("books.xml")
    root = tree.getroot()
    for book in root.findall("book"):
        book_title = book.find("title").text
        if book_title.lower() == title.lower():
            author = book.find("author").text
            year = book.find("year").text
            available = book.find("available").text
            return f"Title: {book_title}, Author: {author}, Year: {year}, Available: {available}"
    return "Title not found."

file_type = input("Search in (json/xml)? ").strip().lower()
title = input("Enter the book title: ").strip()

if file_type == "json":
    print(search_json(title))
elif file_type == "xml":
    print(search_xml(title))
else:
    print("Invalid file type. Please choose 'json' or 'xml'.")
