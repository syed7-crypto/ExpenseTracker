from budget_manager import get_budget

EXPENSES_FILE = "expenses.txt"


def get_total_expenses():
    total = 0
    try:
        with open(EXPENSES_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                total += float(parts[1])
    except FileNotFoundError:
        pass
    return total


def check_budget_alerts():
    budget = get_budget()
    if budget is None or budget <= 0:
        return

    total = get_total_expenses()

    if total >= budget:
        print(f"\n*** WARNING: You have exceeded your monthly budget! "
              f"(${total:.2f} / ${budget:.2f}) ***")
    elif total >= budget * 0.8:
        print(f"\n*** ALERT: You have used {total / budget * 100:.1f}% of your monthly budget "
              f"(${total:.2f} / ${budget:.2f}) ***")
