#1 Calculate the remainder of two numbers.
a = 15
b = 4
print("1: Remainder:", a % b)

#2 Check if a number is even or odd.
c = 7
if c % 2 == 0:
    print("2: Even or Odd: Even")
else:
    print("2: Even or Odd: Odd")


#3 Compare two numbers and print the larger one.
d = 10
e = 20
if d > e:
    print("3: Larger number:", d)
else:
    print("3: Larger number:", e)


#4 Write a program to calculate the square and cube of a number.
f = 5
print("4: Square:", f ** 2)
print("Cube:", f ** 3)

#5 Check if two entered numbers are equal.
g = 12
h = 12
if g == h:
    print("5:",g, h, "number equal")
else:
    print("5:",g, h, "number not equal")

#6 Take two numbers and print True if both are positive, else False.
i = 5
j = 10
if i > 0 and j > 0:
    print("6: Both positive: True")
else:
    print("6: Both positive: False")

#7 Write a program to convert float to integer.
k = 9.8
print("7: Float to int:", int(k))
#8 Take a number as string, convert to int, and multiply by 10.
l = "15"
print("8: String to int and multiply by 10:", int(l) * 10)
#9 Write a program that uses and & or operators to check multiple conditions.
m = 10
n = 20
if (m < 15 and n > 15) or (m == 10):
    print("9: Condition met: True")
else:
    print("9: Condition met: False")

#10 Divide two numbers and print the quotient and remainder separately.
o = 25
p = 6
print("10: Quotient:", o // p)
print("Remainder:", o % p)
