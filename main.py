import pandas as pd
import matplotlib.pyplot as plt
import os
FILE = "expenses.csv"
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE, index=False)
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc): ")
    amount = float(input("Enter amount: "))
    new_data = pd.DataFrame([[date, category, amount]],
                            columns=["Date", "Category", "Amount"])
    new_data.to_csv(FILE, mode='a', header=False, index=False)
    print("Expense added successfully!")
def view_expenses():
    df = pd.read_csv(FILE)
    print("\nAll Expenses:")
    print(df)
def analyze_expenses():
    df = pd.read_csv(FILE)
    print("\nTotal Spending:", df["Amount"].sum())
    print("\nCategory-wise Spending:")
    print(df.groupby("Category")["Amount"].sum())
def show_graph():
    df = pd.read_csv(FILE)
    df.groupby("Category")["Amount"].sum().plot(kind='bar')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Analyze Expenses")
    print("4. Show Graph")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        analyze_expenses()
    elif choice == '4':
        show_graph()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")