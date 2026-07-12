BUDGET_FILE = "budget.txt"


def get_budget():
    try:
        with open(BUDGET_FILE, "r") as file:
            return float(file.read().strip())
    except (FileNotFoundError, ValueError):
        return None


def set_budget(amount):
    with open(BUDGET_FILE, "w") as file:
        file.write(str(amount))


def has_budget():
    budget = get_budget()
    return budget is not None and budget > 0
