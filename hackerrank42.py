from collections import namedtuple

# Read the number of students
n = int(input())

# Read the field names and create the namedtuple class
fields = input().split()
Student = namedtuple("Student", fields)

# Initialize a list to store the marks
marks_lst = []

# Read the student data and extract the marks
for _ in range(n):
    data = input().split()  # Split the input to match the fields
    student = Student(*data)  # Create a Student namedtuple instance
    marks_lst.append(int(student.MARKS))  # Append the marks to the list

# Calculate and print the average marks
print(sum(marks_lst) / n)

