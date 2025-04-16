# encapsulation:
'''restriction of access to particular object for
the prevention of the accidental modification of data.

access specifier :
i) public: access to everyone.
ii) protected members: access within the class and by subclass.
iii) private members: access within the class. intended from the outside access'''

# public :
# eg: (living room)
# syntax: name
'''class House:
    def __init__(self, address): # constructor created
        self.address = address
    def doorbell(self):
        print("Doorbell rang at", self.address)
my_house = House("123 House")   # create instance
print(my_house.address)
my_house.doorbell()'''  # anyone can ring the bell

# protected : kitchen
# syntax : _name
'''class House:
    def __init__(self, address):
        self._kitchen_access = True     
    def _cook_meal(self):
        print("Cooking meal")
class Family(House):
    def use_kitchen(self):
        if self._kitchen_access:
            self._cook_meal()
family = Family("123 Family")
family.use_kitchen()'''    # only within the class can access

# private : master bedroom
# syntax : __name
'''class House:
    def __init__(self, address):
        self.__master_bedroom_code = "moksh123"
    def __enter_master_bedroom(self):
        print("Entering master bedroom:", self.__master_bedroom_code)
    def access_master_bedroom(self):
        self.__enter_master_bedroom()
my_house = House("123 House")
my_house.access_master_bedroom()'''

# Encapsulation : (Coffee Machine)
'''class CoffeeMachine:
    def __init__(self):
        self.__water_tank = 1000
    def __heat_water(self):
        print("Heat water")
    def __grind_beans(self):
        print("Grind beans")
    def make_coffee(self):
        self.__heat_water()
        self.__grind_beans()
        print("Coffee is ready")
machine = CoffeeMachine()
machine.make_coffee()'''

'''class MyClass:
    def __init__(self):
        self._protected_variable = "Protected variable"
        self._access_flag = False
    def set_access_flag(self, flag):
        self._access_flag = flag
    def get_protected_variable(self):
        if self._access_flag:
            return self._protected_variable
        else:
            return "Access denied"
obj = MyClass()
print(obj.get_protected_variable())
obj.set_access_flag(True)
print(obj.get_protected_variable())'''


'''Flag : under what condn give the access to anyone
        flexible'''

'''today's assessment :
create a book class private attributes, public method
test scenarios:
1. create an instance of a book 
2. borrow a book and check available copies
3. return the book and verify no. of copies available/ counts of books'''

'''class Book:
    def __init__(self, title, author, total_copies):
        self.__title = title
        self.__author = author
        self.__total_copies = total_copies
        self.__available_copies = total_copies

    def borrow(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print(f"You have successfully borrowed '{self.__title}'.")
        else:
            print(f"Sorry, '{self.__title}' is currently unavailable.")

    def return_book(self):
        if self.__available_copies < self.__total_copies:
            self.__available_copies += 1
            print(f"Thank you for returning '{self.__title}'.")
        else:
            print(f"Error: The number of copies for '{self.__title}' is already at maximum.")

    def available_copies(self):
        return self.__available_copies

# 1. Create an instance of a book
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 5)

# 2. Borrow a book and check available copies
print(f"Available copies of '{book1._Book__title}': {book1.available_copies()}")
book1.borrow()
print(f"Available copies of '{book1._Book__title}': {book1.available_copies()}")

# 3. Return the book and verify the number of copies available/counts of books
book1.return_book()
print(f"Available copies of '{book1._Book__title}': {book1.available_copies()}")'''
