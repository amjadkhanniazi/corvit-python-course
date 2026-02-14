# try except block
# try:
#     print("Try block started")
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed")

# multiple exceptions
# try:
#     number = int(input('Enter a number: '))
#     result = 10 /number
#     print(result)
# except ValueError:
#     print('Error: Invalid input. Plz enter a number')
# except ZeroDivisionError:
#     print('Error: Division by zero is not allowed')

# try-except-else-finally
# try:
#     file = open('file11.txt','r')
#     content = file.read()
# except FileNotFoundError:
#     print('File not found')
# else:
#     print('file read successful')
#     print(content)
# finally:
#     print('this block always execute')

# catching all exceptions
try:
    num=1/0
except Exception as e:
    print(f'Error: {e}')