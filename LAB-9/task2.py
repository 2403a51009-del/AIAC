# Manually written comments explaining each line/block

class sru_student:
    # Constructor to initialize student attributes
    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # Store the student's name
        self.roll_no = roll_no  # Store the student's roll number
        self.hostel_status = hostel_status  # Store hostel status (Yes/No)
        self.fee_paid = False  # Track if the fee is updated/paid

    # Method to update the fee status
    def fee_update(self):
        self.fee_paid = True  # Set fee_paid to True to indicate fee is updated

    # Method to display all student details
    def display_details(self):
        print("Student Details:")  # Print header
        print(f"Name: {self.name}")  # Print student's name
        print(f"Roll No.: {self.roll_no}")  # Print student's roll number
        print(f"Hostel Status: {self.hostel_status}")  # Print hostel status
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")  # Print fee status

# Read values from console for student details
name = input("Enter student name: ")  # Take student's name as input
roll_no = input("Enter roll number: ")  # Take roll number as input
hostel_status = input("Hostel status (Yes/No): ")  # Take hostel status as input

# Create an instance of sru_student with the provided details
student = sru_student(name, roll_no, hostel_status)

# Ask if the student has paid the fee and update accordingly
fee_input = input("Has the student paid the fee? (Yes/No): ")  # Ask about fee payment
if fee_input.strip().lower() == "yes":
    student.fee_update()  # Update fee status if paid

# Display all details of the student
student.display_details()

# --- AI-generated inline comments for the same code below ---

class sru_student:
    # Initializes the sru_student object with name, roll_no, hostel_status, and sets fee_paid to False
    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # Assigns the name parameter to the object's name attribute
        self.roll_no = roll_no  # Assigns the roll_no parameter to the object's roll_no attribute
        self.hostel_status = hostel_status  # Assigns the hostel_status parameter to the object's hostel_status attribute
        self.fee_paid = False  # Initializes the fee_paid attribute as False

    # Updates the fee_paid attribute to True
    def fee_update(self):
        self.fee_paid = True  # Sets fee_paid to True

    # Prints the student's details including name, roll number, hostel status, and fee status
    def display_details(self):
        print("Student Details:")  # Prints a header for student details
        print(f"Name: {self.name}")  # Prints the student's name
        print(f"Roll No.: {self.roll_no}")  # Prints the student's roll number
        print(f"Hostel Status: {self.hostel_status}")  # Prints the student's hostel status
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")  # Prints whether the fee is paid

# Prompts the user to enter the student's name
name = input("Enter student name: ")  # Reads the student's name from input
# Prompts the user to enter the student's roll number
roll_no = input("Enter roll number: ")  # Reads the student's roll number from input
# Prompts the user to enter the student's hostel status
hostel_status = input("Hostel status (Yes/No): ")  # Reads the hostel status from input

# Creates a new sru_student object with the entered details
student = sru_student(name, roll_no, hostel_status)

# Prompts the user to indicate if the fee has been paid
fee_input = input("Has the student paid the fee? (Yes/No): ")  # Reads fee payment status from input
# If the input is 'yes', updates the fee status
if fee_input.strip().lower() == "yes":
    student.fee_update()  # Calls the fee_update method

# Calls the display_details method to print all student information
student.display_details()
