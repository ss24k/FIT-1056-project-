class Verify:
    @staticmethod
    def check_username(username):
        # Check if the given username exists in the user_info.txt file
        with open("user_info.txt", "r") as f:
            for line in f:
                line = line.strip().split()  # Split each line into words
                if line and line[0] == username:  # Check if the line is not empty and the first word matches the username
                    return False  # Username already exists
        return True  # Username is available

    @staticmethod
    def checkpass(password):
        if len(password) >= 6:
            char = 0
            num = 0
            xtra = 0
            for i in password:
                if i.isdigit():
                    num += 1
                elif i.isalpha():
                    char += 1
                else:
                    xtra += 1
            if num != 0 and char != 0 and xtra != 0:
                return True  # Password meets the requirements
            return False  # Password does not meet the requirements

    @staticmethod
    def dobchk(dob):
        dob1 = dob.split(":")
        if len(dob1) != 3:
            return False  # The date should consist of day, month, and year

        day, month, year = dob1
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            return False  # Day, month, and year should be numeric.

        day = int(day)
        month = int(month)
        year = int(year)

        if month < 1 or month > 12:
            return False  # Month is out of range (1-12).

        if year < 1913 or year > 2023:
            return False  # Year is out of range (1913-2023).

        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days[1] = 29  # Leap year, February has 29 days

        if day < 1 or day > days[month - 1]:
            return False  # Day is out of range for the given month.

        return True  # The date is valid.

    @staticmethod
    def check_mail(mail):
        if "@" in mail:
            return True  # The email address is valid
        return False  # The email address is invalid

