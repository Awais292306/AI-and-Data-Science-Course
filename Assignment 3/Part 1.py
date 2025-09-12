# Student Record Management System (Procedural Programming)

# We will use a list of dictionaries to store student records
students = []

# Function to add a new student record
def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Grade: ")

    # Create a student record as a dictionary
    student = {"roll_no": roll_no, "name": name, "grade": grade}

    # Add record to the students list
    students.append(student)
    print("Student record added successfully!\n")


# Function to display all student records
def display_students():
    if not students:
        print("No student records found!\n")
        return

    print("---- Student Records ----")
    for student in students:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Grade: {student['grade']}")
    print()


# Function to search a student by roll number
def search_student():
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student['roll_no'] == roll_no:
            print(f"Record Found -> Roll No: {student['roll_no']}, Name: {student['name']}, Grade: {student['grade']}\n")
            return
    print("Record not found!\n")


# Function to delete a student record by roll number
def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student['roll_no'] == roll_no:
            students.remove(student)
            print("Record deleted successfully!\n")
            return
    print("Record not found!\n")


# Function to update student details
def update_student():
    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student['roll_no'] == roll_no:
            print("Record Found. Enter new details.")
            student['name'] = input("Enter New Name: ")
            student['grade'] = input("Enter New Grade: ")
            print("Record updated successfully!\n")
            return
    print("Record not found!\n")


# Main menu (Procedural flow)
def main_menu():
    while True:
        print("[=======================================]")
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("[======================================]")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Program starts here
main_menu()
