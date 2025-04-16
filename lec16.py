# OOPS
'''why we use oops concept: building codes with operates on
 the properties of an real life entity, object oriented programming where every variable is object
 and we have different classes with different properties.
 classes are the blueprints of object.(eg: 'Car' characterisitics of car)
 object are the instances of class. or
 object are real life entities which have a blueprint(class)
 eg: 'Car' : "Toyoto"
constructor in python: is use to initialise the attributes of an objects.
types of Constructor:default constructor,Parameterized Constructor
Syntax : __init__(self)
Syntax:
class ClassName:
        def __init__(self, parameters):
                self.attribute1 = value1
                self.attribute2 = value2'''

# eg: 1
'''class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.make}, {self.model}, {self.year}")

car1 = Car("ford","Mustang","1999")
car1.display_info()'''

# define a class for student with attribute : name , age and grade
# create an instance of the class and print their details
'''class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display_details(self):
        print(f"{self.name}, {self.age}, {self.grade}")

student1 = Student("ABC","20","A+")
student1.display_details()'''

# Inheritance:
'''includes some properties of parent class.'''

# TCS: how will u include inheritance in the program

'''class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super(). __init__(name)         
        self.breed = breed
    def speak(self):
        print(f"{self.name} barks")

dog1 = Dog("German Shepherd", "Rex")
dog1.speak()'''

# supper() refers to supperclass = allowing you to access the properties from
                                        # child class

# multiple inhertiance:
'''class A:
    def __init__(self):
        print("Class A constructor called")
    def speak(self):
        print("Class A speak called")
class B:
    def __init__(self):
        print("Class B constructor called")
class C(A,B):
    def __init__(self):
        super(). __init__()
        print("Class C constructor called")
    def speak(self):
        print("Class A speak called")'''




