
# Q2 - Student Marks Analysis

# Create a list of student marks
student_marks = [78, 35, 92, 40, 61]

# Convert list into tuple
marks_tuple = tuple(student_marks)

# Display list and tuple
print("Student Marks List:", student_marks)
print("Data type of list:", type(student_marks))

print("Student Marks Tuple:", marks_tuple)
print("Data type of tuple:", type(marks_tuple))

# Find highest and lowest marks
print("Highest Marks:", max(student_marks))
print("Lowest Marks:", min(student_marks))

# Count students who scored at least 40
count_40 = student_marks.count(40)
count_above_40 = student_marks.count(61) + student_marks.count(78) + student_marks.count(92)

total_40 = count_40 + count_above_40

print("Students scoring at least 40:", total_40)

# Check whether all marks are within 0 to 100
valid_marks = (
    student_marks[0] >= 0 and student_marks[0] <= 100 and
    student_marks[1] >= 0 and student_marks[1] <= 100 and
    student_marks[2] >= 0 and student_marks[2] <= 100 and
    student_marks[3] >= 0 and student_marks[3] <= 100 and
    student_marks[4] >= 0 and student_marks[4] <= 100
)

print("Are all marks valid?", valid_marks)

# Changing an element in the list
student_marks[0] = 85
print("Modified List:", student_marks)

# Trying to change an element in the tuple
# marks_tuple[0] = 85

# Observation:
# A list is mutable, so its elements can be changed.
# A tuple is immutable, so its elements cannot be changed.
# Uncommenting the tuple assignment above will cause a TypeError.
