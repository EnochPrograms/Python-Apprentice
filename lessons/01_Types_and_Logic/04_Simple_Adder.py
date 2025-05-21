import tkinter as tk
from tkinter import simpledialog, messagebox

# Create a window object
window = tk.Tk()

# Hide the window
window.withdraw()

# Ask the user for the first number
num1 = simpledialog.askfloat("Input", "Enter the first number:")

# Ask the user for the second number
num2 = simpledialog.askfloat("Input", "Enter the second number:")

# Display the sum of the two numbers
sum_result = num1 + num2
messagebox.showinfo("Result", f"The sum of {num1} and {num2} is {sum_result}")

# Keep the window open (optional, but usually unnecessary in this context)
window.mainloop()