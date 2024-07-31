
import tkinter as tk
from tkinter import messagebox, simpledialog

class AdminGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")

        self.logged_in = False

        # List of admin usernames and passwords
        self.admin_users = ["admin1", "admin2", "admin3"]
        self.admin_pass = ["admin1", "admin2", "admin3"]

        # Create a frame for the login interface
        self.login_frame = tk.Frame(root)
        self.login_frame.pack()

        # Username input
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        # Password input (with masking)
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        # Login button
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()

        # Create buttons for "View Student Details" and "Shutdown" and disable them initially
        self.student_details_button = tk.Button(self.login_frame, text="View Student Details", state=tk.DISABLED, command=self.view_student_details)
        self.student_details_button.pack()

        self.shutdown_button = tk.Button(self.login_frame, text="Shutdown", state=tk.DISABLED, command=self.shutdown)
        self.shutdown_button.pack()

        # Button to return to the main menu
        self.return_to_main_menu_button = tk.Button(root, text="Return to Main Menu", command=self.return_to_main_menu)
        self.return_to_main_menu_button.pack()

    def login(self):
        # Attempt to log in with entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
        if (username in self.admin_users) and (password == self.admin_pass[self.admin_users.index(username)]):
            # Successful login
            self.logged_in = True
            messagebox.showinfo("Login", "Logged in successfully.")
            self.username_entry.delete(0, tk.END)  # Clear the username entry
            self.password_entry.delete(0, tk.END)  # Clear the password entry
            self.username_entry.config(state=tk.DISABLED)
            self.password_entry.config(state=tk.DISABLED)
            self.login_button.config(state=tk.DISABLED)
            # Enable the buttons after a successful login
            self.student_details_button.config(state=tk.NORMAL)
            self.shutdown_button.config(state=tk.NORMAL)
        else:
            # Login failed
            messagebox.showerror("Login Error", "Invalid username or password.")

    def view_student_details(self):
        # View student details if logged in
        if self.logged_in:
            user = simpledialog.askstring("View Student Details", "Enter username for which you want details:")
            if user:
                details = self.get_student_details(user)
                if details:
                    messagebox.showinfo("Student Details", details)
                else:
                    messagebox.showerror("Student Not Found", "No details found for the entered username.")

    def shutdown(self):
        # Shutdown the program if logged in
        if self.logged_in:
            messagebox.showinfo("Shutdown", "Shutting down the program...")
            self.root.quit()
        else:
            messagebox.showerror("Access Denied", "You must be logged in to shut down the program.")

    def get_student_details(self, username):
        # Retrieve student details from a file
        with open("user_info.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split()
                if line[0] == username:
                    return " ".join(line)
        return None

    def return_to_main_menu(self):
        # Close the user window to return to the main menu
        self.root.destroy()

    def close(self):
        # Close the application
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    admin_gui = AdminGUI(root)
    root.mainloop()

