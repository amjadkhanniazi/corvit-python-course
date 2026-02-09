# -strings
str1 = 'text'
str2 = 'this is some text'
str3 = '''this is a 
multiline
string'''

# print(str1)
# print(str2)
# print(str3)

# -indexing
# print(str1[1])
# print(str2[0])
# str1[0] = 'T'   # this will give error as strings are immutable

# -slicing
# print(str2[0:4])
# print(str2[5:])
# print(str2[::-1]) # reverse string
# print(str2[-6:]) # last 5 characters
# print(str2[-1:-7:-1]) # last 6 characters in reverse order

# -copy a string
# str4 = str2[:]
# print(str4)

# -string formatings
# user = 'amjad'
# city = 'karachi'
# print('hello,', user, 'from',city) # concatenation
# print('hello, {} from {}'.format(user, city)) # using format method -old method
# print(f'hello, {user} from {city}') # using f string -preferred method in python 3.6+

# -string methods
str5 = ' hello python '
# print(str5.strip()) # removes leading and trailing spaces
# print(str5.upper().strip()) # convert to uppercase and removes spaces
# print(str5.lower()) # convert to lowercase
print(str5.replace('python','world').upper().strip()) # replace a substring with another substring, convert to uppercase and removes spaces

# -conditional statements (if, else)

num1 = int(input("Enter a Number: "))
if num1 >= 18:
    print("You are 18 or older")
else:
    print("You are younger than 18")
