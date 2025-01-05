# Expense-tracker
The Expense Tracker application is a graphical user interface (GUI) program built using Python's tkinter library. It allows users to efficiently track their expenses by categorizing them, calculating totals, and saving/loading data for later use.  
Features

Add Expense:

Input expense details including name, category, and amount.

Automatically organizes expenses by category.

View Expenses:

Displays all expenses grouped by category in a new window.

Delete Expense:

Remove a specific expense by providing the category and name.

Save/Load:

Save expenses to a JSON file for persistence.

Load expenses from a previously saved file.

Clear Error Messages:

Handles missing or invalid inputs gracefully.

How to Use

Prerequisites

Python 3.x

No additional libraries are required as the application uses built-in Python modules.

Running the Application

Save the code into a file, e.g., expense_tracker.py.

Run the program using the following command:

python expense_tracker.py

The application window will open, providing the following options:

Add an expense

View all expenses

Delete a specific expense

Save/Load expenses

Adding an Expense

Enter the expense name in the Expense Name field.

Enter the category in the Category field.

Enter the amount in the Amount field.

Click the Add Expense button to save the details.

Viewing Expenses

Click the View Expenses button.

A new window will open, displaying all saved expenses grouped by category.

Deleting an Expense

Click the Delete Expense button.

A new window will open prompting you to input the category and expense name to delete.

Fill in the fields and confirm the deletion.

Saving Expenses

Click the Save Expenses button.

All current expenses will be saved to a file named expenses.json in the program's directory.

Loading Expenses

Click the Load Expenses button.

If a file named expenses.json exists, it will load the saved expenses into the application.

Exiting the Application

Click the Exit button to close the application.

Code Structure

Main Components:

Add Expense Functionality: Adds new expenses to a dictionary.

View Expenses Functionality: Displays all expenses in a new window.

Delete Expense Functionality: Deletes specific expenses based on user input.

Save/Load Functionality: Saves and loads data to/from a JSON file.

Expense Data Structure

The expenses are stored in a dictionary:

{
    "Category1": [("Expense1", amount1), ("Expense2", amount2)],
    "Category2": [("Expense3", amount3)]
}

Error Handling

Invalid or empty inputs are flagged with error messages.

The application gracefully handles cases where no expenses are available to view or delete.

Future Enhancements

Add graphs/charts to visualize spending trends.

Support for exporting data to CSV or Excel files.

Integration with a database for enhanced data management.

Screenshots:
![image](https://github.com/user-attachments/assets/e4a90096-3118-49f1-8e9c-f4cf819bf1f6)
