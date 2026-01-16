# Function to check if a number is prime.
print("1:")

def is_prime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return true
print(is_prime(9))

# Function to reverse a string.
print("2:")

def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

#  Function to find factorial. 
print("3:")

def factorial(n):
    fact = 1
    for i in range(1,n + 1):
        fact = fact * i
    return fact
print(factorial(5))


# Function to calculate simple interest.
print("4:")

def simple_interest(p, r, t):
    return (p * r * t) / 100

print(simple_interest(1000, 5, 2))


# Function to check if a word is palindrome.
print("5:")

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))


# Function to count vowels in a string.
print("6:")

def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count
print(count_vowels("hello"))


# Function to merge two lists. 
print("7:")

def merge_lists(a,b):
    return a + b
    print(merge_lists([1,2],[3,4]))


# Function to find GCD of two numbers.
print("8:")

def gcd(a, b):
    while b != 0:
        a,b = b, a % b
    return a
print(gcd(12,8))


# Function to find area of rectangle.
print("9:")

def area_rectangle(length, width):
    return length * width
print(area_rectangle(5, 4))


# Function to check Armstrong number.
print("10:")

def is_armstrong(n):
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    return total == n
print(is_armstrong(123))



