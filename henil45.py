#1.Calculate the remainder of two numbers.
a=33
b=15
reminder=a%b
print(reminder)
#2. Check if a number is even or odd.
c = ["10","11","12"]
for i in c:
    num = int(i)
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
#3. Compare two numbers and print the larger one.
d = ["450","500"]
largenum = max(d)
print(largenum)

#4. Write a program to calculate the square and cube of a number.
num = int(input("enter a num: "))
square = num**2
cube = num**3
print(square)
print(cube)
#5. Check if two entered numbers are equal.
a=5
b=5
if a==b:
    print("same")
else:
    print("not same")
#6. Take two numbers and print True if both are positive, else False.
a=5
b=-6
if a <=0 & b <=0:
    print("positive")
else:
    print("negative")
#7. Write a program to convert float to integer.
num = float(input("enter a num= "))
int_num = int(num)
print(int_num)
#8. Take a number as string, convert to int, and multiply by 10.
num_str = "7"      
num_int = int(num_str)  
result = num_int * 10   
print(result)
#39. Write a program that uses and & or operators to check multiple conditions.
num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("The number is positive and even")
if num < 0 or num > 100:
    print("The number is either negative or greater than 100")

#10. Divide two numbers and print the
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = a / b
print("Result:", result)