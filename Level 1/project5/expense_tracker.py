import datetime

def add_expense():

    categories = {
        1: "Groceries",
        2: "Dining",
        3: "Shopping",
        4: "Transport",
        5: "Other"
    }

    try:
        date = input("Enter the date (YYYY-MM-DD) or press enter for today: ".strip())
        if not date:
            date = str(datetime.date.today())
        else:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        
        amount = float(input("Enter the expense amount: ".strip()))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        print("\nChose a category: ")
        for key, value in categories.items():
            print(f"{key}. {value}")
        
        category_number = int(input("Enter category number: ".strip()))
        if category_number not in categories:
            print("Invalid category number. Please try again.")
            return
        category = categories[category_number]
        with open("expenses.txt", "a") as file:
            file.write(f"{date} - ${amount:.2f} - {category}\n")
        print("Expense added successfully")

    except ValueError as e:
        print(f"Invalid input: {e}")

def read_expenses():
    try:
        with open("expenses.txt", "r") as file:
            content = file.readlines()
        if not content:
            print("No expenses recorded")
            return
        print("\nAll expenses: ")
        for line in content:
            print(line.strip())
    except FileNotFoundError:
        print("No expenses found. Add expenses first")

def main():
    while True:
        try:
            option = int (input("Choose an option: \n1. Add Expense\n2. View Expenses\n3. Exit\n"))
        except ValueError:
            print("Chose option between 1 and 3")
            continue
            
        if (option == 1):
            add_expense()
        elif (option == 2):
            read_expenses()
        elif (option == 3):
            print("Program was closed. Bye!")
            break
        else:
            print("Chose option between 1 and 3")
        print("\n")

if __name__ == "__main__":
    main()