# -lists 
cities = ['lahore', 23, 34.22, 'Khan', 'Karachi'] # can be same or different types of items, mutable, ordered
# print(cities);
# print(type(cities))
# print(type(cities[2]))

# -list Indexing
# print(cities[0])
# cities[2]= 'Multan'
# print(cities)

# -Slicing
# print(cities[1:3])
# new_cities=cities[0:3]
# print(new_cities)
# print(cities[::-1])


# -tuples
# subjects = ("this", 'this', 2, 3.44454, 2) # immutable, ordered, heterogenous
# print(subjects)
# print(type(subjects[3]))

# -Sets  mutable | un ordered no indexes | duplication not allowed
# set1 = {1, 2, 3.566, 4, 2, 3}
# set2 = {'a01', 'a02', 'a03', 'a02'}
# print(set1)
# print(set2)
# print(type(set1))
# print(type(set2))

# -Dictionary  mutable | ordered | duplication not allowed for keys
# student_marks = {'Amjad': 99, 'Khan': 100, 'Amjad': 100}
# print(student_marks)
# print(type(student_marks))

# -revision fifth session

def greet(name):
    print('hello {}'.format(name))
def summm(a,b):
    return a+b;

# name='Amad'
# greet(name)

num1 = 2
num2 = 4
print(summm(num1, num2))