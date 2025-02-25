# Get user input
last_name = input("Enter last name: ").strip()
first_name = input("Enter first name: ").strip()
age = input("Enter age: ").strip()
contact_number = input("Enter contact number: ").strip()
course = input("Enter course: ").strip()

# Format the student information
student_info = (
    f"Last Name: {last_name}\n"
    f"First Name: {first_name}\n"
    f"Age: {age}\n"
    f"Contact Number: {contact_number}\n"
    f"Course: {course}\n"
    "----------------------------------\n"
)

# Save the information to students.txt
with open("students.txt", "a") as file:
    file.write(student_info)

# Confirmation message
print("Student information has been saved to 'students.txt'.")
