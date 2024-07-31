
import tkinter as tk
from tkinter import simpledialog
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox


class StudentFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.topic_window = None
        self.quiz_window = None
        self.user_answers = []  # List to store user's answers

        welcome_label = tk.Label(self, text="Welcome, Student!")
        welcome_label.grid(row=0, column=0, padx=10, pady=10)

        options = [
            "Study Python Concepts",
            "Take Python Quiz",
            "Add Date to Calendar",
            "View Calendar",
            "View Grades",
            "View Targets",
            "Exit"
        ]

        for index, option_text in enumerate(options, start=1):
            option_button = tk.Button(self, text=option_text, command=lambda text=option_text: self.handle_option(text))
            option_button.grid(row=index, column=0, padx=10, pady=10)

    def handle_option(self, option_text):
        if option_text == "Study Python Concepts":
            topic_number = simpledialog.askinteger("Study Python Concepts", "Enter the topic number:")
            if topic_number is not None:
                self.study(topic_number)
        elif option_text == "Take Python Quiz":
            username = simpledialog.askstring("Enter your username", "Please Enter your username:")
            if username is not None:
                self.take_quiz(username)
        elif option_text == "Add Date to Calendar":
            self.add_date()
        elif option_text == "View Calendar":
            self.view_calendar()
        elif option_text == "View Grades":
            self.view_grades()
        elif option_text == "View Targets":
            self.view_targets()
        elif option_text == "Exit":
            self.close_frame()

    def study(self, topic_no):
        topic = "topic " + str(topic_no) + ".txt"

        self.topic_window = tk.Toplevel(self.master)
        self.topic_window.title("Study Python Concepts - Topic {}".format(topic_no))

        text_widget = ScrolledText(self.topic_window, wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True)

        with open(topic, "r") as f:
            topic_content = f.read()
            text_widget.insert(tk.END, topic_content)

        back_button = tk.Button(self.topic_window, text="Back to Main Menu", command=self.return_to_main_menu)
        back_button.pack()

    def take_quiz(self, username):
        # Define the quiz questions and correct answers
        questions = [
            "Q1) What is the output of the following code: print(9//2)\n(a) 4.5\n(b) 4.0\n(c) 4\n(d) error",
            "Q2) Which of the following is not a complex number?\n(a) -4+3J\n(b) 12+3i\n(c) 2+3j\n(d) k=complex(4,5)",
            "Q3) What is the output of the following statement: print(22%3)\n(a) 7\n(b) 1\n(c) 0\n(d) 5",
            "Q4) Which of the following is NOT a core data type?\n(a) Lists\n(b) Dictionary\n(c) Tuples\n(d) Class",
            "Q5) What is the output of the following statement: print(3*1**3)\n(a) 27\n(b) 3\n(c) 1\n(d) 9",
            "Q6) What will be the output of print(24//6%3) gives\n(a) 6\n(b) 12\n(c) 1\n(d) None of the above",
            "Q7) What is the output of the following code-:\nx,y=20,60\ny,x,y = x,y-10,x+10\nprint(x,'&',y)\n(a) 60 & 30\n(b) 50 & 50\n(c) 50 & 30\n(d) 30 & 50",
            "Q8) What is the output of the following program-:\ni=10\nif i<15: print('i is less than 15')\n(a) Nothing will be printed\n(b) i is less than 15\n(c) Error in the code\n(d) None of the above",
            "Q9) Identify the valid identifier out of the following-:\n(a) item*qty\n(b) $price\n(c) price\n(d) for",
            "Q10) Which among the following list of operators has the highest precedence-:\n+, -, **, %, /, <<, >>, |\n(a) <<\n(b) **\n(c) +\n(d) %"
        ]

        correct_answers = ["b", "b", "b", "d", "b", "c", "c", "b", "c", "b"]

        # Initialize the score
        score = 0

        # Display each question and collect the user's answers
        for i, question in enumerate(questions):
            user_answer = simpledialog.askstring("Quiz Question {}".format(i + 1), question)
            if user_answer and user_answer.lower() == correct_answers[i]:
                score += 1

        result_text = "Your score is: {}/10".format(score)  # Use 'score' instead of 'self.score'
        if score >= 8:
            result_text += "\nYou have scored {} marks out of 10 - passed".format(score)
        else:
            result_text += "\nYou have scored {} marks out of 10 - failed".format(score)
            result_text += "\n1. Attempt again 2. Quit"
            choice = simpledialog.askstring("Quiz Result", result_text)
            if choice == "1":
                self.take_quiz(username)  # Call the function again to attempt the quiz
            elif choice == "2":
                self.master.destroy()

        # Record the score to a file
        with open("grade_var.txt", "a") as f:
            f.write(username + "-quiz-" + str(score) + " marks" + "\n")

    def view_calendar(self):
        self.calendar_window = tk.Toplevel(self.master)
        self.calendar_window.title("Calendar Dates")

        calendar_text = tk.Text(self.calendar_window)
        calendar_text.pack()

        # Read the calendar file and display its content
        with open("calendar.txt", "r") as f:
            calendar_content = f.read()
            calendar_text.insert(tk.END, calendar_content)
            calendar_text.config(state=tk.DISABLED)


    def add_date(self):
        username = simpledialog.askstring("Enter your username", "Please Enter your username:")
        date_dead = simpledialog.askstring("Enter the date", "Please Enter date in the format (dd:mm:yyyy): ")
        topic_add = simpledialog.askstring("Enter the topic", "Please enter a name for the deadline: ")

        if username and date_dead and topic_add:
            with open("calendar.txt", "a") as f:
                f.write(username + " " + date_dead + " - " + topic_add + "\n")
            messagebox.showinfo("Success", "Deadline added successfully")

    def view_grades(self):
        username = simpledialog.askstring("Enter your username", "Please Enter your username:")
        if username:
            found = False
            # Create a Tkinter window
            grades_window = tk.Tk()
            grades_window.title("Grades")

            with open("grade_var.txt", "r") as f:
                lines = f.readlines()
                grade_message = ""  # Initialize an empty string to store the grades message
                for line in lines:
                    line = line.strip().split("-")
                    if line[0] == username:
                        found = True
                        # Append the grade information to the message string
                        grade_message += f"{line[0]} - Quiz {line[1]} - {line[2]} marks\n"

            if found:
                # Create a Message widget and display the grades
                grade_msg = tk.Message(grades_window, text=grade_message, width=200)
                grade_msg.pack()
            else:
                messagebox.showinfo("Error", "User not found or no quiz scores available for this user.")

            # Start the Tkinter main loop to display the grades window
            grades_window.mainloop()

    def view_targets(self):
        self.username = simpledialog.askstring("Enter your username", "Please Enter your username:")

        if self.username:
            time_goal = None
            topic_goal = None

            # Read the time_goal.txt file and find the time goal for the user
            with open("time_goal.txt", "r") as f1:
                lines1 = f1.readlines()
                for line in lines1:
                    line = line.split()
                    if line[0] == self.username:
                        time_goal = line[1]

            # Read the topic_goal.txt file and find the topic goal for the user
            with open("topic_goal.txt", "r") as f2:
                lines2 = f2.readlines()
                for line in lines2:
                    line = line.split()
                    if line[0] == self.username:
                        topic_goal = line[1]

            if time_goal is not None and topic_goal is not None:
                message = "Time goal = {} Topic goal = {}".format(time_goal, topic_goal)
                messagebox.showinfo("Message", message)
            else:
                messagebox.showinfo("Error", "User not found or goals not set.")

    def return_to_main_menu(self):
        self.close_topic_window()  # Close the topic window if it's open
        self.master.lift()  # Bring the main menu window to the top
        self.master.deiconify()  # Show the main menu window

    def close_topic_window(self):
        if self.topic_window is not None:
            self.topic_window.destroy()
            self.topic_window = None

    def close_frame(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    student_frame = StudentFrame(root)
    student_frame.pack()
    root.mainloop()








































