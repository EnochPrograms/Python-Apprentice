from tkinter import messagebox, simpledialog, Tk  # Import the modules we need

# Create and hide the main window
window = Tk()
window.withdraw()

# Ask the user for their age
age = simpledialog.askinteger("Your Age", "How old are you?")


my_age = 13  # this is my age, to give that custom message :D

# Decide what message to show
if age == my_age:
    message = "we are the same age!"
elif age < 2:
    message = "You are a baby."
elif age < 5:
    message = "You are a toddler."
elif age < 12:
    message = "You are a child."
elif age < 19:
    message = "You are a teen."
elif age < 64:
    message = "You are an adult."
elif age < 105:
    message = "You are a senior."
else:
    message = "wow, thats crazy"

# Show the message to the user
messagebox.showinfo("Your age makes you a:", message)