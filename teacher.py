

import tkinter as tk
from tkinter import messagebox, simpledialog

class Teacher:

    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Panel")

        self.logged_in = False

        # Predefined teacher usernames and passwords
        self.tech_users = ["teach1", "teach2", "teach3"]
        self.tech_pass = ["teach1", "teach2", "teach3"]

        # Username entry field
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        # Password entry field with password masking
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Login button
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

        # "Add Content" button, initially disabled
        self.add_content_button = tk.Button(root, text="Add Content", command=self.add_content, state="disabled")
        self.add_content_button.pack()

        # Return to the main menu button
        self.return_to_main_menu_button = tk.Button(root, text="Return to Main Menu", command=self.return_to_main_menu)
        self.return_to_main_menu_button.pack()

    def login(self):
        # Method to handle teacher login
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the entered credentials match any predefined teacher credentials
        if (username in self.tech_users) and (password == self.tech_pass[self.tech_users.index(username)]):
            self.logged_in = True
            messagebox.showinfo("Login", "Logged in successfully.")
            # Enable the "Add Content" button when logged in
            self.add_content_button.config(state="normal")
        else:
            messagebox.showerror("Login Error", "Invalid credentials.")

    def add_content(self):
        if self.logged_in:
            # Method to add content to a text file
            topic_number = simpledialog.askstring("Add Content", "Enter topic number:")
            topic_title = simpledialog.askstring("Add Content", "Enter topic name:")
            file_name = "topic " + topic_number + ".txt"
            with open(file_name, "a") as f:
                messagebox.showinfo("Add Content", "You can now add the content. To stop adding content, type 'no more content'.")
                f.write(topic_title + "\n")
                while True:
                    content = simpledialog.askstring("Add Content", "Enter content (type 'no more content' to stop):")
                    if content == "no more content":
                        break
                    else:
                        f.write(content + "\n")
            messagebox.showinfo("Content Added", f"Content added to the text file {file_name}.")
        else:
            messagebox.showerror("Access Denied", "You must be logged in to add content.")

    def return_to_main_menu(self):
        # Method to return to the main menu
        self.root.destroy()  # Close the user window

    def close(self):
        # Method to close the teacher GUI
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    teacher_gui = Teacher(root)
    root.mainloop()
