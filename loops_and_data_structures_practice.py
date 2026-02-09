matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# sum = 0
# for rows in matrix:
#     for items in rows:
#         sum += items
# print(sum)

# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# transpose = []
# for i in range(len(matrix[0])):
#     row=[]
#     for j in range(len(matrix)):
#         row.append(matrix[j][i])
#     transpose.append(row)

# for row in transpose:
#     print(row)

# nested dictionaries

stu_records = {
    'Stu1' : {
        'name': 'Amjad',
        'Age': 21,
        'Grades': {
            'Maths': 99,
            'English': 100
        }
    },
    'Stu2' : {
        'name': 'Khan',
        'Age': 23,
        'Grades': {
            'Maths': 85,
            'English': 99
        }
    },
}

# for student_id, info in stu_records.items():
#     print(f'Student ID: {student_id}')
#     for key, value in info.items():
#         print(f'{key}: {value}')
#     print('---')

stu_records['Stu3'] = {
    'name': 'Niazi',
    'Age': 22,
    'Grades': {
        'Maths': 100,
        'English': 100
    }
}

for student_id, info in stu_records.items():
    print(f'Student ID: {student_id}')
    for key, value in info.items():
        print(f'{key}: {value}')
    print('---')