import sqlite3
from datetime import datetime

# Initialize SQLite database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create expenses table
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY,
             amount REAL,
             category TEXT,
             date DATE)''')
conn.commit()

# Function to add an expense
def add_expense(amount, category, date):
    try:
        c.execute('''INSERT INTO expenses (amount, category, date)
                     VALUES (?, ?, ?)''', (amount, category, date))
        conn.commit()
        print("Expense added successfully!")
    except sqlite3.Error as e:
        print("Error adding expense:", e)

# Function to get monthly summary
def monthly_summary(month, year):
    try:
        c.execute('''SELECT SUM(amount) FROM expenses
                     WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?''', (month, year))
        total = c.fetchone()[0]
        print(f"Total expenses for {month}-{year}: ${total}")
    except sqlite3.Error as e:
        print("Error fetching monthly summary:", e)

# Function to get category-wise expenditure
def category_expenditure(category):
    try:
        c.execute('''SELECT SUM(amount) FROM expenses
                     WHERE category = ?''', (category,))
        total = c.fetchone()[0]
        print(f"Total expenses for {category}: ${total}")
    except sqlite3.Error as e:
        print("Error fetching category-wise expenditure:", e)

# Main function to interact with user
def main():
    print("Welcome to Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. Monthly Summary")
        print("3. Category-wise Expenditure")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(amount, category, date)

        elif choice == '2':
            month = input("Enter month (MM): ")
            year = input("Enter year (YYYY): ")
            monthly_summary(month, year)

        elif choice == '3':
            category = input("Enter category: ")
            category_expenditure(category)

        elif choice == '4':
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
