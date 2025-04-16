# polymorphism : many forms
# importance: enables flexibility and reusability in code
# types :
# i) compile time : (Method Overloading) resolved at the time of compilation
# ii) run-time : (Method Overriding)

# overloading :multiple methods in same class with same name but different parameters.

# overriding : subclass provides a specific type of implementation which is already define in superclass which modify or extend the behaviour.

# python doesn't support overloading directly

# eg: Overloading
'''class Calculator:
    def add(self, a, b, c=0):
        return a + b + c
calc = Calculator()
print(calc.add(1, 2))
print(calc.add(1, 2, 3))'''

# eg: Overriding
'''class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()'''    # overriding

# eg:
'''class Animal:
    def sound(self):
        return"Animal makes a sound"
class Dog(Animal):
    def sound(self):
        return"Dog barks"
class Cat(Animal):
    def sound(self):
        return"Cat"
def make_animal(Animal):
    print(animal.sound())
animal = Animal()
dog = Dog()
cat = Cat()
make_animal(animal)
make_animal(dog)
make_animal(cat)'''

# eg:
'''class Device:       # base class : device
    def send_notification(self, message):
        raise NotImplementedError("subclasses must implement send_notification")
class Phone(Device):
    def send_notification(self, message):
        print(f"Phone notification : {message}")
class laptop(Device):
    def send_notification(self, message):
        print(f"Laptop notification:{message}")
def notify(device, message):
    device.send_notification(message)
devices = [Phone(), laptop()]
for device in devices:
    notify(device, "You have new message")'''

# data abstraction: Hiding implementation details

# eg:
'''class Car:
    def start_engine(self):
        raise NotImplementedError("subclasses must implement start_engine")
    def horn(self):
        raise NotImplementedError("subclasses must implement start_engine")
class Tata(Car):
    def start_engine(self):
        print("Tata starts")
    def horn(self):
        print("Tata horns")
class SUV(Car):
    def start_engine(self):
        print("SUV Starts")
    def horn(self):
        print("SUV Horns")
def operate_car(car):
    car.start_engine()
    car.horn()
tata = Tata()
suv = SUV()
operate_car(tata)
operate_car(suv)'''

'''today's assesssment
1. polmorphism : atm program
2. abstraction : classes : food , methods used , pass use 
o\p: pizza *  2 - A dinner_table
    burger * 1 - B
    [('pizza', 2)]
    [('burger', 1)]'''





