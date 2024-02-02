import tkinter as tk
from tkinter import filedialog
import pandas as pd

class ExpensesCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Expenses Calculator")

        self.load_button = tk.Button(master, text="Load CSV", command=self.load_csv)
        self.load_button.pack()

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_expenses)
        self.calculate_button.pack()

    def load_csv(self):
        file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
        self.df = pd.read_csv(file_path)
        print("CSV Loaded Successfully!")

    def calculate_expenses(self):
        if hasattr(self, 'df'):
            total_expenses = self.df['Amount'].sum()
            print(f'Total Expenses: ${total_expenses:.2f}')
        else:
            print("No CSV file loaded. Please load a CSV file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpensesCalculator(root)
    root.mainloop()
