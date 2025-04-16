'''OOPS:
1. class
2. object
3. inheritance : i) Parent class : class whose properties are inherited by another class
                 ii) Child class: class that inherits properties from te parent class
                 types: i) single inheritance: occurs when child class inherits from only one parent class
                        ii) multiple inheritance: allows child class to inherit from more than one parent class
4. encapsulation
5. polymorphism
6. data abstraction'''
#single inheritance:
'''class Animal:
    def speak(self):
        print('Animal is speaking')
class Dog(Animal):
    def bark(self):
        print('Dog is barlking')
d = Dog()
d.speak()
d.bark()'''

# multiple inheritance:
'''class Father:
    def show_father(self):
        print("Father is working")
class Mother:
    def show_mother(self):
        print("Mother is working")
class Child(Father, Mother):
    def show_child(self):
        print("Child is working")
c = Child()
c.show_father()
c.show_mother()
c.show_child()'''

'''iii) multi-level inheritance: when a class inherits from another child class , forming a hierachy
'''
# eg
'''class Grandfather:
    def show_grandfather(self):
        print("Grandfather is working")
class Father:
    def show_father(self):
        print("Father is working")
class Child(Father):
    def show_child(self):
        print("Child is working")
c = Child()
c.show_grandfather()
c.show_father()
c.show_child()'''

'''hierarchical inheritance:
when multiple child class inherits from a single parent class'''
# eg
'''class Parent:
    def show_parent(self):
        print("Parent is working")
class Child1(Parent):
    def show_child1(self):
        print("Child1 is working")
class Child2:
    def show_child2(self):
        print("Child2 is working")
c1 = Child1()
c2 = Child2()
c1.show_parent()
c1.show_child1()
c2.show_parent()
c2.show_child2()'''

'''hybrid inheritance :mixture of two or more inheritance 
'''
# eg
'''class Animal:
    def speak(self):
        print("Animal is speaking")
class Mammal (Animal):
    def walk(self):
        print("Mammal is walking")
class Bird(Animal):
    def fly(self):
        print('Bird flies')
class Bat(Mammal, Bird):
    def bat_info(self):
        print("Bat is mammal")

b = Bat()
b.speak()
b.walk()
b.fly()
b.bat_info()'''


'''1. delivery manager
2. supervisor
3, onshore manager (outside the country)
4, offshore manager (inside the country)
5. team lead
6. consultants
7. developers : (2 to 5 years experience)
8. freshers

name, employee_id
class manager1
    which inherited from employee, supervisior, team lead, tester'''
