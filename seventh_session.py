# -List Methods
# cars = ['honda', 'toyota']
# cars_models = ['civic', 'corolla']
# cars[1] = 'united'

# add items
# cars.append('united')
# cars.insert(1, 'suzuki')


# remove items
# cars.remove('toyota')
# remove_item = cars.pop(3) # remove and return the removed item.
# cars.extend(cars_models)

# print(cars)

# -Dictionaries method
# modelss = {12.72663: 'civic', 'toyota': 'corolla'}
# print(modelss.keys())
# print(modelss.values())

# print(modelss.pop(12.72663))
# print(modelss)

# -LOOPS
# for loop: sequence of values and range of numbers
# for x in range(1,11):
#     print(x)

# for y in range(1, 15, 3):
#     print(y)

# for z in range(-15, -1, 2):
#     print(z)

# -for loop: for sequence of values
# -for with strings
# text = 'hello world'
# for x in text:
#     print(x)
# -for with lists
# cars = ['honda', 'toyota', 'suzuki']
# for x in cars:
#     print(x)

# -for with dictionaries
# student_marks = {'Amjad': 99, 'Khan': 100, 'Niazi': 100}
# for x in student_marks:
#     print(x)
#     print(student_marks[x])

# for x in student_marks.values():
#     print(x)

# for subjects, marks in student_marks.items():
#     print(f'subject: {subjects} | marks: {marks}')

# for loop for number of iterations are confirmed and while loop where number of iteration are not confirmed

# -while loop
# x = 2
# while x < 10:
#     print(x)
#     x +=1

num = int(input('Enter a number: '))
sum = 0
while num > 0:
    sum += num
    num = int(input('Enter a number: '))
print(sum)