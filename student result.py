def calculate_result():
    student_number = input("Enter student number: ")
    student_name = input("Enter student name: ")
    marks1 = float(input("Enter marks in subject 1: "))
    marks2 = float(input("Enter marks in subject 2: "))
    marks3 = float(input("Enter marks in subject 3: "))

    total_marks = marks1 + marks2 + marks3
    average_marks = total_marks / 3

    print("Total marks:", total_marks)
    print("Average marks:", average_marks)

    if average_marks >= 75:
        print("Result: Distinction")
    elif average_marks >= 60:
        print("Result: First Class")
    elif average_marks >= 50:
        print("Result: Second Class")
    elif average_marks >= 35:
        print("Result: Third Class")
    else:
        print("Result: Fail")

calculate_result()
