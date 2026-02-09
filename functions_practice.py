# -Simple function
# def greet():
#     print("Hello")

# greet()

# -function with parameters
# def greet(name):
#     print(f'Hello, {name}')

# greet("Amjad")

# -function with return statement
# def sum(a,b):
#     return a+b

# print(sum(2,6))

# -functions with default parameters
# def greet(name="Guest"):
#     print(f'Hello, {name}')

# greet()

# -multiple return values
# def stats(numbers):
#     return min(numbers), max(numbers), sum(numbers)

# minimum, maximum, total = stats([1,2,3,4,5,6])
# print(minimum, maximum, total)

# -variable scope
# global variable
# global_var = 'I am Global Variable'

# def my_function():
#     local_var = 'I am Local Variable'
#     print(global_var)
#     print(local_var)

# my_function()
# print(local_var) # error

# modifying global var

# counter = 0

# def increment():
#     global counter
#     counter += 1

# increment()
# print(counter)
# increment()
# print(counter)
# increment()
# print(counter)

# -recursive functions
# def fictorial(n):
#     if n ==1 or n==0:
#         return 1
#     else:
#         return n * fictorial(n-1)

# print(fictorial(5))

# febonacci series
# def febonacci(n):
#     if n<=1:
#         return n
#     else:
#         return febonacci(n-1) + febonacci(n-2)

# for i in range(4):
#     print(febonacci(i), end=" ")

# -lambda function
# regular function
# def square(x):
#     return x**2

# print(square(5))

# lambda function
# sqr = lambda x: x**2
# print(sqr(5))

# add = lambda a, b: a+b
# print(add(2,5))

# -Higher order functions
numbers = [1,2,3,4,5,6]
# map() function
# squared = list(map(lambda x: x**2, numbers))
# print(squared)

# filter() function
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# zip() function

names = ['Amjad', 'Khan', 'Niazi']
marks = [99, 100, 100]
# for name, marks in zip(names, marks):
#     print(f'Name: {name} | Marks: {marks}')

zipped = list(zip(names, marks))
print(zipped)