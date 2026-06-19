FILENAME = "expense.txt"

def save_expense(item,cost):
    with open(FILENAME,"a") as f:
        f.write(f"{item},{cost}\n")

def read_expense():
    try:
        with open(FILENAME) as f:
            print("--CURRENT EXPENSES--")
            total = 0
            for line in f:
                cleared_line = line.strip()
                if cleared_line:
                    item,cost_str = cleared_line.split(",")
                    cost =float(cost_str)
                    print(f"{item} : ${cost}")
                    total +=cost
            print("-"*25)
            print(f"Total expenses : ${total}")
    except FileNotFoundError:
        # If the file doesn't exist yet, it means they haven't bought anything
        print("\nNo expenses recorded yet. Your file is empty!")