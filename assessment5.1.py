# Write a program to handle division by zero error.
print("1:")

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(a / b)
except ZeroDivisionError:
    print("cannot divide by zero")

# Write a program to handle invalid integer input.
print("2:")

try:
    n = int(input("Enter number:"))
    print(n)
except valueError:
    print("invalid number")

# Write a program to open a file and handle the “file not found” error.
print("3:")

try:
    f = open("abc.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")

# Write a program to demonstrate multiple exception blocks.
print("4:")

try:
    x = int(input("Enter X: "))
    y = int(input("Enter y:"))
    print(x/y)
except ValueError:
    print("Wrong input")
except ZeroDivisionError:
    print("Division by zero")

# Write a program to use finally for resource cleanup.
print("5:")

try:
    print(10/2)
finally:
    print("This always runs")


# Write a program to create a custom exception for invalid age (<18).
print("6:")

class ageError(Exception):
    pass
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise ageError
    print("Allowed")
except AgeError:
    print("Age must be 18 or more")

# Write a program to handle IndexError when accessing a list.
print("7:")

a = [1,2,3]

try:
    print(a[5])
except IndexError:
    print("Index error")


# Write a program that takes two numbers and handles all possible errors.
print("8:")

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except:
    print("Some error occurred")

# Write a program to log errors to a file instead of printing them.
print("9:")

import logging

logging.basicConfig(filename="log.txt", level=logging.ERROR)

try:
    print(10/0)
except Exception as e:
    logging.error(e)

# Write a program that validates an email format and raises an exception for invalid ones.
print("10:")

try:
    email = input("Enter email: ")
    if "@" not in email:
        raise Exception
        print("Valid email")
except:
    print("Invalid email")
