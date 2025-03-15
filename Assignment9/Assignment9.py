import csv

def load_customers(filename):
    customers = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            for x in reader:
                if len(x) >= 3:
                    customers.append({
                        "CompanyName": x[0],
                        "ContactName": x[1],
                        "Phone": x[2]
                    })
        customers.sort(key=lambda x: x["CompanyName"])  # Sort by company name by default
    except Exception as e:
        print(f"An error occurred: {e}")
    return customers

def display_customers(customers, sort_by):
    if sort_by not in {"CompanyName", "ContactName"}:
        print("Invalid sort option.")
        return
    sorted_customers = sorted(customers, key=lambda x: x[sort_by])
    for customer in sorted_customers:
        print(f"Company:    {customer['CompanyName']}\nContact:    {customer['ContactName']}\nPhone:      {customer['Phone']}\n")

def search_customers(customers, search_term, search_by):
    if search_by not in {"CompanyName", "ContactName"}:
        print("Invalid search field.")
        return
    results = [customer for customer in customers if search_term.lower() in customer[search_by].lower()]
    if results:
        for customer in results:
            print(f"Company:    {customer['CompanyName']}\nContact:    {customer['ContactName']}\nPhone:      {customer['Phone']}\n")
    else:
        print("No matching records found.")

def main():
    filename = "northwind_customers.csv"  # Ensure the file exists in the working directory
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
            display_customers(customers, "CompanyName")
        elif choice == "2":
            display_customers(customers, "ContactName")
        elif choice == "3":
            term = input("Enter company name or part of it: ")
            search_customers(customers, term, "CompanyName")
        elif choice == "4":
            term = input("Enter contact name or part of it: ")
            search_customers(customers, term, "ContactName")
        elif choice == "5":
            print("Bye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
