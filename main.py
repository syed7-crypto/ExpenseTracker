import os
from budget_manager import set_budget, get_budget
from alerts import check_budget_alerts

filename="expenses.txt"

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def add_expense():
    category=input("Category: ")
    amount=float(input("Amount: "))
    with open(filename,"a") as file:
        file.write(f"{category},{amount}\n")

def view_expenses():
    with open(filename,"r") as file:
        for line in file:
            line=line.strip()
            parts=line.split(",")
            print(f"Category: {parts[0]}\tAmount: {parts[1]}")

def show_total():
    total=0
    with open(filename,"r") as file:
        for line in file:
            parts=line.strip().split(",")
            price=float(parts[1])
            total+=price
    print(f"Total expenses: {total}")

def search_category():
    search=input("Enter the category to search for: ")
    found=False
    with open(filename,"r") as file:
        for line in file:
            parts=line.strip().split(",")
            if search.lower() == parts[0].lower():
                print(f"{parts[0]} - {parts[1]}")
                found=True
        if not found:
            print("No expenses found.")

def delete_category():
    delete=input("Enter category: ")
    found=[]
    with open(filename,"r") as file:
        lines = file.readlines()

        for index,line in enumerate(lines):
            parts=line.strip().split(",")
            if delete.lower() == parts[0].lower():
                found.append((index, parts))

        if not found:
            print("No such expenses found.")
            return
        
        print("Which expence to delete? ")
        for i,(original_index, parts) in enumerate(found, start=1):
            print(f"{i}. {parts[0]} - {parts[1]}")
        
        choice=int(input("Enter number: "))
        if choice < 1 or choice > len(found):
            print("Invalid choice!!")
            return
        line_to_delete = found[choice-1][0]

        lines.pop(line_to_delete)

        with open(filename, "w") as file:
                for line in lines:
                    file.write(line)
                print("Expense deleted successfully.")

def set_monthly_budget():
    try:
        amount = float(input("Enter monthly budget limit: $"))
        if amount <= 0:
            print("Budget must be greater than zero.")
            return
        set_budget(amount)
        print(f"Monthly budget set to ${amount:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def main():
    while True:
        clear_screen()

        print("""===== Expense Tracker =====""")
        check_budget_alerts()
        budget = get_budget()
        if budget is not None:
            print(f"Monthly budget: ${budget:.2f}")
        print("""
1. Add Expense
2. View Expenses
3. Show Total
4. Search by Category
5. Delete expense by Category
6. Set Monthly Budget
7. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            search_category()
        elif choice == "5":
            delete_category()
        elif choice == "6":
            set_monthly_budget()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")
main()