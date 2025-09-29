# Student Record Management System (Procedural Programming)

students = []  # Global list to store student records

# Function to add a student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    age = input("Enter Age: ")

    student = {
        "roll": roll,
        "name": name,
        "course": course,
        "age": age
    }
    students.append(student)
    print("Student added successfully!\n")


# Display all students
def display_students():
    if not students:
        print("No student records found.\n")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print(f"Roll: {s['roll']}, Name: {s['name']}, Course: {s['course']}, Age: {s['age']}")
        print()


# Search student by roll number
def search_student():
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found -> Roll: {s['roll']}, Name: {s['name']}, Course: {s['course']}, Age: {s['age']}\n")
            return
    print("Student not found.\n")


# Update student
def update_student():
    roll = input("Enter Roll Number to update: ")
    for s in students:
        if s["roll"] == roll:
            print("Enter new details (leave blank to keep old value):")
            name = input(f"New Name ({s['name']}): ") or s['name']
            course = input(f"New Course ({s['course']}): ") or s['course']
            age = input(f"New Age ({s['age']}): ") or s['age']

            s["name"] = name
            s["course"] = course
            s["age"] = age
            print("Student updated successfully!\n")
            return
    print("Student not found.\n")


# Delete student
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")

def main():
    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run program
main()
