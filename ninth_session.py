# break and continue statements
# for x in range(10):
#     if x == 4:
#         break # breaks and terminates the loop
#     print(x)

# print('----')

# for x in range(10):
#     if x == 5:
#         continue # skips the current iteration and continues with the next iteration
#     print(x)

# -List Comprehension
# traditional way using a loop
lst1 = [1,2,3,4,5,6,7,8,9]
# lst2 = []
# for x in lst1:
#     lst2.append(x**2)
# print(lst2)

# -using list comprehension
# lst2 = [x ** 2 for x in lst1]
# print(lst2)

# -even numbers using list comprehension
# even_list = [x for x in lst1 if x % 2 == 0 and x < 7]
# print(even_list)

# list comprehension using nested loop
c = [(x,y) for x in range(3) for y in range(3)]
print(c)