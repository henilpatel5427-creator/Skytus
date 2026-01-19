# Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake. 
print("1")
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Speed after acceleration:", self.speed)

    def brake(self):
        self.speed -= 10
        print("Speed after brake:", self.speed)

car = Car("Kia", "Seltos", 50)
car.accelerate()
car.brake()


# Create a BankAccount class with deposit and withdraw methods.
print("2")
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Balance after withdrawal:", self.balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)


# Create a Student class with a method to calculate average marks. 
print("3")
class Student:
    def __init__(self, marks):
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s = Student([80, 70, 90])
print("Average marks:", s.average())


# Create a Rectangle class with methods to find area and perimeter. 
print("4")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(5, 3)
print("Area:", r.area())
print("Perimeter:", r.perimeter())


# Create an Employee class that displays salary details. 
print("5")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)

e = Employee("Darshil", 30000)
e.show_salary()


# Create a Book class to store title, author, and price, and display details. 
print("6")

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

b = Book("Python Basics", "Guido", 500)
b.display()


# Create a Circle class to find area and circumference. 
print("7")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

c = Circle(7)
print("Area:", c.area())
print("Circumference:", c.circumference())


# Create a Laptop class with a method to apply discounts on price. 
print("8")

class Laptop:
    def __init__(self, price):
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * percent / 100
        self.price -= discount
        print("Price after discount:", self.price)

l = Laptop(50000)
l.apply_discount(10)


# Create a Flight class with seat booking functionality. 
print("9")

class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked. Seats left:", self.seats)
        else:
            print("No seats available")

f = Flight(3)
f.book_seat()
f.book_seat()


# Create a Shop class with a method to add and list products.
print("10")

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("Products:", self.products)

s = Shop()
s.add_product("Laptop")
s.add_product("Mobile")
s.list_products()
