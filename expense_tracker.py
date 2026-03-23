# Expense Tracker - Save to Date-wise File on Save

# List to store expenses temporarily in memory
expenses = []

# Function to add a new expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added in memory!")

# Function to view all current expenses in memory
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nCurrent Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']}")

# Function to calculate total expenses in memory
def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses in memory: {total}")

# Function to save all expenses to a date-named file
def save_expenses():
    if not expenses:
        print("No expenses to save.")
        return
    
    date = input("Enter date to save expenses (YYYY-MM-DD): ")
    filename = f"{date}.txt"
    
    with open(filename, "w") as file:
        for expense in expenses:
            file.write(f"{expense['amount']},{expense['category']}\n")
    
    print(f"All expenses saved to {filename}!")
    # Clear memory after saving if desired
    expenses.clear()

# Main menu
def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Save Expenses and Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            save_expenses()
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()