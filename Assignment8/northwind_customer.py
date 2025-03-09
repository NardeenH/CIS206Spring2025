import csv

def load_customers(filename):
    customers = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                if len(row) >= 3:  
                    customers.append((row[0], row[1], row[2]))  # https://stackoverflow.com/questions/32238196/how-does-the-key-argument-in-pythons-sorted-function-work
        customers.sort(key=lambda x: x[0])  
    except Exception as e:
        print(f"An error occurred: {e}")
    return customers

def display_customers(customers, sort_by):
    """Displays customers sorted by the specified field."""
    if sort_by == "company":
        sorted_customers = sorted(customers, key=lambda x: x[0])
    elif sort_by == "contact":
        sorted_customers = sorted(customers, key=lambda x: x[1])
    else:
        print("Invalid sort option.")
        return
    
    for company, contact, phone in sorted_customers:
        print(f"Company: {company}, Contact: {contact}, Phone: {phone}")

def search_customers(customers, search_term, search_by):
    results = []
    for company, contact, phone in customers:
        if search_by == "company" and search_term.lower() in company.lower():
            results.append((company, contact, phone))
        elif search_by == "contact" and search_term.lower() in contact.lower():
            results.append((company, contact, phone))
    
    if results:
        for company, contact, phone in results:
            print(f"Company: {company}, Contact: {contact}, Phone: {phone}")
    else:
        print("No matching records found.")

def main():
    filename = "northwind_customers.csv"  
    customers = load_customers(filename)

    while True:
        print("\nMenu:")
        print("1. Display customers sorted by company name")
        print("2. Display customers sorted by contact name")
        print("3. Search customers by company name")
        print("4. Search customers by contact name")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_customers(customers, "company")
        elif choice == "2":
            display_customers(customers, "contact")
        elif choice == "3":
            term = input("Enter company name or part of it: ")
            search_customers(customers, term, "company")
        elif choice == "4":
            term = input("Enter contact name or part of it: ")
            search_customers(customers, term, "contact")
        elif choice == "5":
            print("bye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

