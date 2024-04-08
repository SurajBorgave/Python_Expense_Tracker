import tkinter as tk
from tkinter import messagebox


class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")
        self.master.configure(bg='#f0f0f0')  # Setting background color

        self.expenses = []

        self.label_amount = tk.Label(master, text="Enter amount (Rupees):", bg='#f0f0f0')
        self.label_amount.grid(row=0, column=0, padx=10, pady=5)

        self.entry_amount = tk.Entry(master)
        self.entry_amount.grid(row=0, column=1, padx=10, pady=5)

        self.label_description = tk.Label(master, text="Enter description:", bg='#f0f0f0')
        self.label_description.grid(row=1, column=0, padx=10, pady=5)

        self.entry_description = tk.Entry(master)
        self.entry_description.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add Expense", command=self.add_expense, bg='#4CAF50', fg='white')
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.listbox = tk.Listbox(master, bg='#ffffff', selectmode=tk.SINGLE)
        self.listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.delete_button = tk.Button(master, text="Delete Expense", command=self.delete_expense, bg='#f44336',
                                       fg='white')
        self.delete_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.clear_button = tk.Button(master, text="Clear Expenses", command=self.clear_expenses, bg='#f44336',
                                      fg='white')
        self.clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.total_label = tk.Label(master, text="Total:", bg='#f0f0f0')
        self.total_label.grid(row=6, column=0, padx=10, pady=5)

        self.total_text = tk.Text(master, height=1, width=20, bg='#ffffff')
        self.total_text.grid(row=6, column=1, padx=10, pady=5)

    def add_expense(self):
        amount = self.entry_amount.get()
        description = self.entry_description.get()

        if amount and description:
            self.expenses.append((float(amount), description))
            self.listbox.insert(tk.END, f"{amount} Rupees - {description}")
            self.update_total()
            self.entry_amount.delete(0, tk.END)
            self.entry_description.delete(0, tk.END)
        else:
            messagebox.showwarning("Incomplete Entry", "Please enter both amount and description.")

    def delete_expense(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.expenses[index]
            self.listbox.delete(index)
            self.update_total()
        else:
            messagebox.showwarning("No Expense Selected", "Please select an expense to delete.")

    def clear_expenses(self):
        if self.expenses:
            self.expenses = []
            self.listbox.delete(0, tk.END)
            self.update_total()
            messagebox.showinfo("Expenses Cleared", "All expenses cleared successfully.")
        else:
            messagebox.showinfo("No Expenses", "No expenses to clear.")

    def update_total(self):
        total = sum(expense[0] for expense in self.expenses)
        self.total_text.delete(1.0, tk.END)
        self.total_text.insert(tk.END, f"{total:.2f} Rupees")


def main():
    root = tk.Tk()
    root.configure(bg='#f0f0f0')  # Setting background color
    app = ExpenseTracker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
