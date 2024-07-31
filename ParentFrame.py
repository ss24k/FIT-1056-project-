


import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

# Create a class for the ParentFrame that inherits from tk.Frame
class ParentFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.logged_in = True  # Simulating a logged-in state

        # Display a welcome message for the parent.
        welcome_label = tk.Label(self, text="Welcome, Parent!")
        welcome_label.grid(row=0, column=0, padx=10, pady=10)

        # Create buttons for different options.
        options = [
            "View Child's Information",
            "Set Time Goal",
            "Set Topic Goal"
        ]

        for index, option_text in enumerate(options, start=1):
            option_button = tk.Button(self, text=option_text, command=lambda text=option_text: self.handle_option(text))
            option_button.grid(row=index, column=0, padx=10, pady=10)

    # Function to handle different options when buttons are clicked
    def handle_option(self, option_text):
        if option_text == "View Child's Information":
            self.view_child_details()
        elif option_text == "Set Time Goal":
            self.set_time_goal()
        elif option_text == "Set Topic Goal":
            self.set_topic_goal()

    # Function to get the child's username via a dialog
    def get_username(self):
        self.user = tk.simpledialog.askstring("Input", "Enter your child's username:")

    # Function to view child's information
    def view_child_details(self):
        if self.logged_in:
            self.get_username()  # Get the child's username from the user
            with open("user_info.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip().split()
                    if len(line) >= 7 and line[0] == self.user:
                        # Assuming the order of information in the file is as follows:
                        us_username, us_password, us_categ, us_mail, us_fs, us_ls, us_dob = line
                        if us_categ == "student":
                            info_window = tk.Toplevel(self)
                            info_window.title("Child's Information")
                            labels = ["Username", "Category", "Email", "First Name", "Last Name", "Date of Birth"]
                            values = [us_username, us_categ, us_mail, us_fs, us_ls, us_dob]
                            for i in range(len(labels)):
                                tk.Label(info_window, text=f"{labels[i]}: {values[i]}").grid(row=i, column=0, padx=10, pady=10)
                        else:
                            tk.messagebox.showinfo("Information", "Child is not a student.")
                        break
                else:
                    tk.messagebox.showinfo("Information", "User not found.")
        else:
            tk.messagebox.showinfo("Information", "You are not logged in!")

    # Function to set a time goal for a student
    def set_time_goal(self):
        if self.logged_in:
            try:
                time = int(tk.simpledialog.askstring("Input", "Enter the time goal (0-15 hours):"))
                if 0 <= time <= 15:
                    with open("user_info.txt", "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            line = line.split()
                            if line[2] == "student":
                                with open("time_goal.txt", "a") as file2:
                                    file2.write(line[0] + " " + str(time) + "\n")
                                tk.messagebox.showinfo("Information", "Time goal set successfully")
                                return
                        tk.messagebox.showinfo("Information", "No student found in user_info.txt.")
                else:
                    tk.messagebox.showinfo("Information",
                                           "Invalid time input. Time goal must be an integer value between 0 and 15.")
            except ValueError:
                tk.messagebox.showinfo("Information", "Invalid input. Please enter a valid integer for the time goal.")
        else:
            tk.messagebox.showinfo("Information", "You are not logged in!")

    # Function to set a topic goal for a student
    def set_topic_goal(self):
        if self.logged_in:
            try:
                topic = int(tk.simpledialog.askstring("Input", "Enter the topic goal (1-3):"))
                if 0 < topic <= 3:
                    username = tk.simpledialog.askstring("Input", "Enter the student's username:")
                    password = tk.simpledialog.askstring("Input", "Enter the student's password:")

                    with open("user_info.txt", "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            line = line.split()
                            if line[0] == username and line[1] == password and line[2] == "student":
                                with open("topic_goal.txt", "a") as file2:
                                    file2.write(username + " " + str(topic) + "\n")
                                tk.messagebox.showinfo("Information", "Topic goal set successfully")
                                return
                        tk.messagebox.showinfo("Information", "User not found or invalid credentials.")
                else:
                    tk.messagebox.showinfo("Information",
                                           "Invalid topic goal input. Topic goal must be an integer between 1 and 3.")
            except ValueError:
                tk.messagebox.showinfo("Information", "Invalid input. Please enter a valid integer for the topic goal.")
        else:
            tk.messagebox.showinfo("Information", "You are not logged in!")

if __name__ == "__main__":
    root = tk.Tk()
    parent_frame = ParentFrame(root)
    parent_frame.pack()
    root.mainloop()







































# import tkinter as tk
#
# class Student:
#     def __init__(self):
#
#
#      def handle_student_menu(self, user_type, root):
#         text_label.config(text="Student Menu")
#         welcome_label.config(text="Welcome to Code Venture - Student")
#
#         if user_type == "student":
#             student_window = tk.Toplevel(root)
#             student_frame = tk.Frame(student_window)
#             student_frame.pack()
#
#             # Create buttons for the student menu
#             buttons = [
#                 "Study Python Concepts",
#                 "Take Python Quiz",
#                 "Add Date to Calendar",
#                 "View Calendar",
#                 "View Grades",
#                 "Help",
#                 "Exit"
#             ]
#
#             for button_text in buttons:
#                 button = tk.Button(student_frame, text=button_text)
#                 button.pack()
#
#         elif user_type == "parent":
#             parent_window = tk.Toplevel(root)
#             parent_frame = tk.Frame(parent_window)
#             parent_frame.pack()
#
#             # Create buttons for the parent menu
#             buttons = [
#                 "View Student Information",
#                 "Set Time Goal",
#                 "Set Topic Goal",
#             ]
#
#             for button_text in buttons:
#                 button = tk.Button(parent_frame, text=button_text)
#                 button.pack()
#
#         else:
#             print("Invalid user type")
#
# # Create the root window
# root = tk.Tk()
# root.title("Code Venture")
# root.geometry("400x300")
#
# # Create labels
# text_label = tk.Label(root, text="Student Menu")
# text_label.pack()
# welcome_label = tk.Label(root, text="Welcome to Code Venture - Student")
# welcome_label.pack()
#
# # Create an instance of the Student class
# student = Student()
#
# # Start the tkinter main loop
# root.mainloop()
# import os
# import re
# import tkinter as tk
# from tkinter import simpledialog, messagebox
# from user import User
# from parent import Parent
#
#
# class Student(User):
#     def __init__(self, username, password):
#         self.root = tk.Tk()
#         super().__init__(self.root)
#         self.username = username
#         self.password = password
#         self.logged_in = False
#         self.question_number = 1  # Initialize question_number here
#         self.quiz_score = 0
#         self.total_questions = 0
#         self.correct_answers = ["b","b","b","d","b","c","c","b","c","b"]
#
#         self.root = tk.Tk()
#         self.root.title("Student Login")
#
#         self.username_label = tk.Label(self.root, text="Username:")
#         self.username_entry = tk.Entry(self.root)
#         self.password_label = tk.Label(self.root, text="Password:")
#         self.password_entry = tk.Entry(self.root, show="*")
#         self.login_button = tk.Button(self.root, text="Login", command=self.login)
#
#         self.message_label = tk.Label(self.root, text="")
#
#         self.username_label.pack()
#         self.username_entry.pack()
#         self.password_label.pack()
#         self.password_entry.pack()
#         self.login_button.pack()
#         self.message_label.pack()
#
#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#
#         with open("user_info.txt", "r") as file:
#             lines = file.readlines()
#             for line in lines:
#                 user_info = line.strip().split(", ")
#                 us_username, us_password, us_categ, *_ = user_info
#
#                 if us_username == username and us_password == password:
#                     if us_categ == "student":
#                         self.logged_in = True
#                         self.message_label.config(text="Login successful!")
#                         return
#                     else:
#                         self.message_label.config(text="You are not a student!")
#                         return
#
#             self.message_label.config(text="Invalid username or password.")
#
#     def select_topic(self):
#         topic_files = [file for file in os.listdir() if file.startswith("topic_") and file.endswith(".txt")]
#
#         if not topic_files:
#             messagebox.showinfo("Topics", "No topic files found.")
#             return
#
#         available_topics = "Available topics:\n"
#         for i, topic_file in enumerate(topic_files, 1):
#             available_topics += f"{i}. {topic_file}\n"
#
#         choice = simpledialog.askinteger("Select a Topic",
#                                          prompt="Enter the number of the topic you would like to study(1/2/3):")
#
#         if 1 <= choice <= len(topic_files):
#             selected_topic = topic_files[choice - 1]
#             with open(selected_topic, "r", encoding="utf8") as file:
#                 content = file.read()
#                 messagebox.showinfo("Topic Contents", content)
#         else:
#             messagebox.showinfo("Invalid Choice", "Invalid choice. Please select a valid topic.")
#
#     def view_targets(self):
#         time_goal = None
#         topic_goal = None
#         with open("time_goal.txt", "r") as f1:
#             lines1 = f1.readlines()
#             for line1 in lines1:
#                 line1 = line1.split()
#                 if line1[0] == self.username:
#                     time_goal = line1[1]
#
#         with open("topic_goal.txt", "r") as f2:
#             lines2 = f2.readlines()
#             for line2 in lines2:
#                 line2 = line2.split()
#                 if line2[0] == self.username:
#                     topic_goal = line2[1]
#
#         if time_goal is not None and topic_goal is not None:
#             message = f"Time Goal: {time_goal} hours\nTopic Goal: {topic_goal} topics"
#             messagebox.showinfo("Your Goals", message)
#         else:
#             messagebox.showinfo("Goals Not Found", "Your goals could not be found.")
#
#
#     def take_quiz(self):
#         quiz_files = ["Quiz_1.txt", "Quiz_2.txt", "Quiz_3.txt"]
#
#         for quiz_file in quiz_files:
#             with open(quiz_file, "r", encoding="utf8") as file:
#                 lines = file.readlines()
#                 current_question = ""
#                 options = []
#
#                 for line in lines:
#                     line = line.strip()
#                     if line.startswith("Q"):
#                         if current_question:
#                             self.total_questions += 1
#                             correct_option = self.ask_question(current_question, options)
#                             if correct_option:
#                                 self.quiz_score += 1
#                         current_question = line
#                         options = []
#                     elif line.startswith("(a)") or line.startswith("(b)") or line.startswith("(c)") or line.startswith(
#                             "(d)"):
#                         options.append(line)
#
#                 # Process the last question
#                 if current_question:
#                     self.total_questions += 1
#                     correct_option = self.ask_question(current_question, options)
#                     if correct_option:
#                         self.quiz_score += 1
#
#         if self.total_questions == 0:
#             messagebox.showinfo("No Questions", "No quiz questions found.")
#         else:
#             score_percentage = (self.quiz_score / self.total_questions) * 100
#             if score_percentage >= 80:
#                 messagebox.showinfo("Quiz Result",
#                                     f"Quiz completed with a score of {score_percentage}%.\nCongratulations, you passed!")
#             else:
#                 messagebox.showinfo("Quiz Result",
#                                     f"Quiz completed with a score of {score_percentage}%.\nYou need to reattempt the quiz.")
#
#     def ask_question(self, question, options):
#         # Extract question and options
#         question_text = question.split(") ")[1]
#         options_text = "\n".join(options)
#
#         # Display the question and options
#         user_answer = simpledialog.askstring(f"Quiz Question {self.question_number + 1}",
#                                              f"{question_text}\n{options_text}")
#
#         # Check the user's answer against the correct answers list
#         if user_answer and user_answer.strip().lower() in ["a", "b", "c", "d"]:
#             selected_option = options[ord(user_answer) - ord("a")]
#             correct_option = self.correct_answers[self.question_number]
#
#             if selected_option.startswith(f"({correct_option})"):
#                 self.question_number += 1  # Increment question number here
#                 return True
#
#         return False
#
#     def view_targets(self):
#
#      with open("time_goal.txt","r") as f1:
#                 f2 = open("topic_goal.txt","r")
#                 lines = f2.readlines()
#                 lines1 = f1.readlines()
#                 for line in lines1:
#                     line = line.split()
#                     if line[0] == self.username:
#                         time_goal = line[1]
#                 for line1 in lines:
#                     line1 = line1.split()
#                     if line1[0] == self.username:
#                         topic_goal = line1[1]
#                 print("time goal =",time_goal,"topic goal =",topic_goal)
#                 f2.close()
#     def run(self):
#         self.root.mainloop()
#
# if __name__ == "__main__":
#     student = Student("your_username", "your_password")
#     student.run()

