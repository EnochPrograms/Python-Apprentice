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
elif age >= 0 and age <= 2:
    message = "You are a baby."
elif age >= 3 and age <= 5:
    message = "You are a toddler."
elif age >= 6 and age <= 12:
    message = "You are a child."
elif age >= 13 and age <= 19:
    message = "You are a teen."
elif age >= 20 and age <= 64:
    message = "You are an adult."
elif age >= 65 and age <= 105:
    message = "You are a senior."
else:
    message = "go die in a hole you bag of bones"

# Show the message to the user
messagebox.showinfo("What you are", message)