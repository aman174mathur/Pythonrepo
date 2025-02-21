#INHERITANCE
#SINGLE INHERITANCE: A class can inherit from 
# only one parent class.
'''class Employee:
    def __init__(self,loacation):
        self.__location=loacation
    def get_location(self):
        print("name of location is :",self.__location)

class Manager(Employee):
    def get_project(self):
        print("project name is working....")

sam= Employee('jaipur')
#sam.get_location()
Mohit = Manager('delhi')
Mohit.get_project()
Mohit.get_location()'''

'''#MULTIPLE INHERITANCE: A class can inherit from more 
# than one parent class.

class Engine:
    def start_engine(self):
        print("Engine started")

class Wheels:
    def rotate_wheels(self):
        print("Wheels are rotating")

class race:
    def race(self):
        print("Racing is started")

class Car(Engine,Wheels,race):
    def drive(self):
        print("Car is driving")
    
my_car= Car()
my_car.start_engine()
my_car.rotate_wheels()
my_car.drive()
my_car.race()'''


#Multi - level inheritance: A class can inherit from a class
# that has inherited from another class.

'''class Grandparent:
    def grandparent(self):
        print("calling grandparent")

class Parent(Grandparent):
    def parent(self):
        print("calling parent")

class Child(Parent):
    def child(self):
        print("calling child")

aman= Child()
aman.grandparent()
aman.parent()
aman.child()'''

#case study : ecommerce order mangement
#customer class: name and contact details
#product class: with name and price
#order class: with customer and product details
#requirements:
#customer should have 
#product should have product details
#order should generate an order summary

class customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def order_summary(self):
        total = sum([product.price for product in self.products])
        summary = f"order summary for {self.customer.name}:\n"
        for product in self.products:
            summary += f"product name: {product.name}\n price: {product.price}\n"
        summary += f"your total is : {total}"
        return summary

cus1 = customer("aman", "1234567890")
prod1 = product("HAIR-GEL", 1000)
prod2=product("shower-gel",200)
order1 = order(cus1, [prod1, prod2])
print(order1.order_summary())