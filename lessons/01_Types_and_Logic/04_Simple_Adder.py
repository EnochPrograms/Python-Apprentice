import tkinter as tk
from tkinter import simpledialog, messagebox

# Create a window object
window = tk.Tk()
window.withdraw()

Number1 = simpledialog.askinteger("First Number", "Enter the first number.")
Number2 = simpledialog.askinteger("Second Number", "Enter the second number.")

Answer = Number1 + Number2

messagebox.showinfo("Your answer is", Answer)