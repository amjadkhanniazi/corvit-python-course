# Nested Data Structures and Nested Loops

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(matrix[1][1])
# print(matrix[1])
# print(matrix)

# for row in matrix: # outer loop
#     for items in row: # Inner Loop
#         print(items, end=" ")
#     print()

# list of dictionaries
# students = [
#     {'name': 'Amjad', 'marks': 99},
#     {'name': 'Khan', 'marks': 100},
#     {'name': 'Niazi', 'marks': 100}
# ]

# dictionary of dictionaries
students = {
    'Ali': {'maths': 100, 'english': 78},
    'Khan': {'maths': 98, 'english': 100}
}
# print(students['Ali']['english'])

# Student Name: 
# Subject 1:
# Subject 2: 
# n = 1
# for student, subjects in students.items():
#     n = 1
#     print(f'Student Name: {student}')
#     for subject, marks in subjects.items():
#         print(f'Subject {n}')
#         print(f'name: {subject} | marks: {marks}')
#         n += 1
#     print('----------')

# iterating a list with range method
# lst1 = [1,2,3,4,5,6]
# for i in range(len(lst1)):
#     print(lst1[i], end=", ")

# count even numbers in a nested list
count = 0
for rows in matrix:
    for items in rows:
        if items % 2 == 0:
            count += 1
print(f'Even Numbers in Matrix: {count}')