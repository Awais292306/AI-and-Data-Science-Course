# Data Filtering and Prosessing.

while True:
        try:
            age = int(input("Enter your age: "))
            if age > 20:
                print(f"Your age is {age}")
                break
            else:
                print("Age must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
