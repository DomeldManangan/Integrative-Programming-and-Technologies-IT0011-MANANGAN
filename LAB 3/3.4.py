# Open the file in read mode
try:
    with open("students.txt", "r") as file:
        student_data = file.read()
    
    # Display the contents
    print("Reading Student Information:\n")
    print(student_data)

except FileNotFoundError:
    print("Error: 'students.txt' not found. Please add student information first.")