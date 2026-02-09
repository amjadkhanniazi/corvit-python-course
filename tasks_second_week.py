# -Task-1
# name = input("Enter your name: ");
# age = int(input("Enter your age: "));
# height = float(input("Enter your height in CMs: "));

# print(f'My name is {name}, I am {age} years old and my height is {height}cms');

# -Task-2
# integer_num = 89
# float_num = 78.98
# string_val = "Python Programming"
# boolean_val = True

# print(f'the type of {integer_num} is {type(integer_num)}')
# print(f'the type of {float_num} is {type(float_num)}')
# print(f'the type of {string_val} is {type(string_val)}')
# print(f'the type of {boolean_val} is {type(boolean_val)}')

# -Task-3
# num1 = int(input("Enter a Number: "))
# num2 = int(input("Enter another Number: "))

# print(f'addition: {num1 + num2}')
# print(f'subtraction: {num1 - num2}')
# print(f'Multiplication: {num1 * num2}')
# print(f'Division: {num1 / num2}')

# -Task-4
# studentName = input("enter student name: ")
# marks1 = int(input("enter marks1: "))
# marks2 = int(input("enter marks2: "))
# marks3 = int(input("enter marks3: "))

# totalMarks = marks1 + marks2 + marks3
# averageMarks = totalMarks/3

# print(f'student name: {studentName}')
# print(f'total marks: {totalMarks}')
# print(f'average marks: {averageMarks}')


# -Task-5
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))

# print(f'Greater than: {num1 > num2}')
# print(f'Less than: {num1 < num2}')
# print(f'Equal to: {num1 == num2}')
# print(f'Not equal to: {num1 != num2}')

# -Task-6
# age = int(input('enter your age: '));
# hasCnic = bool(int(input('do you have CNIC? (1 for Yes, 0 for No): ')));
# isEligible = age >= 18 and hasCnic
# if isEligible:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# -Task-7
# balance = 1000

# balance += 500
# print("Add Using assignment Operators: ", balance)
# balance -= 200
# print("subtract using assignment operators: ", balance)
# balance *= 2
# print("multiply using assignment operators: ", balance)
# balance /= 4
# print("divide using assignment operators: ", balance)

# -Task-8
# word1 = input("enter a word: ")
# print("1st character: ", word1[0])
# print("last character: ", word1[-1])

# -Task-9
# username generator
# full_name = input('enter your full name: ')
# list_name = full_name.split()
# username = list_name[0].lower() + '_' + list_name[-1].lower()
# print("Generated username: ", username)

# -Task-10
# str1 = input('Enter a Sentence: ')
# print("first 5 characters: ", str1[:5])
# print("last 5 characters: ", str1[-5:])
# print('sentence without 1st and last character: ', str1[1:-1])

# -Task-11
# str1 = input('Enter a string: ')
# print("Length of string: ", len(str1))
# print("string in uppercase: ", str1.upper())
# print("string in lowercase: ", str1.lower())
# # number of time a character occurs
# print("number of times 'a' occurs: ", str1.count('a'))

# -Task-12
import string
# String constants
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.printable)
# String Formators
# String Substitutes
t = string.Template("$name likes $food")
print(t.substitute(name="Amjad Khan", food="Biryani"))

location="lahore"

t2 = string.Template("welcome to $location, We serve everyone with $word")
print(t2.substitute(location=location, word="Care"))