#1. Print your name, age, and city in one line

name = "Henil Patel"
Age = 20
city = "Chikhli"

print(name,Age,city)

#2. Take user input for two numbers and print their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)

#3.Convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


#4. Store your name in a variable and print it in uppercase


name = "Henil Patel"
print(name.upper())


# 5. Ask the user for their birth year and calculate current age

Birth_year=int(input("Enter your Birth Year:"))
Current_Year=2026
  
Age = Current_Year - Birth_year
print("Your age is:", Age)

#6. Swap the values of two variables

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))


temp = a
a = b
b = temp

print("After swaping:")
print("a =", a)
print("b =", b)


#7. Calculate the area of a rectangle from user input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print("Area of rectangle:", area)


#8. Check if a number is positive or negative

num=float(input("Enter the number"))

if num>0 :
 print("Positive number")

elif num<0:
 print("Negative number")
else:
   print("Zero")


#9. Ask for two numbers and print their average
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

average = (a + b) / 2
print("Average:", average)


#10. Take favorite color as input and print it

color = input("Enter your favorite color: ")
print("Your favorite color is:", color)