import os

def add_expense():
    category=input("Category: ")
    amount=input("Amount: ")
    with open("expense.txt","a") as file:
        file.write(f"{category},{amount}\n")

def main():
    os.system('clear' if os.name != 'nt' else 'cls')

    print("""1. Add Expense
2. View Expenses
3. Show Total
4. Search by Category
5. Exit""")

    choise=input("Enter choise: ")


main()