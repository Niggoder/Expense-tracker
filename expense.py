import tkinter as tk
from tkinter import messagebox
import json

# Initialize root window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x500")

# Global dictionary to store expenses
expenses = {}

# Function to add an expense
def add_expense():
    name = expense_entry.get().strip()
    category = category_entry.get().strip()
    amount = amount_entry.get().strip()

    if not name or not category or not amount:
        result_label.config(text="Please fill out all the fields!", fg="red")
        return

    try:
        amount = float(amount)
    except ValueError:
        result_label.config(text="Amount must be a number!", fg="red")
        return

    if category not in expenses:
        expenses[category] = []
    expenses[category].append((name, amount))

    result_label.config(text=f"Added: {name} - Rs. {amount:.2f} to {category}", fg="green")
    expense_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Function to view all expenses
def view_expenses():
    view_window = tk.Toplevel(root)
    view_window.title("All Expenses")
    view_window.geometry("400x300")

    text_widget = tk.Text(view_window, wrap=tk.WORD, font=("Helvetica", 10))
    text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    if not expenses:
        text_widget.insert(tk.END, "No Expenses to display!")
    else:
        for category, items in expenses.items():
            text_widget.insert(tk.END, f"Category: {category}\n")
            for name, amount in items:
                text_widget.insert(tk.END, f"  - {name}: Rs. {amount:.2f}\n")
            text_widget.insert(tk.END, "\n")

# Function to delete an expense
def delete_expense():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Expenses")
    delete_window.geometry("300x200")

    tk.Label(delete_window, text="Category:").pack(pady=5)
    category_entry = tk.Entry(delete_window, width=30)
    category_entry.pack(pady=5)

    tk.Label(delete_window, text="Expense Name:").pack(pady=5)
    expense_entry = tk.Entry(delete_window, width=30)
    expense_entry.pack(pady=5)

    def confirm_delete():
        category = category_entry.get().strip()
        expense_name = expense_entry.get().strip()

        if not category or not expense_name:
            tk.Label(delete_window, text="Please fill out all fields!", fg="red").pack(pady=5)
            return

        if category in expenses:
            for item in expenses[category]:
                if item[0] == expense_name:
                    expenses[category].remove(item)
                    if not expenses[category]:
                        del expenses[category]
                    tk.Label(delete_window, text="Expense deleted successfully!", fg="green").pack(pady=5)
                    return
            tk.Label(delete_window, text="Expense not found in category!", fg="red").pack(pady=5)
        else:
            tk.Label(delete_window, text="Category not found!", fg="red").pack(pady=5)

    confirm_button = tk.Button(delete_window, text="Confirm Delete", command=confirm_delete)
    confirm_button.pack(pady=10)

# Function to save expenses to a file
def save_to_file():
    try:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)
        result_label.config(text="Expenses saved successfully!", fg="green")
    except Exception as e:
        result_label.config(text=f"Error saving expenses: {e}", fg="red")

# Function to load expenses from a file
def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        result_label.config(text="Expenses loaded successfully!", fg="green")
    except FileNotFoundError:
        result_label.config(text="No saved expenses found!", fg="red")
    except Exception as e:
        result_label.config(text=f"Error loading expenses: {e}", fg="red")

# UI Elements
expense_label = tk.Label(root, text="Expense Name:", font=("Helvetica", 12))
expense_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

expense_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
expense_entry.grid(row=0, column=1, padx=10, pady=10)

category_label = tk.Label(root, text="Category:", font=("Helvetica", 12))
category_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

category_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
category_entry.grid(row=1, column=1, padx=10, pady=10)

amount_label = tk.Label(root, text="Amount:", font=("Helvetica", 12))
amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

amount_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Expense", font=("Helvetica", 12), command=add_expense)
add_button.grid(row=3, column=0, padx=10, pady=10)

view_button = tk.Button(root, text="View Expenses", font=("Helvetica", 12), command=view_expenses)
view_button.grid(row=3, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Expense", font=("Helvetica", 12), command=delete_expense)
delete_button.grid(row=4, column=0, padx=10, pady=10)

save_button = tk.Button(root, text="Save Expenses", font=("Helvetica", 12), command=save_to_file)
save_button.grid(row=4, column=1, padx=10, pady=10)

load_button = tk.Button(root, text="Load Expenses", font=("Helvetica", 12), command=load_expenses)
load_button.grid(row=5, column=0, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), command=root.quit)
exit_button.grid(row=5, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
