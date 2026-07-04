import os

def main():
    os.system('clear' if os.name != 'nt' else 'cls')

    print("""1. Add Expense
2. View Expenses
3. Show Total
4. Search by Category
5. Exit""")


main()