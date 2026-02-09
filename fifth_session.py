# 1. Conditional statements
# 2. User-defined

# code 1
# num = int(input('Enter an integer: '))

# if num > 0:
#     print('Number is Positive')
#     # nested IF
#     if num % 2 == 0:
#         print('Number is also even')
#     else:
#         print('Number is Odd')
# elif num == 0:
#     print('Number is Zero')
# else:
#     print('Number is Negative')

# code 2
# num1 = int(input('Enter an integer: '))
# num2 = int(input('Enter another integer: '))

# if num1 % 2 == 0 and num2 % 2 == 0:
#     print(num1 + num2)
# else:
#     print('One or both numbers are not even')

# User-Defined Function UDF
# a re-usable block of code

# def greet():#definition
#     print('Hi, User')

# greet()#calling


# function with parameters
# def greet(name):
#     print(f'Hello, {name}')

# user = input("Enter your name: ")
# greet('Ahmed')
# greet(user)

# function with return statement

def add(a, b):
    result = a + b #local variable
    # print(result) 
    return result

# print(result) 
print(add(5, 7))
sum = add(4, 9) #sum is global variable

def divide():
    division =sum / 2