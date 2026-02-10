# Task-1
# fix the Mutable default argument bug 
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1))
print(add_item(2))

# Task-2
# check where the floating comparison fails 
import math
def check_sum():
    return math.isclose(0.1 + 0.2, 0.3)
print(check_sum())

# Task-3
#Analyze given code where recursion runs infinitely due to missing base case. Use AI to fix.
# fix the No base case bug in the recursive function
def countdown(n):
    if n == 0:
        return
    print(n)
    return countdown(n-1)
countdown(5)

# Task-4
#Analyze given code where a missing dictionary key causes error. Use AI to fix it
def get_value():
    data = {"a": 1, "b": 2,}
    return data.get("c")
print(get_value())

# Task-5
#Task: Analyze given code where loop never ends. Use AI to detect and fix it.
# Fix the Infinite loop
def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1
loop_example()

# Task-6
#Analyze given code where tuple unpacking fails. Use AI to fix it.
a, b, c = (1, 2, 3)
print(a, b, c)

#Task7: Analyze given code where mixed indentation breaks execution. Use AI to fix it.
def func():
    x = 5
    y = 10
    return x+y
print (func())

# Task8: Analyze given code with incorrect import. Use AI to fix.
# Bug: Wrong import
import math
print(math.sqrt(16))

# Task9: Analyze given code where a return inside a loop prevents full iteration. Use AI to fix it.
# Bug: Early return inside loop
def total(numbers):
    sum_total = 0
    for n in numbers:
        sum_total += n
    return sum_total
print(total([1,2,3]))

# Task10: Analyze given code where a variable is used before being defined. Let AI detect and fix the error.
# Bug: Using undefined variable
def calculate_area(length, width):
    return length * width
print(calculate_area(5, 10))

# Task11:Analyze given code where integers and strings are added incorrectly. Let AI detect and fix the error.
# Bug: Adding integer and string
def add_values():
    return 5 + int("10")
print(add_values())

#Task12 : Analyze code where a string is incorrectly added to a list.
# Bug: Adding string and list
def combine():
    return "Numbers: " + str([1, 2, 3])
print(combine())

# Task-13 : Detect and fix code where a string is multiplied by a float.
# Bug: Multiplying string by float
def repeat_text():
    return "Hello " * int(2.5)
print(repeat_text())

#Task-14 : Analyze code where None is added to an integer.
# Bug: Adding None and integer
def compute():
    value = 0
    return value + 10
print(compute())

Task-15 : Fix code where user input is not converted properly.
def sum_two_numbers(a, b):
    if a is None:
        a = int(input("Enter first number: "))
    if b is None:
        b = int(input("Enter second number: "))
    return a + b
print(sum_two_numbers(None, None))
