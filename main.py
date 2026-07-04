import os
filename="expenses.txt"
def add_expense():
    category=input("Category: ")
    amount=input("Amount: ")
    with open("expenses.txt","a") as file:
        file.write(f"{category},{amount}\n")

def view_expenses():
    with open("expenses.txt","r") as file:
        for line in file:
            line=line.strip()
            parts=line.split(",")
            print(f"Category: {parts[0]}\tAmount: {parts[1]}")

def show_total():
    total=0
    with open("expenses.txt","r") as file:
        for line in file:
            line=line.strip()
            parts=line.split(",")
            price=float(parts[1])
            total+=price
    print(f"Total expenses: {total}")

def search_category():
    search=input("Enter the category to search for: ")
    found=False
    with open("expenses.txt","r") as file:
        for line in file:
            line=line.strip()
            parts=line.split(",")
            if search.lower() == parts[0].lower():
                print(f"{parts[0]} - {parts[1]}")
                found=True
        if not found:
            print("No expenses found.")



def main():
    os.system('clear' if os.name != 'nt' else 'cls')

    print("""1. Add Expense
2. View Expenses
3. Show Total
4. Search by Category
5. Exit""")

    choise=input("Enter choise: ")


main()