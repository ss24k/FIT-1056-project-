import tkinter as tk
from PIL import Image, ImageTk
from user import User
from admin import AdminGUI
from teacher import Teacher

# Function to handle the Student Menu
def handle_student_menu():
    text_label.config(text="Student Menu")  # Change the displayed text
    welcome_label.config(text="Welcome to Code Venture - Student")  # Update welcome message
    # Add student-specific functionality here (user window creation)
    user_window = tk.Toplevel(root)
    user_menu = User(user_window)

# Function to handle the Admin Menu
def handle_admin_menu():
    text_label.config(text="Admin Menu")  # Change the displayed text
    welcome_label.config(text="Welcome to Code Venture - Admin")  # Update welcome message
    # Add admin-specific functionality here (admin window creation)
    admin_window = tk.Toplevel(root)
    admin_menu = AdminGUI(admin_window)

# Function to handle the Parent Menu
def handle_parent_menu():
    text_label.config(text="Parent Menu")  # Change the displayed text
    welcome_label.config(text="Welcome to Code Venture - Parent")  # Update welcome message
    # Add parent-specific functionality here (user window creation)
    user_window = tk.Toplevel(root)
    user_menu = User(user_window)

# Function to handle the Teacher Menu
def handle_teacher_menu():
    text_label.config(text="Teacher Menu")  # Change the displayed text
    welcome_label.config(text="Welcome to Code Venture - Teacher")  # Update welcome message
    # Add teacher-specific functionality here (teacher window creation)
    teacher_window = tk.Toplevel(root)
    teacher_menu = Teacher(teacher_window)

# Create the main Tkinter window
root = tk.Tk()
root.title("Code Venture")

# Create a frame to hold the image
image_frame = tk.Frame(root)
image_frame.grid(row=0, column=0, columnspan=2)

# Load the image from the file and display it
image_path = "images/download.jpeg"  # Path to the image file
image = Image.open(image_path)
image = ImageTk.PhotoImage(image)
image_label = tk.Label(image_frame, image=image)
image_label.pack()

# Create labels to display welcome text
welcome_label = tk.Label(root, text="Welcome to Code Venture", font=("Helvetica", 25))
welcome_label.grid(row=1, column=0, columnspan=2)

text_label = tk.Label(root, text="Student Menu", font=("Helvetica", 26))
text_label.grid(row=2, column=0, columnspan=2)

# Button styling
button_font = ("Helvetica", 14)
button_padx = 10
button_pady = 5

# Create a frame to hold the menu buttons
button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=2)

# Create buttons for different menus
student_button = tk.Button(button_frame, text="Student Menu", command=handle_student_menu, font=button_font,
                           padx=button_padx, pady=button_pady)
student_button.pack(side="left")

admin_button = tk.Button(button_frame, text="Admin Menu", command=handle_admin_menu, font=button_font,
                         padx=button_padx, pady=button_pady)
admin_button.pack(side="left")

parent_button = tk.Button(button_frame, text="Parent Menu", command=handle_parent_menu, font=button_font,
                          padx=button_padx, pady=button_pady)
parent_button.pack(side="left")

teacher_button = tk.Button(button_frame, text="Teacher Menu", command=handle_teacher_menu, font=button_font,
                           padx=button_padx, pady=button_pady)
teacher_button.pack(side="left")

# Create an exit button to close the application
exit_button = tk.Button(root, text="Exit", command=root.quit, font=button_font, padx=button_padx, pady=button_pady)
exit_button.grid(row=3, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()

