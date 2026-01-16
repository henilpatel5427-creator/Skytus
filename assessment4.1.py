# Print numbers from 1 to 10.
print("1:")

for i in range(1, 11):
    print(i)

# Display multiplication table for a given number. 
print("2:")

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# Find factorial of a number.
print("3:")

n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

# Generate the first N Fibonacci numbers.
print("4:")

n = int(input("Enter N: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Check if a number is prime.
print("5:")

n = int(input("Enter number: "))
flag = 0

for i in range(2, n):
    if n % i == 0:
        flag = 1

if flag == 0 and n > 1:
    print("Prime number")
else:
    print("Not prime")


# Reverse a number (e.g., 123 → 321). 
print("6:")

n = int(input("Enter number: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

print("Reverse =", rev)


# Count digits in a number. 
print("7:")

n = int(input("Enter number: "))
count = 0

while n > 0:
    count += 1
    n = n // 10

print("Digits =", count)


# Find sum of even numbers between 1–100.
print("8:")

sum = 0

for i in range(2, 101, 2):
    sum += i

print("Sum =", sum)


# Print a pyramid pattern. 
print("9:")

rows = 5

for i in range(1, rows + 1):
    print("* " * i)


# Find all divisors of a number.
print("10:")

n = int(input("Enter number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

