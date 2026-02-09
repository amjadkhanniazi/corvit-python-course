# -strings
str1 = 'text'
str2 = "text"
str3 = '''this is a 
multiline
string'''
str4 = '123456789'

# print(str1)
# print(str2)
# print(str3)

# -indexing
# print(str1[6])
# str1[0] = 'T'  # this will give error as strings are immutable

# -slicing
# print(str3[0:4])
# print(str3[5:])
# print(str3[4::1])
# print(str3[::-1])  # reverse string
# print(str3[-1:-6:-1])  # last 5 characters in reverse order
# print(str4[::-1])  # reverse string using slicing
#print(str4[-4:-2]) # slicing using negative indexing

# -copy a string
# str5 = str4[:]
# print(str5)

# -string formatings
# user = 'amjad'
# city = 'karachi'
# print("hello,", user, "from", city) # concatenation
# print("hello, {} from {}".format(user, city)) # using format method -old method
# print(f'hello, {user} from {city}') # using f string -preferred method in python 3.6+

# -string methods, a method is that act on value changes it and returns a new value, original value remains unchanged
# difference between function and method is that method is associated with object whereas function is independent
# str6 = ' hello world '
# print(str6.strip().upper()) # convert to uppercase
# print(str6.lower()) # convert to lowercase
# print(str6.strip()) # removes leading and trailing spaces
# print(str6.replace('world', 'there')) # replace a substring with another substring

# -conditional statements (if, else)

num1 = int(input("Enter a Number: "))

if num1 >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# -check even odd
num2 = int(input("Enter a Number: "))
if num2 % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
