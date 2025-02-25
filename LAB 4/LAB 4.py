import json
import os

# Sample student records (StudentID, (FirstName, LastName), ClassStanding, MajorExam)
students = [
    ("123456", ("Domeld", "Manangan"), 85, 90),
    ("654321", ("Benedict", "Uggaddan"), 78, 88),
    ("987654", ("John", "Glema"), 92, 80),
]

current_file = "students.json"

def save_file(filename):
    with open(filename, "w") as file:
        json.dump(students, file)
    print("Records saved successfully.")

def open_file(filename):
    global students
    if os.path.exists(filename):
        with open(filename, "r") as file:
            students[:] = json.load(file)
        print("File loaded successfully.")
    else:
        print("File not found.")

def show_all_records():
    for student in students:
        print(student)

def order_by_last_name():
    sorted_students = sorted(students, key=lambda x: x[1][1])
    for student in sorted_students:
        print(student)

def order_by_grade():
    sorted_students = sorted(students, key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True)
    for student in sorted_students:
        print(student)

def show_student_record(student_id):
    for student in students:
        if student[0] == student_id:
            print(student)
            return
    print("Student not found.")

def add_record():
    student_id = input("Enter Student ID (6 digits): ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Student added successfully.")

def edit_record(student_id):
    for i, student in enumerate(students):
        if student[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully.")
            return
    print("Student not found.")

def delete_record(student_id):
    global students
    students = [student for student in students if student[0] != student_id]
    print("Record deleted successfully.")

def menu():
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            open_file(current_file)
        elif choice == "2":
            save_file(current_file)
        elif choice == "3":
            new_filename = input("Enter new filename: ")
            save_file(new_filename)
        elif choice == "4":
            show_all_records()
        elif choice == "5":
            order_by_last_name()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            show_student_record(student_id)
        elif choice == "8":
            add_record()
        elif choice == "9":
            student_id = input("Enter Student ID to Edit: ")
            edit_record(student_id)
        elif choice == "10":
            student_id = input("Enter Student ID to Delete: ")
            delete_record(student_id)
        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

menu()
