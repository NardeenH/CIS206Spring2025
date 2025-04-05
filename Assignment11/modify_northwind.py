import sqlite3

def connect_to_database():
    return sqlite3.connect('northwind.db')

def get_table_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    return tables

def show_table_data(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    print(f"\nShowing table: {table_name}")
    print(" | ".join(columns))
    for index, row in enumerate(rows):
        print(f"{index + 1}. {row}")

    return rows, columns

def insert_data(conn, table_name, columns):
    values = []
    for col in columns:
        value = input(f"Enter value for '{col}': ")
        values.append(value)

    placeholders = ", ".join("?" for _ in columns)
    sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
    try:
        conn.execute(sql, values)
        conn.commit()
        print("New row inserted.")
    except Exception as e:
        print("Insert failed:", e)

def update_data(conn, table_name, rows, columns):
    try:
        row_number = int(input("Enter row number to update: ")) - 1
        if row_number not in range(len(rows)):
            print("Invalid row number.")
            return

        column_to_edit = input(f"Enter column name to update ({', '.join(columns)}): ")
        if column_to_edit not in columns:
            print("Invalid column name.")
            return

        new_value = input("Enter new value: ")
        row_id_column = columns[0]
        row_id_value = rows[row_number][0]

        sql = f"UPDATE {table_name} SET {column_to_edit} = ? WHERE {row_id_column} = ?"
        conn.execute(sql, (new_value, row_id_value))
        conn.commit()
        print("Row updated.")
    except Exception as e:
        print("Update failed:", e)

def delete_data(conn, table_name, rows, columns):
    """Delete a row from the table."""
    try:
        row_number = int(input("Enter row number to delete: ")) - 1
        if row_number not in range(len(rows)):
            print("Invalid row number.")
            return

        row_id_column = columns[0]
        row_id_value = rows[row_number][0]

        sql = f"DELETE FROM {table_name} WHERE {row_id_column} = ?"
        conn.execute(sql, (row_id_value,))
        conn.commit()
        print("Row deleted.")
    except Exception as e:
        print("Delete failed:", e)

def main():
    print("Welcome to the Northwind Database Tool")
    conn = connect_to_database()

    tables = get_table_names(conn)
    print("\nAvailable Tables:")
    for i, table in enumerate(tables):
        print(f"{i + 1}. {table}")

    try:
        table_choice = int(input("Select a table by number: ")) - 1
        selected_table = tables[table_choice]
    except:
        print("Invalid table number.")
        return

    rows, columns = show_table_data(conn, selected_table)

    action = input("Choose an action - (I)nsert, (U)pdate, or (D)elete: ").strip().upper()

    if action == 'I':
        insert_data(conn, selected_table, columns)
    elif action == 'U':
        update_data(conn, selected_table, rows, columns)
    elif action == 'D':
        delete_data(conn, selected_table, rows, columns)
    else:
        print("Invalid choice.")

    conn.close()
    print("Program finished.")

if __name__ == "__main__":
    main()
