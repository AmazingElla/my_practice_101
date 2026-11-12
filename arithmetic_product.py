'''
def arithmetic_product(num1, num2):
    if num1 * num2 <=  1000:
        return num1 * num2
    else:
        return num1 + num2

print(arithmetic_product(50, 20))
'''

'''
def cumulative_sum():
    previous_num = 0

    for num in range(10):
        total = num + previous_num
        print("Current:", num, "Previous:", previous_num, "Sum:", total)
        previous_num = num

print(cumulative_sum())
'''

'''
def even_slicing(s):
    start = 0
    stop = len(s) 
    step = 2

    for char in range(start, stop, step):
        result += s[char]

'''

'''
a = 5
b = 10

print(f"Before swap: A is {a}, and B is {b}")

a, b = b, a

print(f"After swap: A is {a}, B is {b}")
'''
'''
def swap_values(a, b):
    a, b = b, a
    return a, b

a = 5
b = 10

a, b = swap_values(a, b)
print(f"After swap: A is {a} and B is {b}")
'''
'''
def factorial(num):
    factorial = 1

    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
'''

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")