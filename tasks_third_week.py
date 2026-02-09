# -Task-1 -Login Validation
# username = 'amjad'
# email = 'amjad@gmail.com'
# password = '123456789'

# if username == 'amjad' or email == 'amjad@gmail.com':
#     if password == '123456789':
#         print('Login Successful')
#     else:
#         print('Login Failed')
# else:
#     print('Login Failed')

# -Task-2 -Logical NOT Operator
# isLogedin = bool(int(input('Are you loged in? (1 for Yes, 0 for No): ')))
# if isLogedin:
#     print('Welcome')
# else:
#     print('Please login')

# -Task-3 -Calculator Function
# num1 = int(input('Enter a Number: '))
# num2 = int(input('Enter another Number: '))
# operator = input('Enter an operator: ')

# def calculate(num1, num2, operator):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         return num1 / num2
#     else:
#         return 'Invalid Operator'

# print(f'Result of {num1} {operator} {num2} is:',calculate(num1, num2, operator))

# -Task-4 -Pass or Fail Function
# marks = int(input('Enter your Marks: '))

# def check_marks(marks):
#     if marks >= 50:
#         return 'Pass'
#     else:
#         return 'Fail'

# result = check_marks(marks)
# print(result)

# Task-5 -Discount Calculator
# price = 4000
# isMember = True

# def calculate_discount(price, isMember):
#     if isMember and price >=3000:
#         return price * 0.9
#     else:
#         return price

# print(calculate_discount(price, isMember))

# -Task-6 -ATM Balance Checker
# balance = 5000
# withdrawal_amount = 500

# def atm(balance, withdrawal_amount):
#     if balance >= withdrawal_amount and withdrawal_amount > 0:
#         print('Withdrawal Successful')
#         return balance - withdrawal_amount
#     else:
#         print('Withdrawal Failed')
#         return balance

# print("Balance",atm(balance, withdrawal_amount))