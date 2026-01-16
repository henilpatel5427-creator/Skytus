# Check if a person is eligible to vote (age ≥ 18).
print("1:")

age = int(input("Enter age:"))

if age >= 18:
    print("Eligible to vote")
else:
    print("not eligible")

# Grade calculator based on marks: 90+ = A, 80+ = B, else C. 
print("2:")

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")


# Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go. 
print("3:")

light = input ("Enter light clour: ")

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")

# ATM withdrawal check: sufficient balance or not. 
print("4:")

balance = 5000
withdraw = int(input("Enter amount: "))

if withdraw <= balance:
    print("Withdraw successful")
else:
    print("Insufficient balance")

# Check if a number is positive, negative, or zero. 
print("5:")

n = int (input("Enter number: "))

if n > 0:
    print("positive")
elif n < 0:
    print("nagative")
else:
    print("zero")

# Check if a number lies within a given range.
print("6:")

n = int(input("Enter number: "))

if n >= 10 and n <= 50:
    print("In range")
else:
    print("Out of range")


# Username & password verification. 
print("7:")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid login")


# Electricity bill calculator based on units consumed.
print("8:")

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2
else:
    bill = units * 3

print("Bill =", bill)


# Simple calculator (add, subtract, multiply, divide). 
print("9:")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)


# Check type of triangle (equilateral, isosceles, scalene).
print("10:")

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")



