# using print statement
# def calculate_avg(numbers):
#     print(f'DEBUG: Numbers Recieved: {numbers}')
#     total = sum(numbers)
#     print(f'DEBUG: total: {total}')
#     num_len = len(numbers)
#     print(f'DEBUG: num_len: {num_len}')
#     avg = total / num_len
#     print(f'DEBUG: Avg: {avg}')
#     return avg
# avrg = calculate_avg([1,2,3,4,5])

# using assert statement
# def devide(a,b):
#     assert b!=0
#     return a/b
# result = devide(10,0)
# print(result)

# try-except for debugging
def safe_devide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Error: Division by zero is not allowed: {e}')
        return None
result = safe_devide(10,2)
print(result)