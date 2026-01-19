# Create a base class Animal and subclasses Dog and Cat. 
print("1")
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.speak()
c.speak()


# Create a class hierarchy for Vehicle → Car → ElectricCar.
print("2")
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def fuel_type(self):
        print("Car uses petrol or diesel")

class ElectricCar(Car):
    def fuel_type(self):
        print("Electric car uses battery")

e = ElectricCar()
e.move()
e.fuel_type()


# Implement method overriding in a base and derived class.
print("3")
class Shape:
    def area(self):
        print("Area not defined")

class Rectangle(Shape):
    def area(self):
        print("Area = length × breadth")

r = Rectangle()
r.area()

# Demonstrate multiple inheritance with two parent classes.
print("4")
class Father:
    def skill(self):
        print("Farming")

class Mother:
    def hobby(self):
        print("Planting")

class Child(Father, Mother):
    pass

c = Child()
c.skill()
c.hobby()


# Create a polymorphic function that works with different shapes.
print("5")
class Circle:
    def draw(self):
        print("Drawing Circle")

class Square:
    def draw(self):
        print("Drawing Square")

def draw_shape(shape):
    shape.draw()

draw_shape(Circle())
draw_shape(Square())


# Create a Bank system with SavingsAccount and CurrentAccount classes.
print("6")
class BankAccount:
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account Interest: 4%")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account Interest: 0%")

s = SavingsAccount()
c = CurrentAccount()
s.calculate_interest()
c.calculate_interest()

# Create a class with private attributes and getter/setter methods.
print("7")
class Student:
    def __init__(self):
        self.__marks = 0   # private attribute

    def set_marks(self, m):
        self.__marks = m

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(85)
print(s.get_marks())

# Create a Teacher and Student class to show inheritance.
print("8")
class Person:
    def role(self):
        print("I am a person")

class Teacher(Person):
    def role(self):
        print("I am a teacher")

class Student(Person):
    def role(self):
        print("I am a student")

t = Teacher()
s = Student()
t.role()
s.role()

# Create a MusicPlayer class and subclass Spotify to override play method.
print("9")
class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")

sp = Spotify()
sp.play()

# Demonstrate the use of super() in inheritance.
print("10")
class Animal:
    def __init__(self):
        print("Animal created")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")

d = Dog()
