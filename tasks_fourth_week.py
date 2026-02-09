# Section-A
# Task-1 -Counting Numbers

# for i in range(1, 11):
#     print(i)

# Task-2 -Sum of N Numbers
# num1 = int(input('Enter a Number: '))
# sum = 0
# for i in range(1, num1+1):
#     sum += i
# print(sum)

# -Task-3 -Count Characters in a String
# str1 = input('Enter a String: ')
# count = 0
# for i in str1:
#     count += 1
# print(count)

# Task-4 -Multiplication Table
# num1 = int(input('Enter a Number: '))
# for i in range(1, 11):
#     print(f'{num1} x {i} = {num1*i}')

# Section-B
# Task-5
# num = 1
# while (num <= 10):
#     print(num)
#     num += 1

# Task-6
# num = int(input('Enter a Number: '))
# sum = 0
# while (num > 0):
#     sum += num
#     num=int(input('Enter a Number: '))
# print(sum)

# -Task-7
# password = 'python123'
# enteredPass = input('Enter a Password: ')
# while (password != enteredPass):
#     print('Incorrect Password')
#     enteredPass = input('Enter a Password: ')
# print('Correct Password')

# -Task-8
# num = int(input('Enter a Number: '))
# count = 0
# while (num > 1):
#     num = num /10
#     count += 1
# print(count)


# -Section-C
# -Task-9
str1 = input('Enter a String: ')
for i in str1:
    print(i)

strLength = len(str1)
ind = 0
while (ind < strLength):
    print(str1[ind])
    ind += 1