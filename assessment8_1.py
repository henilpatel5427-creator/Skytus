# Create a custom math module and import it in another file. 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# Create a module to perform string operations. 
def count_vowels(s):
    return sum(1 for ch in s if ch.lower() in "aeiou")

def reverse_string(s):
    return s[::-1]


# Use random module to generate 5 random integers. 
print ("3:")
import random

for i in range(5):
    print(random.randint(1, 100))


# Use datetime module to display current date and time. 
print ("4:")
from datetime import datetime

now = datetime.now()
print("Current Date & Time:", now)


# Use math module to find factorial of a number. 
print ("5:")
import math

num = 5
print("Factorial:", math.factorial(num))



# Create a package shapes with modules for circle and rectangle. 
print ("6:")
from shapes.circle import area as circle_area
from shapes.rectangle import area as rectangle_area

print(circle_area(5))
print(rectangle_area(4, 6))


# Import multiple functions from one module and use them. 
print ("7:")
from math import sqrt, pow

print(sqrt(16))
print(pow(2, 3))



# Write a program to shuffle a list using random module.
print ("8:")
import random

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)


# Write a program to calculate the difference between two dates. 
print ("9:")
from datetime import date

d1 = date(2024, 1, 1)
d2 = date(2024, 1, 10)

diff = d2 - d1
print("Difference in days:", diff.days)


# Use os module to list files in a directory.
print ("10:")
import os

files = os.listdir(".")
print(files)
