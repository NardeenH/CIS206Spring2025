import sqlite3

# Connect to the database
conn = sqlite3.connect('northwind.db')  # Make sure this file is in the same folder
cursor = conn.cursor()

# --- READ Operation ---
cursor.execute("SELECT CustomerID, CompanyName FROM Customers LIMIT 5")
customers = cursor.fetchall()
print("Customers:\n", customers)

# --- INSERT Operation ---
cursor.execute("INSERT INTO Customers (CustomerID, CompanyName) VALUES ('NARDN', 'Nardeen Inc.')")

# --- UPDATE Operation ---
cursor.execute("UPDATE Customers SET CompanyName = 'Updated Inc.' WHERE CustomerID = 'NARDN'")

# --- DELETE Operation ---
cursor.execute("DELETE FROM Customers WHERE CustomerID = 'NARDN'")

# Save and close
conn.commit()
conn.close()
