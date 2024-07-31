
import tkinter as tk
from tkinter import messagebox
from verify import Verify
import sys
from studentFrame import StudentFrame
from ParentFrame import ParentFrame

class User:
    def __init__(self, root):
        self.root = root
        self.root.title("User Account Management")

        self.verify = Verify()
        self.user = None  # Initialize user instance

        # Create buttons for account actions
        self.create_account_button = tk.Button(root, text="Create Account", command=self.create_account)
        self.create_account_button.grid(row=0, column=0)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=1, column=0)

        self.help_button = tk.Button(root, text="Help", command=self.help)
        self.help_button.grid(row=2, column=0)

        # Create the "Return to Main Menu" button
        self.return_to_main_button = tk.Button(root, text="Return to Main Menu", command=self.return_to_main_menu)
        self.return_to_main_button.grid(row=3, column=0)

    def return_to_main_menu(self):
        # This method handles returning to the main menu.
        self.root.destroy()  # Close the user window

    def close(self):
        self.root.destroy()
        sys.exit()

    def create_account(self):
        # Create a new window for the account creation form
        create_account_window = tk.Toplevel(self.root)
        create_account_window.title("Create Account")

        # Add form elements for creating an account
        tk.Label(create_account_window, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(create_account_window)
        self.username_entry.grid(row=0, column=1)

        tk.Label(create_account_window,
                 text="Password (It should be at least 6 characters with one number, letter, and special character mandatory):").grid(
            row=1, column=0)
        self.password_entry = tk.Entry(create_account_window, show='*')  # Show asterisks for the password
        self.password_entry.grid(row=1, column=1)

        tk.Label(create_account_window, text="Date of Birth (dd:mm:yyyy):").grid(row=2, column=0)
        self.dob_entry = tk.Entry(create_account_window)
        self.dob_entry.grid(row=2, column=1)

        tk.Label(create_account_window, text="Email:").grid(row=3, column=0)
        self.email_entry = tk.Entry(create_account_window)
        self.email_entry.grid(row=3, column=1)

        tk.Label(create_account_window, text="First Name:").grid(row=4, column=0)
        self.firstname_entry = tk.Entry(create_account_window)
        self.firstname_entry.grid(row=4, column=1)

        tk.Label(create_account_window, text="Last Name:").grid(row=5, column=0)
        self.lastname_entry = tk.Entry(create_account_window)
        self.lastname_entry.grid(row=5, column=1)
        tk.Label(create_account_window, text="User Type:").grid(row=6, column=0)
        self.user_type_var = tk.StringVar(value="student")
        tk.Radiobutton(create_account_window, text="Student", variable=self.user_type_var, value="student").grid(row=6,
                                                                                                                 column=1)
        tk.Radiobutton(create_account_window, text="Parent", variable=self.user_type_var, value="parent").grid(row=6,
                                                                                                               column=2)

        # Create "Register" and "Back" buttons using grid
        tk.Button(create_account_window, text="Register", command=lambda: self.process_create_account(
            self.username_entry.get(), self.password_entry.get(), self.dob_entry.get(), self.email_entry.get(),
            self.firstname_entry.get(), self.lastname_entry.get(), self.user_type_var.get())).grid(row=7, column=0,
                                                                                                   columnspan=2)
        back_button = tk.Button(create_account_window, text="Back", command=create_account_window.destroy)
        back_button.grid(row=8, column=0, columnspan=2)

    def process_create_account(self, username, password, dob, email, firstname, lastname, categ):
        # Process the account creation form data
        us_username = self.username_entry.get()
        us_password = self.password_entry.get()
        us_dob = self.dob_entry.get()
        us_mail = self.email_entry.get()
        us_fs = self.firstname_entry.get()
        us_ls = self.lastname_entry.get()
        us_categ = self.user_type_var.get()

        if not (us_username and us_password and us_dob and us_mail and us_fs and us_ls):
            tk.messagebox.showerror("Error", "Entries not filled")
            return

        if not Verify.check_username(us_username):
            tk.messagebox.showerror("Error", "Username already exists")
            return
        if not Verify.checkpass(us_password):
            tk.messagebox.showerror("Error", "Invalid password")
            return
        if not Verify.dobchk(us_dob):
            tk.messagebox.showerror("Error", "Invalid date of birth")
            return
        if not Verify.check_mail(us_mail):
            tk.messagebox.showerror("Error", "Invalid email address")
            return

        with open("user_info.txt", "a") as f:
            f.write(f"{us_username} {us_password} {us_categ} {us_mail} {us_fs} {us_ls} {us_dob}\n")

        tk.messagebox.showinfo("Success", "Account created successfully")

    def login(self):
        # Create a new window for the login form
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")

        # Add form elements for the login
        username_label = tk.Label(login_window, text="Username:")
        username_label.grid(row=0, column=0)
        username_entry = tk.Entry(login_window)
        username_entry.grid(row=0, column=1)

        password_label = tk.Label(login_window, text="Password:")
        password_label.grid(row=1, column=0)
        password_entry = tk.Entry(login_window, show="*")
        password_entry.grid(row=1, column=1)

        # Create "Login" and "Back" buttons using grid
        login_button = tk.Button(login_window, text="Login", command=lambda: self.process_login(
            username_entry.get(), password_entry.get()))
        login_button.grid(row=2, column=0, columnspan=2)
        back_button = tk.Button(login_window, text="Back", command=login_window.destroy)
        back_button.grid(row=3, column=0, columnspan=2)

        # Add a "Return to Main Menu" button
        return_button = tk.Button(login_window, text="Return to Main Menu", command=login_window.destroy)
        return_button.grid(row=3, column=0, columnspan=2)

    def process_login(self, username, password):
        # Process the login form data
        with open("user_info.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                if len(data) >= 3:
                    if data[0] == username and data[1] == password:
                        # Successfully logged in
                        if data[2] == "student":
                            self.root.withdraw()  # Hide the login window
                            self.show_student_frame()
                            return
                        elif data[2] == "parent":
                            self.root.withdraw()  # Hide the login window
                            self.show_parent_frame()
                        else:
                            messagebox.showinfo("Success", "Login successful! User type: " + data[2])
                            return
            else:
                messagebox.showinfo("Error", "Incorrect username or password")

    def show_student_frame(self):
        student_frame = tk.Toplevel(self.root)  # Create a new top-level window
        student_frame.title("Student Frame")
        student_frame.geometry("400x400")  # Adjust the size as needed
        student_frame.protocol("WM_DELETE_WINDOW", self.on_student_frame_close)  # Handle window close

        student_app = StudentFrame(student_frame)
        student_app.pack()

    def on_student_frame_close(self):
        self.root.deiconify()  # Show the main User window when the StudentFrame is closed

    def show_parent_frame(self):
        parent_frame = tk.Toplevel(self.root)  # Create a new top-level window
        parent_frame.title("Student Frame")
        parent_frame.geometry("400x400")  # Adjust the size as needed
        parent_frame.protocol("WM_DELETE_WINDOW", self.on_parent_frame_close)  # Handle window close

        parent_app = ParentFrame(parent_frame)
        parent_app.pack()

    def on_parent_frame_close(self):
        self.root.deiconify()  # Show the main User window when the StudentFrame is closed

    def help(self):
        # Load and display the help text from your "help.txt" file
        with open("help.txt", "r") as f:
            help_text = f.read()

        help_window = tk.Toplevel(self.root)
        help_window.title("Help")

        # Create a Text widget to display the help text with scrolling
        help_text_widget = tk.Text(help_window, wrap=tk.WORD)
        help_text_widget.grid(row=0, column=0, columnspan=2)

        # Insert the help text into the Text widget
        help_text_widget.insert(tk.END, help_text)

        # Create a vertical scrollbar for scrolling
        scrollbar = tk.Scrollbar(help_window, orient=tk.VERTICAL, command=help_text_widget.yview)
        scrollbar.grid(row=0, column=2, sticky="ns")
        help_text_widget.config(yscrollcommand=scrollbar.set)
        help_text_widget.config(state=tk.DISABLED)

        back_button = tk.Button(help_window, text="Back", command=help_window.destroy)
        back_button.grid(row=1, column=0, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = User(root)
    root.mainloop()
