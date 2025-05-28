"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules

# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

# Ask the user for the second number

# Ask the user for the math operation

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open

import tkinter as tk
from tkinter import simpledialog, messagebox

# Create a window object
window = tk.Tk()
window.withdraw()

Number1 = simpledialog.askinteger("First Number", "Enter the first number.")
Number2 = simpledialog.askinteger("Second Number", "Enter the second number.")
OperatorUsed = simpledialog.askstring("What would you like to do with these numbers?", "+, -, /, *?")



if OperatorUsed == "+":
    messagebox.showinfo (str(Number1 + Number2))

elif OperatorUsed == "-":
    messagebox.showinfo (str(Number1 - Number2))

elif OperatorUsed == "*":
    messagebox.showinfo(str (Number1 * Number2))

elif OperatorUsed == "/":
    messagebox.showinfo(str (Number1 / Number2))

